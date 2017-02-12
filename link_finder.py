from html.parser import HTMLParser
from urllib import parse
from bs4 import BeautifulSoup
import re
from urllib.parse import urlsplit
import csv

class internals():

    def __init__(self, html,base,status,page_url,data_file,response_header):
        super().__init__()
        self.base_url = base
        self.html = html
        self.links = set()
        soup = BeautifulSoup(html, 'html.parser')
        print(base)
        for link in soup.find_all('a'):
            try:
                # IF absolute links are used in the page use this
                if link.attrs['href'] is not None:
                    link_base = "{0.scheme}://{0.netloc}/".format(urlsplit(link.attrs['href']))
                    if link_base == base:
                        url = link.attrs['href']
                        self.links.add(url)
                # IF relative links are used in the page use this
                    elif link_base == ':///':
                        url = link.attrs['href']
                        url = re.sub(r"^/", "", url)
                        url = base + url
                        self.links.add(url)
            except:
                continue


    def page_links(self):
        return self.links

    def meta_data(self,html,base,status,page_url,data_file,response_header):
        self.url = page_url
        self.base = base
        soup = BeautifulSoup(html, 'html.parser')
        self.status_code = status
        try:
            self.meta_title = soup.title.text
            self.title_length = len(self.meta_title)
        except:
            self.meta_title = 'N/A'
            self.title_length = 'N/A'
        try:
            meta_description = soup.find('meta', attrs={'name': 'description'})
            self.meta_description = meta_description['content']
            self.meta_description_length = len(self.meta_description)
        except:
            self.meta_description = 'N/A'
            self.meta_description_length = 'N/A'
        try:
            self.response_header = response_header
        except:
            self.response_header = 'N/A'
        try:
            canonical = soup.find('link', attrs={'rel': 'canonical'})
            canonical_count = len(soup.findAll('link', attrs={'rel': 'canonical'}))
            self.canonical = canonical['href']
            self.canonical_count = canonical_count
        except:
            self.canonical = 'N/A'
            self.canonical_count = 0
        try:
            robots = soup.find('meta', attrs={'name': 'robots'})
            self.robots = robots['content']
        except:
            self.robots = 'N/A'

        with open(data_file, 'a') as file:
            file.write('{},{},{},{},{},{},{},{},{},{}\n'.format(self.url,self.status_code,self.response_header,
            self.meta_title,self.title_length, self.meta_description,self.meta_description_length,self.canonical,self.canonical_count,
            self.robots))
        return self.meta_title,self.status_code

class externals():

    def __init__(self, html,base,status,page_url,data_file,response_header):
        super().__init__()
        self.base_url = base
        self.html = html
        self.links = set()
        soup = BeautifulSoup(html, 'html.parser')
        print(base)
        for link in soup.find_all('a'):
            try:
                # IF absolute links are used in the page use this
                if link.attrs['href'] is not None:
                    link_base = "{0.scheme}://{0.netloc}/".format(urlsplit(link.attrs['href']))
                    if link_base == ':///':
                        continue
                    elif link_base != base:
                        url = link.attrs['href']
                        self.links.add(url)
            except:
                continue


    def page_outlinks(self):
        return self.links


