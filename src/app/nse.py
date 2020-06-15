import requests
import json
import logging

logger = logging.getLogger(__name__)


class NSELiveAPI:

    API_BASE_URL = 'https://www.nseindia.com/api/'
    API_QUOTE = 'quote-equity?symbol='
    API_SECTION = '&section=trade_info'
    API_DIRECT_QUOTE = 'https://www.nseindia.com/get-quotes/equity?symbol='

    API_HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'authority': 'www.nseindia.com',
        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }

    def __init__(self, symbol):
        self.symbol = symbol

    def get_section_request_url(self):
        return  self.get_quote_url() + self.API_SECTION

    def get_quote_url(self):
        return self.API_BASE_URL + self.API_QUOTE + self.symbol
    
    def get_stock_trade_info(self):
        try:
            url = self.get_section_request_url()
            logger.info('GET Request : ' + str(url))
            response = requests.get(url=url, headers=self.API_HEADERS)
            if response.status_code == 200:
                return json.loads(response.content)
            else:
                return None
        except Exception as e:
            return None
        
    def get_live_data(self):
        try:
            url = self.get_quote_url()
            logger.info('GET Request : ' + str(url))
            response = requests.get(url=url, headers=self.API_HEADERS)
            if response.status_code == 200:
                return json.loads(response.content)
            else:
                return None
        except Exception as e:
            return None

    def get_order_book(self):
        data = self.get_stock_trade_info()
        if data and data.get('marketDeptOrderBook'):
            return data.get('marketDeptOrderBook')
        else:
            return {}

    def get_direct_link(self):
        return self.API_DIRECT_QUOTE + self.symbol