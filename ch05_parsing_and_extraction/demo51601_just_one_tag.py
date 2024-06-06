import re

from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com'
response = requests.get(url)

content = response.text

soup = BeautifulSoup(content, 'html.parser')

soup.find_all('a', limit=1)
soup.find('a')
soup.find_all('a', limit=1)[0] is soup.find('a')


soup.select('a', limit=1)
soup.select_one('a')
soup.select('a', limit=1)[0] is soup.select_one('a')
