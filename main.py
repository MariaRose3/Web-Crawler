import threading
from queue import Queue
from crawler import crawler
from file_manage import *
from cli1 import *

DIRECTORY_NAME = args.output()                 #"cyberlabs"
HOME_PAGE = args.url()                         #"http://cyberlabs.club"
HEADERS = {"Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
QUEUE_FILE = DIRECTORY_NAME + '/queue.txt'
CRAWLED_FILE = DIRECTORY_NAME + '/crawled.txt'
NUMBER_OF_THREADS = args.bots()

queue = Queue()
crawler(DIRECTORY_NAME, HOME_PAGE, HEADERS)

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

