"""
program finds every "a" tag within a website's html

    use case

            for each website on the 'html archive project', 
            use this module to find search-sepcific hyperlinks;
            then build archive of link paths from searches —
            incorporate into site experience

    future use case

            use for 'iQuery project'

    modules
    
            urllib.request
    
                module of fucntions and classes which help in opening URLs
                basic and digest authentication, redirections, cookies, etc.

            ssl
               without module, as program runs,
               makes to connection to site, 
               connection is denied/forbidden
    
    beautiful soup 
    
            python library for pulling data out of HTML and XML files
"""
# 
import urllib.request, ssl
from bs4 import BeautifulSoup
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
    link = str(input('enter a link: '))
    if '.' not in link:
        print(f'{link}\tneeds periods')
        if 'www' in link:
            link = link.replace('www', '')
            link = f'www.{link}'
            print(f'{link}\tsolved "www"')
        extensions = ['com', 'net', 'org']
        print(extensions)
        for extension in extensions:
            if extension in link:
                link = link.replace(extension, '')
                link = f'{link}.{extension}'
                print(f'{link}\tsolved "{extension}"')
    elif 'https://' not in link:
        print(f'{link}\tmissing "https://')
        adjust_link = str(input('enter "yes" to correct link: '))
        if adjust_link == "yes":
            link = f'https://{link}'
            print(f'{link}\tupdated')
    scrape = Scraper(link)
    scrape.scrape()
