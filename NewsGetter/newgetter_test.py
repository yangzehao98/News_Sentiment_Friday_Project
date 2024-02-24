from typing import List, Optional
import requests

PUBLIC_KEY = 'PKA6TNIEWKQ5E2PLEI7Q'
PRIVATE_KEY = 'UFefPAIEx6Y1omgv4ymBUN6tGLnbzcVL2Jm5gARZ'

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


next_page_token = "MTY5ODA3MjMyODAwMDAwMDAwMHwzNTM3NTY1Mw=="
alpaca_news_api = AlpacaNewsAPI(PUBLIC_KEY, PRIVATE_KEY)
news = alpaca_news_api.get_news(symbols='COKE', next_token=next_page_token)
print(news.keys())