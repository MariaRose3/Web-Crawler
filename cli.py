import argparse

# These are the options you can give the web crawler
parser = argparse.ArgumentParser(description = 'Customize your web crawler with the following options.')

parser.add_argument('-d','--depth',
	                 type = int,
	                 default = 1,
	                 help = 'specify the number of web pages you want to crawl')

parser.add_argument('-s','--screen_shots',
	          		action = 'store_true',  #when you give '-s' the the crawler will give you screen shots
	                help = 'specify whether you want the screenshots of the website')

parser.add_argument('-o','--output',
					action = 'store_true',
					help = 'specify whether you want to store the collected data in a file')

parser.add_argument('-a','--all',
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


args = parser.parse_args()