import requests
from bs4 import BeautifulSoup

class StockScraper:
    '''
    Class for scraping news of a stock
    '''
    def __init__(self, ticker: str) -> None:
        self.ticker = ticker
        self.headers = (
                        {   
                        'User-Agent':
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/90.0.4430.212 Safari/537.36',
                        'Accept-Language': 'en-US, en;q=0.5'
                        })
    
    def get_content(self, url, headers) -> BeautifulSoup:
        '''
        Gets the content (DOM) of a given url
        '''
        page = requests.get(url, headers = headers)
        return BeautifulSoup(page.text, 'html.parser')
    
    def news_urls_scraper(self):
        '''
        Scraps all the URLs of the stock
        '''
        url = 'https://finviz.com/quote.ashx?t={}&p=d'.format(self.ticker)
        soup = self.get_content(url=url, headers = self.headers)
        news_table = soup.find_all('table', {'class':'fullview-news-outer'}) 
        # (type(news_table)) <class 'bs4.element.ResultSet'>
        # (len(news_table)) 1
        news = []
        urls = []
        for new in news_table[0].find_all('tr'):
            date_ttl_str = ''
            for td in new.find_all('td')[1]:
                date_ttl_str += td.text
                date_ttl_str += ' ' # Super necessary for future regex filtering
                try:
                    urls.append(str(td.find_all('a', {'class':'tab-link-news'})[0]['href']))
                except:
                    pass
            news.append(date_ttl_str)  
        [print(i) for i in news[:10]]
        [print(i) for i in urls[:10]]
        return 0

        



i1 = StockScraper('NVDA')
i1.news_urls_scraper()

