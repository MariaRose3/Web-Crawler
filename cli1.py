import argparse

# These are the options you can give the web crawler
parser = argparse.ArgumentParser(description = 'Customize your web crawler with the following options.')

parser.add_argument('-u','--url',
					type = str,
					help = 'give the URL you would like to crawl')

parser.add_argument('-o','--output',
					type = str,
					help = 'Give the name of the directory you want to store the result in')

parser.add_argument('-d','--depth',
	                 type = int,
	                 default = 1,
	                 help = 'specify the number of web pages you want to crawl')

parser.add_argument('-b','--bots',
					type = int,
					default = 2,
					help = 'Specify the number of bots (spiders) that must crawl simultaneously')

'''parser.add_argument('-a','--all',
					action = 'store_true',
					help = 'crawl all the links obtained (even those not in the given domain)')

parser.add_argument('-i','--no_images',
					action = 'store_true',
					help = "give this option only if you don't want the links of images in the website")

parser.add_argument('-x','--content',
					action = 'store_true',
					help = 'specify whether you want the content of the website')

parser.add_argument('-c','--contact',
					action = 'store_false',
					help = "give this option only if you don't want the contact information in the website")

parser.add_argument('-s','--screen_shots',
	          		action = 'store_true',  #when you give '-s' the the crawler will give you screen shots
	                help = 'specify whether you want the screenshots of the website')

'''
args = parser.parse_args()