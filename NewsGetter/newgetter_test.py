from typing import List, Optional
import requests

PUBLIC_KEY = 'PKA6TNIEWKQ5E2PLEI7Q'
PRIVATE_KEY = 'UFefPAIEx6Y1omgv4ymBUN6tGLnbzcVL2Jm5gARZ'


class AlpacaNewsAPI:
    def __init__(self, api_key_id: str, api_secret_key: str, symbols: List[str]):
        self.base_url = 'https://data.alpaca.markets/v1beta1/news'
        self.api_key_id = api_key_id
        self.api_secret_key = api_secret_key
        self.headers = {
            'Apca-Api-Key-Id': self.api_key_id,
            'Apca-Api-Secret-Key': self.api_secret_key,
            'symbols': 'COKE'
        }

    def get_news(self, next_page_token: Optional[str] = None):
        if next_page_token:
            self.headers['next_page_token'] = next_page_token
        response = requests.get(self.base_url, headers=self.headers)
        return response.json()


# Usage example:
alpaca_news_api = AlpacaNewsAPI(api_key_id=PUBLIC_KEY, api_secret_key=PRIVATE_KEY, symbols=['COKE'])
news = alpaca_news_api.get_news()

print(news)