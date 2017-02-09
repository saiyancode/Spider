import requests
from bs4 import BeautifulSoup
import datetime
from time import sleep, strftime,gmtime
from random import choice, randint
import re
from urllib.parse import urlsplit

urls = ['https://www.tes.com/teaching-resources']

user_agent_list = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36']


def current_time():
    time_now = strftime('%H:%M:%S', gmtime())
    return time_now

def current_time_date():
    time = datetime.date.today()
    return time

def random_user_agent():
    UserAgent = choice(user_agent_list)
    UserAgent = {'User-Agent': UserAgent}
    return UserAgent

class Status:

    def __init__(self,i):
        self.url = i
        self.status_code = requests.get(i).status_code
        self.time = requests.get(i).elapsed.total_seconds()


class Meta:

    def __init__(self,soup):
        self.url = i
        self.status_code = requests.get(i).status_code
        self.meta_title = soup.title.text
        self.title_length = len(self.meta_title)
        meta_description = soup.find('meta',attrs={'name':'description'})
        self.meta_description = meta_description['content']
        self.meta_description_length = len(self.meta_description)
        self.time = requests.get(i).elapsed.total_seconds()

class Chains:

    def __init__(self,i):
        response = requests.get(i)
        history = response.history
        self.url = i
        self.number_of_redirects = len(history)
        try:
            self.redirect_1_url = history[0].url
            self.redirect_1_response = history[0].status_code
            self.redirect_2_url = history[1].url
            self.redirect_2_response = history[1].status_code
            self.redirect_3_url = history[2].url
            self.redirect_3_response = history[2].status_code
        except:
            pass

# Google Rankings Script
#c = GoogleRanking(keyword,country,base_url,query)
#d = c.__dict__['results']
#d = GoogleRanking.client_ranking()

#print(len(d))

        # date = dictionary['time']
		# day = dictionary['day']
		# keyword = dictionary['keyword']
		# rank = dictionary['rank']
		# url = dictionary['url']
		# title = dictionary['title']
		# title_length = dictionary['title_length']
		# description = dictionary['description']
		# description_length = dictionary['description_length']
		# domain = dictionary['domain']


#print(c.__dict__['results'])