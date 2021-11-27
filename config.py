WIDTH = 80
NLINES = 10000

NITEMS = 20 # numbers of items to pull from an archive.org collection when searching
NTEXTS = 20 # the number of texts to pull from
COLLECTIONS = [ # archive.org collections to pull from
	'mediahistory',
	'library_of_congress'
]
ALBUMS = [ # albums we can pull from
	('the cure', 'disintegration'),
	('the smashing pumpkins', 'adore'),
	('the get up kids', 'something to write home about'),
	('my bloody valentine', 'glider'),
	('slowdive', 'souvlaki'),
	('the cure', 'wish'),
	('broadcast', 'tender buttons'),
	('neutral milk hotel', 'in the aeroplane over the sea'),
	('the smiths', 'the queen is dead'),
	('my bloody valentine', 'loveless'),
	('catherine wheel', 'ferment'),
	('bauhaus', 'in the flat field'),
	('edie brickell & new bohemians', 'shooting rubberbands at the stars'),
	('the beatles', 'rubber soul'),
	('lush', 'lovelife'),
	('lush', 'split'),
	('the cure', '4:13 dream'),
	('dylan brady', 'dog show'),
	('james iha', 'look to the sky'),
	('pulp', 'his n hers'),
	('fleetwood mac', 'rumours')
]
URLS = [ # urls we can pull from
	'http://www.chaosmatrix.org/library/chaos/topy/tt100.txt',
	'http://www.chaosmatrix.org/library/chaos/topy/tt102.txt',
	'http://www.chaosmatrix.org/library/chaos/topy/tt103.txt',
	'http://www.chaosmatrix.org/library/chaos/topy/tt104.txt',
	'http://www.chaosmatrix.org/library/chaos/topy/tt105.txt',
	'http://www.chaosmatrix.org/library/chaos/topy/tt106.txt',
	'https://modernistcommons.ca/islandora/object/yale%3A352',
	'https://www.jacobinmag.com/2015/03/tokyo-firebombing-world-war-ii/',
	'http://onemodelnation.com/',
	'https://theanarchistlibrary.org/library/mary-nardini-gang-be-gay-do-crime',
	'https://ascii.co.uk/art/zodiac',
	'https://theanarchistlibrary.org/library/peter-gelderloos-anarchy-works/',
	'https://theanarchistlibrary.org/library/mary-nardini-gang-toward-the-queerest-insurrection',
	'https://theanarchistlibrary.org/library/mary-nardini-gang-what-is-it-to-become-beautiful',
	'http://www.geom.uiuc.edu/~huberty/math5337/groupe/digits.html'
]

THRESHOLD = 20 # the number of times lines from one text can be used in a row
SPLIT = 0.3 # the chance a new column is added each step
MERGE = 0.65 # the chance that if there is more than one column one goes away
MAXCOLS = 6 # maximum number of columns, should be less than number of texts

