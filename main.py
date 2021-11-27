#!/usr/bin/env python

import internetarchive as ia
import requests
from bs4 import BeautifulSoup
import random
import lyricsgenius
import wikipedia
from config import *

genius = lyricsgenius.Genius(open('.env').read())
genius.remove_section_headers = True

def get_item_text(item):
	for file in ia.get_files(item):
		if file.name.endswith('.txt'):
			url = f'http://archive.org/stream/{file.identifier}/{file.name}'
			r = requests.get(url).text
			soup = BeautifulSoup(r, features='html.parser')
			text = soup.find('pre').text.replace('\n', '')[:WIDTH * NLINES]
			return text
	return None

def random_collection_item(collection, n):
	res = []
	search = ia.search_items(f'collection:({collection})', params={'rows': n}).iter_as_items()
	for i in range(n):
		print(i + 1, '/', n)
		res.append(next(search))
	return random.choice(res).identifier

TYPES = ['ia', 'genius', 'url', 'wiki']
srcs = []
while len(srcs) < NTEXTS:
	t = random.choice(TYPES)
	if t == 'ia':
		i = ('ia', random_collection_item(random.choice(COLLECTIONS), NITEMS))
	elif t == 'genius':
		i = ('genius', random.choice(ALBUMS))
	elif t == 'url':
		i = ('url', random.choice(URLS))
	elif t == 'wiki':
		i = ('wiki', None)
	if i not in srcs:
		srcs.append(i)
texts = []
for src in srcs:
	t, data = src
	if t == 'ia':
		texts.append(get_item_text(data))
	elif t == 'genius':
		blob = ''
		s = genius.search_album(*data[::-1])
		for track in s.tracks:
			blob += ' '.join(track.to_text().split('\n')[:-1])
			if len(blob) >= WIDTH * NLINES:
				break
		texts.append(blob)
	elif t == 'url':
		print(data)
		r = requests.get(data)
		if r.headers['Content-Type'] == 'text/plain':
			texts.append(r.text.replace('\n', '')[:WIDTH * NLINES])
		else:
			soup = BeautifulSoup(r.text, features='html.parser')
			texts.append(soup.find(['p', 'pre', 'li']).text.replace('\n', '')[:WIDTH * NLINES])
	elif t == 'wiki':
		res = None
		while res is None:
			try:
				page = wikipedia.random()
				print(page)
				res = wikipedia.page(page).content.replace('\n', '')[:WIDTH * NLINES]
			except wikipedia.exceptions.PageError: # error is thrown if the page cannot be found
				pass
		texts.append(res)

random.shuffle(texts)

cols = [random.randrange(0, len(texts))]
colcounts = [0]
last = cols[:]
layout = []
for i in range(NLINES):
	layout.append(cols)

	for c in range(len(cols)):
		if last[c] == cols[c]:
			colcounts[c] += 1
		if colcounts[c] == THRESHOLD:
			colcounts[c] == 0
			cols[c] += 1
			cols[c] %= len(texts)
	
	if random.uniform(0, 1) < SPLIT and len(cols) < MAXCOLS:
		choice = cols[0]
		while choice in cols:
			choice = random.randrange(0, len(texts))
		cols.append(choice)
		colcounts.append(0)
	elif random.uniform(0, 1) < MERGE and len(cols) > 1:
		cols = cols[:-1]
		colcounts.pop()

	last = cols[:]

pos = [0] * len(texts)
out = open('out.txt', 'w')
for i in range(len(layout)):
	print(i + 1, '/', len(layout))
	row = layout[i]
	line = ''
	size = WIDTH // len(row)
	for col in row:
		text = texts[col][pos[col]:pos[col] + size].lower()
		l = len(text) // 2
		a, b = text[:l], text[l:]
		line += ' ' + b + a
		pos[col] += size
		pos[col] %= len(texts[col])
	line = line.ljust(WIDTH + 4, ' ').replace('\t', ' ')
	print(line, file=out)
