from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

class BusinessScraper:
    def __init__(self, stock_code):
        self.stock_code = stock_code

    def scrapCompanyProfile(self):
        news_tables = {}

        company_url = 'https://finviz.com/quote.ashx?t={symbol}'
        url = company_url.format(symbol=self.stock_code)
        request = Request(url = url, headers={'user-agent':'my-app'})
        # Respuesta de la url de FINVIZ
        response = urlopen(request)
        
        html_object = BeautifulSoup(response, 'html')
        news_table = html_object.find(id='news-table')
        news_tables[self.stock_code] = news_table

        parsed_data = []
        titles_and_date = []
        for self.stock_code, news_table in news_tables.items():
            for row in news_table.findAll('tr'):
                title = row.a.text
                date_data = row.td.text.split(" ")
                if len(date_data) == 1:
                    time = date_data[0]
                else:
                    date = date_data[0]
                    time = date_data[1]

                parsed_data.append([self.stock_code,date,time,title])
        
        a_objects = []
        scraped_urls = []

        for self.stock_code, news_table in news_tables.items():
            for row in news_table.findAll('a',href= True):
                a_objects.append(row)

        for i in a_objects:
            html = str(i)
            # print(str(html))
            # print('----')
            bs = BeautifulSoup(html, features="lxml")
            elms = bs.select("a")
            for i in elms:
                #print(i.attrs["href"])
                scraped_urls.append(i.attrs["href"])
        #print(scraped_urls)

        url_plus_parsedData = []

        for i in range(0,len(parsed_data)):
            url_plus_parsedData.append([scraped_urls[i],parsed_data[i]])
            
        
        return url_plus_parsedData

