import requests
from bs4 import BeautifulSoup
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np

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
    
    def text_fetch(self, url) -> list:
        '''
        Returns the text in an array of sentences 
        '''
        soup = self.get_content(url=url, headers= self.headers)
        content = []
        # print(url)
        if 'finance.yahoo.com' in url:
            try:
                ref_url = soup.find_all('a',{'class':'link caas-button'})[0]['href']
                soup2 = self.get_content(url=ref_url, headers=self.headers)
                for p in soup2.find_all('p'):
                    content.append(p.text)
            except:
                pass
            try:
                for p in soup.find_all('p'):
                    content.append(p.text)
            except:
                pass
        else:
            for p in soup.find_all('p'):
                content.append(p.text) 
        # print('pasa')
        # print('***')
        return content
    
    def polarity_score(self, article_array, sid_obj) -> list:
        '''
        Returns the polarity score of an article
        '''
        # sid_obj = SentimentIntensityAnalyzer() Parametrizado para optimizar 
        scores = []
        for sentence in article_array:
            scores.append(float(sid_obj.polarity_scores(sentence)['compound']))
        return scores

    
    def news_urls_scraper(self): # -> pd.DataFrame:
        '''
        Scraps all the URLs of the stock, its title and its date. Returns a Dataframe with this info
        '''
        url = f"https://finviz.com/quote.ashx?t={self.ticker}&p=d" #.format(self.ticker)
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
        
        return df
    
    def percentile(self, arr, p) -> float:
        '''
        Helper function to calculate the percentile p of an array
        '''
        if p == 25:
            return np.percentile(arr, 25)
        elif p == 50:
            return np.percentile(arr, 50)
        elif p == 75:
            return np.percentile(arr, 75)
        else:
            return 0

    def informational_df(self) -> pd.DataFrame():
        '''
        Returns a Dataframe with the title, url and date of a new, alongside the 25th, 50th and 75th percentile of its respective polarity score. 
        '''
        main_df = self.news_urls_scraper()
        urls = main_df['url'].tolist()
        sa_obj = SentimentIntensityAnalyzer()
        ret = [self.polarity_score(self.text_fetch(url), sa_obj) for url in urls]
        
        try:
            p25 = [float(self.percentile(arr, 25)) for arr in ret]
            main_df['compound_25th'] = p25
        except:
            pass
        
        try:
            p50 = [float(self.percentile(arr, 50)) for arr in ret]
            main_df['compound_50th'] = p50
        except:
            pass

        try:
            p75 = [float(self.percentile(arr, 75)) for arr in ret]
            main_df['compound_75th'] = p75
        except:
            pass

        main_df['mean_polarity'] = [np.mean(arr) for arr in ret]
        main_df['mean_std'] = [np.std(arr) for arr in ret]

        return main_df

    def json_informational_df(self) -> str:
        '''
        Returns a json version of the @informational_df function
        '''
        return str(self.informational_df().to_json())
