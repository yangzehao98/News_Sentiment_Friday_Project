import time
from typing import List, Optional
import requests
#私人API，不可以publish



import requests

class AlpacaNewsAPI:
    def __init__(self, api_key_id, api_secret_key):
        self.base_url = 'https://data.alpaca.markets/v1beta1/news?'
        self.api_key_id = api_key_id
        self.api_secret_key = api_secret_key
        self.headers = {
            'Apca-Api-Key-Id': self.api_key_id,
            'Apca-Api-Secret-Key': self.api_secret_key,
            'accept': 'application/json'
        }

    def get_news(self, symbols: str, next_token: Optional[str] = None):
        response = requests.get(self.base_url, headers=self.headers, params={'symbols': symbols,'page_token': next_token})
        full_url = response.url
        print(full_url)
        return response.json()

records = []
news_dic_list = []
current_page_token = 'START'
SYMBOL = 'COKE'
while current_page_token is not None and news_dic_list is not None:
    alpaca_news_api = AlpacaNewsAPI(PUBLIC_KEY, PRIVATE_KEY)
    if current_page_token == 'START':
        api_news_raw = alpaca_news_api.get_news(symbols=SYMBOL)
    else:
        api_news_raw = alpaca_news_api.get_news(symbols=SYMBOL, next_token=current_page_token)
    next_page_token = api_news_raw.get('next_page_token', None)
    news_dic_list = api_news_raw.get('news', None)
    current_page_token = next_page_token
    records.extend(news_dic_list)
    # sleep for 0.1 second
    time.sleep(0.1)

# save the records to a json file
import json
with open('news_records_test.json', 'w') as f:
    json.dump(records, f)

