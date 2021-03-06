# This is a very basic web crawler which extracts the HTML of the website 
# and gives the links present in it.

import requests
from bs4 import BeautifulSoup
from cli import args
# from selenium import webdriver


url = input('Enter the URL -- ')

# driver = webdriver.Firefox()
# driver.get(url)

html = requests.get(url)
soup = BeautifulSoup(html.text,'html.parser')

if args.output:
	f = open('data.txt','x')
	f.close()

def add_text(text):
	f = open('data.txt','a')
	f.write(text)
	f.close()

def file_or_print(text):
	if args.output:
		add_text(text)
	else:
		print(text)

# file_or_print('\n' + driver.title + '\n' + '\n')		

file_or_print(f'The links obtaines under {url} are :\n')

# Gives a list of the links in the domain specified by the user
for link in soup.findAll('a'):
	full_link = url + link.get('href')
	file_or_print(full_link + '\n')
	
file_or_print('\nThe other links obtained are :\n')

# Gives the other links in the website which are in <link> tag
for href in soup.findAll('link'):
	href = href.get('href')
	file_or_print(href + '\n')

if args.no_images != True:
	file_or_print('\nThe image titles and their corresponding links obtained are : \n')

# Gives the image title (string present in <img> tag) and the link to open the image
	for img in soup.findAll('img'):
		if img.get('string') == None:
			title = "This image has no title."
		else:
			title = img.get('string')
		file_or_print(str(title) + '\n')
	
		img = img.get('src')
		file_or_print(img + '\n')
	
file_or_print(f'\nThe bottons in {url} lead to the following links :\n')

# Gives the links the bottons in the given domain direct to, when clicked
for botton in soup.findAll('botton'):
	botton = botton.get('onclick')
	file_or_print(botton + '\n')

if args.contact != False:
	
	file_or_print(f'\nThe contact information found in {url} :\n')

# Gives the address if it is apecified in the <address> tag contact_info  in soup.findAll('address'):
	for contact_info in soup.findAll('address'):
		contact_info = contact_info.get('string')
		file_or_print(contact_info + '\n')
	
file_or_print(f'\nThe links given in {url} for reference are :\n')

# Gives the relevant link to the website from which the content in the given website is taken or relates to
for references in soup.findAll('bolckquote'):
	references = references.get('cite')
	file_or_print(references + '\n')

if args.output:
	f = open('data.txt','r')
	print(f.read())
	f.close()