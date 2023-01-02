import requests
from bs4 import BeautifulSoup
import pandas as pd

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
    
    def date_formatting(self, arr) -> list:
        '''
        Helper function to format all the dates
        '''
        ret = []
        actual_date = arr[0].split(' ')[0]
        for i in range(0, len(arr)):
            actual = arr[i].split(' ')
            if len(actual) == 2:
                if actual[0] != actual_date:
                    actual_date = actual[0]
                    ret.append(actual_date + ' ' + actual[1])
                else:
                    ret.append(actual_date + ' ' + actual[1])
            if len(actual) == 1:
                ret.append(actual_date + ' ' +actual[0])
        return ret
    
    def news_urls_scraper(self): # -> pd.DataFrame:
        '''
        Scraps all the URLs of the stock, its title and its date. Returns a Dataframe with this info
        '''
        url = 'https://finviz.com/quote.ashx?t={}&p=d'.format(self.ticker)
        soup = self.get_content(url=url, headers = self.headers)
        news_table = soup.find_all('table', {'class':'fullview-news-outer'})[0]
        # (type(news_table)) <class 'bs4.element.ResultSet'>
        # (len(news_table)) 1
        
        url = []
        title = []
        date = []

        for el in news_table.find_all('a', {'class':'tab-link-news'}):
            url.append(el['href'])
            title.append(el.text)
        for el in news_table.find_all('td', {'align':'right'}):
            date.append(el.text)
        date = self.date_formatting(date)

        df = pd.DataFrame()
        df['title'] = title
        df['url'] = url
        df['date'] = date

        for i in df['url'].to_numpy():
            print(i)

    def text_evaluator(self, url) -> float:
        '''
        Returns the polarity score of a given article. 
        '''
        pass


        

        



i1 = StockScraper('NVDA')
print(i1.news_urls_scraper())

