import argparse

# These are the options you can give the web crawler
parser = argparse.ArgumentParser(description = 'Customize your web crawler with the following options.')

parser.add_argument('-u','--url',
					type = str,
					help = 'give the URL you would like to crawl')

parser.add_argument('-o','--output',
					type = str,
					help = 'Give the name of the directory you want to store the result in')

parser.add_argument('-b','--bots',
					type = int,
					default = 2,
					help = 'Specify the number of bots (spiders) that must crawl simultaneously')

args = parser.parse_args()