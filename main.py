import threading
from queue import Queue
from crawler import crawler
from file_manage import *
# from cli1 import *

DIRECTORY_NAME = "cyberlabs"
HOME_PAGE = "http://cyberlabs.club"
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 2

queue = Queue()
crawler(DIRECTORY_NAME, HOME_PAGE)

def create_bot():
	for _ in range(NUMBER_OF_THREADS):
		thread = threading.Thread(target = task)
		thread.daemon = True
		thread.start()

def task():
	while True:
		url = queue.get()
		crawler.crawl_page(threading.current_thread().name, url, headers)
		queue.task_done()

def assign():
	for link in file_to_set(QUEUE_FILE):
		queue.put(link)
	queue.join()
	crawl()

def crawl():
	queue_links = file_to_set(QUEUE_FILE)
	if len(queue_links) > 0:
		assign()

create_bot()
crawl()

