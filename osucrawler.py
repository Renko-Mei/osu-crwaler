import requests
from general import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from html.parser import HTMLParser
from urllib import parse

class ContentFinder(HTMLParser):
    # Initializer
    def __init__(self, userID):
        super().__init__()
        self.userID = userID
        self.content = {'ID': userID, 'Name': '', 'Country': '', 'Rank': '', 'SS count': ''}
        self.data = ''
    
    # Overwrite built in method
    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            for (name, value) in attrs:
                if (name == 'data-turbolinks-eval')
                break
        else:
            return
    
    def handle_data(self, data):
        self.data = data
    
    # Output method
    def output(self):


class OsuSpider:
    # Class variables shared among all instances
    project_name = "osu! SS list"
    base_url = "https://osu.ppy.sh"
    # Text files
    queue_file = ''
    crawled_file = ''
    file_name = "SS_list.txt"
    # variables
    queue = set() 
    crawled = set()

    # Initializer
    def __init__(self, project_name, base_url, file_name):
        OsuSpider.project_name = project_name
        OsuSpider.base_url = base_url
        OsuSpider.file_name = file_name
        OsuSpider.queue_file = OsuSpider.project_name + "/queue.txt"
        OsuSpider.crawled_file = OsuSpider.project_name + "/crawled.txt"
        self.boot()
        self.crawl_page("First spider", OsuSpider.base_url)
    
    # Creates directory and files for project on first run and starts the spider
    @staticmethod
    def boot():
        create_project_dir(OsuSpider.project_name)
        create_data_files(OsuSpider.project_name, OsuSpider.base_url)
        OsuSpider.queue = file_to_set(OsuSpider.queue_file)
        OsuSpider.crawled = file_to_set(OsuSpider.crawled_file)

     # Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in OsuSpider.crawled:
            print(thread_name + " is crawling " + page_url)
            print("In queue: " + str(len(OsuSpider.queue)) + " | Pages cralwed: " + str(len(OsuSpider.crawled)))
            OsuSpider.add_links_to_queue