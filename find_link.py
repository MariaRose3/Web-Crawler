import requests
from bs4 import BeautifulSoup
import re

class FindLink():

	def __init__(self, base_url, page_url, headers):
		super().__init__()
		self.base_url = base_url
		self.page_url = page_url
		self.headers = headers
		self.domain_links = set()
		self.out_domain_links = set()

		html = requests.get(page_url, headers=headers)
		soup = BeautifulSoup(html.txt, 'html.parser')

	def tag_attr(self, tag, attr):
		for tag in soup.findall('attr'):
			if re.search('(^)'+url, tag.get('attr')):
				self.domain_links.add(tag.get('attr'))
			elif re.search('^http',tag.get('attr')):
				self.out_domain_links.add(tag.get('attr'))
			else:
				self.domain_links.add(url + tag.get('attr'))

	
	def links_not_in_domain(self):
		return self.out_domain_links

	def links_in_domain(self):
		return self.domain_links

	def error(self, message):
		pass
