from find_link import FindLink
from file_manage import *

# Here, we're trying to make multiple bots, i.e. a certain number of links are crawed simultaneously,
# instead of crawling one by one. the class variables are those common to all the bots. This speeds up the process.
class crawler:
	directory_name = ''
	base_url = ''
	queue_file = ''
	crawled_file = ''

	def __init__ (self, directory_name, base_url, headers):
		crawler.directory_name = directory_name
		crawler.base_url = base_url
		crawler.queue_file = crawler.directory_name + '/queue.txt'
		crawler.crawled_file = crawler.directory_name + '/crawled.txt'
		crawler.out_of_domain_file = crawler.directory_name + '/out_of_domain.txt'
		self.boot()
		self.crawl_page('FirstCrawler', crawler.base_url, headres)

	@staticmethod
	def boot():
		create_dir(crawler.directory_name)
		create_file(crawler.directory_name, crawler.base_url)
		crawler.queue = file_to_set(crawler.queue_file)
		crawler.crawled = file_to_set(crawler.crawled_file)
		crawler.out_of_domain = file_to_set(crawler.out_of_domain_file)

	@staticmethod
	def crawl_page(thread, page_url, headers):
		if page_url not in crawler.crawled:
			print(thread + 'crawling' + page_url)
			crawler.add_link_to_queue(crawler.gather_links(page_url, headers))
			crawler.queue.remove(page_url)
			crawler.crawled.add(page_url)
			crawler.update_file()

	@staticmethod
	def gather_links(page_url, headers):
		FindLink(crawler.base_url, page_url, headers)
		return link_in_domain()
		
	@staticmethod
	def add_links_to_queue(links):
		for url in links:
			if url in crawler.queue:
				continue
			if url in crawler.crawled:
				continue
			if crawler.base_url not in url:
				crawler.out_of_domain.add(url)
			crawler.queue.add(url)

	@staticmethod
	def update_file():
		set_to_file(crawler.queue, crawler.queue_file)
		set_to_file(crawler.crawled, crawler.crawled_file)
		set_to_file(crawler.out_of_domain, crawler.out_of_domain_file)
