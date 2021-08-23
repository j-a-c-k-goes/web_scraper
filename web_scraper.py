"""
urllib is a module of fucntions and classes which help in opening URLs
basic and digest authentication, redirections, cookies, etc.
"""
import urllib.request

"""
beautiful soup is python library for pulling data out of HTML and XML files
"""
from bs4 import BeautifulSoup
import ssl

class Scraper:
    def __init__(self, site):
        self.site = site
    def scrape(self):
        context = ssl._create_unverified_context()
        r = urllib.request.urlopen(self.site, context=context)
        html = r.read()
        parser = 'html.parser'
        sp = BeautifulSoup(html, parser)
        for i,tag in enumerate(sp.find_all("a")):
            url = tag.get('href')
            print(i,'\t',url)

if __name__ == '__main__':
    link = 'https://www.espn.com'
    scrape = Scraper(link)
    scrape.scrape()
