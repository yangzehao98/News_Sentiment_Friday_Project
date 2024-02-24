url = 'https://www.benzinga.com/news/23/03/31277489/what-does-coca-cola-consolidateds-debt-look-like'
import requests
from bs4 import BeautifulSoup

# Fetch the content from the URL
response = requests.get(url)
content = response.content

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

print(soup)