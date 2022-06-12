from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

class BusinessArticleScraper:
    def __init__(self, stock_code):
        self.stock_code = stock_code

    def scrapAvailableURLS(self):
        news_tables = {}

        company_url = 'https://finviz.com/quote.ashx?t={symbol}'
        url = company_url.format(symbol=self.stock_code)
        request = Request(url = url, headers={'user-agent':'my-app'})
        # Respuesta de la url de FINVIZ
        response = urlopen(request)
        
        html_object = BeautifulSoup(response, 'html')
        news_table = html_object.find(id='news-table')
        news_tables[self.stock_code] = news_table

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
        return scraped_urls


    def scrapArticleWebSite(self, article_url):
        # Create request to the article
        # It receives a url 
        request = Request(url=article_url)
        
        try:
            response = urlopen(request)


            #BeautifulSoup Object
            html_object = BeautifulSoup(response, 'html')

            ## paragraphs = html_object.findAll('p')
            # Extract the info 
            content = []
            for tag in html_object.findAll('p'):
                content.append(tag.text)

            # for i in content:
            #     print(i)
            #     print('----------------')
            return content # Returns a list of texts used in the article

        except:
            pass
    
    def scrapMultipleArticles(self, depth):
        # Articles URL's
        articles_urls = self.scrapAvailableURLS()

        # List of articles (i.e articles are lists of paragraphs)
        definite_articles = []

        # limit to search for articles 
        limit = depth*1
        
        for i in articles_urls:
            if limit > 0:
                
                if self.scrapArticleWebSite(i) is not None:
                    definite_articles.append([i, self.scrapArticleWebSite(i)] )
                    # print(( type(self.scrapArticleWebSite(i)) ))
                    # print('')
                    # print('----------------------------------------------')
                    limit = limit - 1
                else:
                    limit = limit + 0
        return definite_articles
                        

# hola = BusinessArticleScraper('NVDA')
# print(hola.scrapMultipleArticles(depth = 4))

