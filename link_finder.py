from html.parser import HTMLParser
from urllib import parse
from bs4 import BeautifulSoup
import re
from urllib.parse import urlsplit

class internals():

    def __init__(self, html,base,status,page_url,data_file):
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

    def meta_data(self,html,base,status,page_url,data_file):
        self.url = page_url
        self.base = base
        soup = BeautifulSoup(html, 'html.parser')
        self.status_code = status
        self.meta_title = soup.title.text
        self.title_length = len(self.meta_title)
        meta_description = soup.find('meta', attrs={'name': 'description'})
        self.meta_description = meta_description['content']
        self.meta_description_length = len(self.meta_description)
        with open(data_file, 'a') as file:
            file.write('{},{},{}\n'.format(self.url,self.meta_title, self.status_code))
        return self.meta_title,self.status_code

