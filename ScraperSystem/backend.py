import json
from flask import Flask, render_template, request
from asset_scraper import StockScraper

app = Flask("Security Sentiment Analysis")

@app.route('/stock_scrap')
def scraper_endpoint():
    '''
    (200) Returns in a JSON the requested information
    '''
    try:
        asset = request.get_json()['stock_ticker']
        scraper = StockScraper(asset)
        return scraper.json_informational_df()
    except:
        # Unhandled error
        return 0 

if __name__ == '__main__':
    app.run()