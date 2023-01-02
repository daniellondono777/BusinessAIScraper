import re
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
import pandas as pd
import numpy as np


arr = ['Dec-31-22 07:00AM', '06:45AM', '06:00AM', '05:10AM', 'Dec-30-22 05:45PM', '03:41PM', '01:30PM', '09:45AM', '06:45AM', 'Dec-29-22 07:56PM', '08:00AM', 'Dec-28-22 04:36PM', '02:10PM', '09:00AM', '08:19AM', '07:47AM', '07:15AM', '06:47AM', '06:45AM', '05:52AM', 'Dec-27-22 10:44PM', '10:08PM', '05:01PM', '09:26AM', '08:20AM', '07:01AM', '06:00AM', '05:36AM', '05:35AM', '05:06AM', 'Dec-26-22 07:26PM', '02:42PM', '12:48PM', '08:23AM', '06:00AM', '05:31AM', 'Dec-25-22 11:17AM', '08:10AM', 'Dec-24-22 12:28PM', '10:10AM', '08:15AM', 'Dec-23-22 05:45PM', '04:07PM', '03:56PM', '02:46PM', '09:53AM', '08:23AM', '07:20AM', '06:30AM', '06:00AM', '05:59AM', '05:21AM', 'Dec-22-22 04:00PM', '02:01PM', '12:45PM', '11:33AM', '09:42AM', '08:10AM', '07:07AM', '06:02AM', '05:56AM', 'Dec-21-22 09:46PM', '09:24PM', '03:02PM', '02:51PM', '01:15PM', '10:40AM', '10:29AM', 'Dec-20-22 08:20AM', '07:30AM', '07:20AM', '07:00AM', 'Dec-19-22 07:21PM', '01:32PM', '10:19AM', '10:13AM', '10:06AM', '09:01AM', '08:22AM', '08:17AM', '06:19AM', '06:00AM', 'Dec-18-22 11:03PM', '02:09PM', '09:21AM', '09:13AM', '08:11AM', '07:00AM', '06:10AM', 'Dec-17-22 06:40AM', '05:09AM', 'Dec-16-22 04:37PM', '04:27PM', '01:16PM', '11:30AM', '10:49AM', '09:00AM', '08:21AM', '06:30AM', '05:51AM']
pattern_news_content = '\d\d:\d\d(AM|PM)\s.*'
pattern_date = '(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-\d\d-\d\d\s\d\d:\d\d(AM|PM)'

headers = ({   
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/90.0.4430.212 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'
            })


def get_content(url, headers) -> BeautifulSoup:
        '''
        Gets the content (DOM) of a given url
        '''
        page = requests.get(url, headers = headers)
        return BeautifulSoup(page.text, 'html.parser')

def text_fetch(url) -> list:
        '''
        Returns the text in an array of sentences 
        '''
        soup = get_content(url=url, headers=headers)
        content = []
        if 'finance.yahoo.com' in url: # Only edge case for now. 
            ref_url = soup.find_all('a',{'class':'link caas-button'})[0]['href']
            soup2 = get_content(url=ref_url, headers=headers)
            for p in soup2.find_all('p'):
                content.append(p.text)
        else:
            for p in soup.find_all('p'):
                # TODO: Implement pos, neu, and neg arrays for better understanding in the return of asset_scraper.py
                # content.append(p.text)
                content.append(p.text) 
        return content

def polarity_score(article_array):
    sid_obj = SentimentIntensityAnalyzer()
    scores = []
    for sentence in article_array:
        scores.append(sid_obj.polarity_scores(sentence))
    return pd.DataFrame(scores).describe()
        

arr = text_fetch('https://finance.yahoo.com/m/4dae6613-e054-389c-98b0-9b568c1b98fb/3-top-ai-stocks-ready-for-a.html')
print(polarity_score(arr))
# print(text_fetch('https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-nasdaq-breaks-key-level-apple-dives-here-is-the-silver-lining/?src=A00220'))