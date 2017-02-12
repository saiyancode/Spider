import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'testsdd'
HOMEPAGE = 'http://www.theluxetravel.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
DATA_FILE = PROJECT_NAME + '/data.csv'
CUSTOM = PROJECT_NAME + '/custom.csv'
SPIDER_TYPE = 'crawl'
NUMBER_OF_THREADS = 4
queue = Queue()

#List or crawl queue
if SPIDER_TYPE == 'crawl':
    QUEUE_FILE = PROJECT_NAME + '/queue.txt'
else:
    QUEUE_FILE = 'urls.txt'

Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME, SPIDER_TYPE,QUEUE_FILE)

# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    print(len(queued_links))
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()



create_workers()
crawl()
