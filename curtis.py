import pandas as pd
import numpy as np
import json
from urllib.request import urlopen
from termcolor import colored

class Curtis:

    def __init__(self, stock_code):
        self.stock_code = stock_code

    # There are maximum 5 quarters to search
    def getCompanyQuarterReport(self, n_quarters):
        
        try:
            # URL's for the request
            url_enterprise_value = 'https://financialmodelingprep.com/api/v3/enterprise-values/{symbol}?period=quarter&limit=130&apikey=71483f6fbf6a203ce6b35a5703793008'.format(symbol = self.stock_code)
            url_company_financial_ratios = 'https://financialmodelingprep.com/api/v3/ratios/{symbol}?period=quarter&limit=140&apikey=71483f6fbf6a203ce6b35a5703793008'.format(symbol = self.stock_code)

            # Requests
            response_enterprise_value = urlopen(url_enterprise_value)
            response_cfr = urlopen(url_company_financial_ratios)

            # Raw Data
            raw_data_enterprise_value = response_enterprise_value.read().decode('utf-8')
            raw_data_cfr = response_cfr.read().decode('utf-8')

            # Actual Data
            data_enterprise_value = json.loads(raw_data_enterprise_value)
            data_crf = json.loads(raw_data_cfr)
            
            print("Report: ")
            print("")
            print(colored('[*] Enterprise Value Information \n', 'blue', attrs=['bold']))
            print(colored('-------------------- \n','blue'))
            for i in data_enterprise_value:
                print(colored('[*] Date: {}'.format(i.get('date')) + '\n', 'cyan', attrs=['bold']))
                print(colored('{}'.format(i) + '\n', 'white'))
                print(colored('-------------------- \n','blue'))
            
            print("")
            print(colored('[*] Financial Ratios \n', 'red', attrs=['bold']))
            print(colored('-------------------- \n','red'))
            for i in data_crf:
                
                print(colored('[*] Date: {}'.format(i.get('date') + '\n'), 'magenta', attrs=['bold']))
                
                
                for key in i:
                    print(colored('[+] {ticker}: '.format(ticker = key ), 'white',attrs=['bold']) + colored(('{value} \n'.format(value = i[key])), 'green'))
                
                print(colored('--------------------', 'red', attrs=['blink']))
        
        except:
            pass

    def getCompanyAnualReport(self, n_years):
        try:
            
            url_enterprise_value = 'https://financialmodelingprep.com/api/v3/enterprise-values/{symbol}?limit=40&apikey=71483f6fbf6a203ce6b35a5703793008'.format(symbol = self.stock_code)
            url_company_financial_ratios = 'https://financialmodelingprep.com/api/v3/ratios/{symbol}?limit=40&apikey=71483f6fbf6a203ce6b35a5703793008'.format(symbol = self.stock_code)

            # Requests
            response_enterprise_value = urlopen(url_enterprise_value)
            response_cfr = urlopen(url_company_financial_ratios)

            # Raw Data
            raw_data_enterprise_value = response_enterprise_value.read().decode('utf-8')
            raw_data_cfr = response_cfr.read().decode('utf-8')

            # Actual Data
            data_enterprise_value = json.loads(raw_data_enterprise_value)
            data_cfr = json.loads(raw_data_cfr)

            print("Report: ")
            print("")
            print(colored('[*] Enterprise Value Information \n', 'blue', attrs=['bold']))
            print(colored('-------------------- \n','blue'))
            for i in data_enterprise_value:
                print(colored('[*] Date: {}'.format(i.get('date')) + '\n', 'cyan', attrs=['bold']))
                print(colored('{}'.format(i) + '\n', 'white'))
                print(colored('-------------------- \n','blue'))
            
            print("")
            print(colored('[*] Financial Ratios \n', 'red', attrs=['bold']))
            print(colored('-------------------- \n','red'))
            for i in data_cfr:
                
                print(colored('[*] Date: {}'.format(i.get('date') + '\n'), 'magenta', attrs=['bold']))
                
                
                for key in i:
                    print(colored('[+] {ticker}: '.format(ticker = key ), 'white',attrs=['bold']) + colored(('{value} \n'.format(value = i[key])), 'green'))
                
                print(colored('--------------------', 'red', attrs=['blink']))
            
            
            
        except:
            pass


    def getMostActive(self):
        url = "https://financialmodelingprep.com/api/v3/actives?apikey=71483f6fbf6a203ce6b35a5703793008"
        response = urlopen(url)

        raw_data = response.read().decode('utf-8')
        data = json.loads(raw_data)

        print("Report: ")
        print("")
        print(colored('[*] Most Active Stocks \n', 'blue', attrs=['bold']))
        print(colored('-------------------- \n','blue'))
        for i in data:
            print(colored('[*] {}: '.format(i.get('companyName')), 'cyan', attrs=['bold']) + colored('{}'.format(i.get('ticker')),'cyan', attrs=['bold'] ))
            print(colored('{}'.format(i) + '\n', 'white'))
            print(colored('-------------------- \n','blue'))


    
    def getMostGainerz(self):
        url = "https://financialmodelingprep.com/api/v3/gainers?apikey=71483f6fbf6a203ce6b35a5703793008"
        response = urlopen(url)

        raw_data = response.read().decode('utf-8')
        data = json.loads(raw_data)

        print("Report: ")
        print("")
        print(colored('[*] Most Gainer Stocks \n', 'blue', attrs=['bold']))
        print(colored('-------------------- \n','blue'))
        for i in data:
            print(colored('[*] {}: '.format(i.get('companyName')), 'cyan', attrs=['bold']) + colored('{}'.format(i.get('ticker')),'cyan', attrs=['bold'] ))
            print(colored('{}'.format(i) + '\n', 'white'))
            print(colored('-------------------- \n','blue'))

    def getMostLosers(self):
        url = "https://financialmodelingprep.com/api/v3/losers?apikey=71483f6fbf6a203ce6b35a5703793008"
        response = urlopen(url)

        raw_data = response.read().decode('utf-8')
        data = json.loads(raw_data)

        print("Report: ")
        print("")
        print(colored('[*] Most Loser Stocks \n', 'blue', attrs=['bold']))
        print(colored('-------------------- \n','blue'))
        for i in data:
            print(colored('[*] {}: '.format(i.get('companyName')), 'cyan', attrs=['bold']) + colored('{}'.format(i.get('ticker')),'cyan', attrs=['bold'] ))
            print(colored('{}'.format(i) + '\n', 'white'))
            print(colored('-------------------- \n','blue'))
    
    def getHourlyMarketPerformance(self):
        url = "https://financialmodelingprep.com/api/v3/sectors-performance?apikey=71483f6fbf6a203ce6b35a5703793008"
        response = urlopen(url)

        raw_data = response.read().decode('utf-8')
        data = json.loads(raw_data)

        print("Report: ")
        print("")
        print(colored('[*] Market Performance \n', 'blue', attrs=['bold']))
        print(colored('-------------------- \n','blue'))
        for i in data:
            if float(i.get('changesPercentage').split('%')[0]) > 0:
                print(colored('[*] Sector: {}: '.format(i.get('sector')), 'green', attrs=['bold']) )
            else:
                print(colored('[*] Sector: {}: '.format(i.get('sector')), 'red', attrs=['bold']) )
            print(colored('{}'.format(i) + '\n', 'white'))
            print(colored('-------------------- \n','blue'))







        
         

# hola4 = Curtis('TSLA')
# print(hola4.getHourlyMarketPerformance())
