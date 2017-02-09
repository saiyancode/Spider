from html.parser import HTMLParser
from urllib import parse
from bs4 import BeautifulSoup
import re
from urllib.parse import urlsplit

class internals():

    def __init__(self, html,base):
        super().__init__()
        self.base_url = base
        self.html = html
        self.links = set()
        soup = BeautifulSoup(html, 'html.parser')
        #print(soup)
        print(base)
        for link in soup.find_all('a'):
            if link.attrs['href'] is not None:
                if link.attrs['href'] not in links:
                    link_base = "{0.scheme}://{0.netloc}/".format(urlsplit(link.attrs['href']))
                    if link_base == base:
                        url = link.attrs['href']
                        self.links.add(url)
                        print(url)


    def page_links(self):
        return self.links
