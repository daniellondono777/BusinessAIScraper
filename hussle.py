import pandas as pd
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import megaScraper
import scraper

class Hussle:

    def __init__(self, stock_code, depth):
        self.stock_code = stock_code
        self.depth = depth
    
    def hussle(self):
        # Article Scrapper object
        article_scraper_object = megaScraper.BusinessArticleScraper(self.stock_code)

        # Title Scrapper object
        title_scraper_object = scraper.BusinessScraper(self.stock_code)

        # Merge both generated dataframes (INNER JOIN) on the url field
        
        # Numpy Array of URL and content
        url_and_content = np.array(article_scraper_object.scrapMultipleArticles( self.depth ))
        
        # Numpy Array of URL and [stock_code, date, time, title]
        url_and_co_info = np.array(title_scraper_object.scrapCompanyProfile())
        
        # For each numpy array, create a Pandas DataFrame
        
        # url_and_content DataFrame 
        df_uac = pd.DataFrame(data=url_and_content, columns = ['URL','CONTENT'])
        
        # url_and_co_info DataFrame
        df_uaci = pd.DataFrame(data=url_and_co_info, columns = ['URL','NN'])
        
        
        # Merge each Pandas DataFrame, on the URL field
        df_merge = df_uaci.merge(df_uac, how = 'inner', on = 'URL')
        
        # VADER Thing
        
        def aux(article): # For the average polarity score
            vader = SentimentIntensityAnalyzer()
            total = 0
            for i in article:
                total += vader.polarity_scores(i).get('compound')
            return (total/len(article))
        
        def aux2(article): # For the highest polarity score found
            vader = SentimentIntensityAnalyzer()
            puntajes = []
            for i in article:
                puntajes.append(vader.polarity_scores(i).get('compound'))
            ret = np.array(puntajes)
            return np.max(ret)
        
        # For every article, calculate the average VADER score
        df_merge['Average Polarity Score'] = df_merge['CONTENT'].apply(aux)
        
        # For every article, calculate the highest VADER score
        df_merge['Highest Polarity Score'] = df_merge['CONTENT'].apply(aux2)
        
        df_merge = df_merge[['NN','CONTENT','Average Polarity Score','Highest Polarity Score','URL']]
        

        # Create Dataframe containing
        # stockCode | Article title | VADER Score | Space for something useful (Interesting words might be) | URL of the article

        urls_list = []
        for url in df_merge['URL'].to_numpy():
            urls_list.append((url)) 

        return df_merge, urls_list






# hola3 = Hussle('TSLA',7)
# print(hola3.hussle()) 
