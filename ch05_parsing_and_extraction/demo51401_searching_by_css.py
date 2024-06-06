import re

from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com'
response = requests.get(url)

content = response.text

soup = BeautifulSoup(content, 'html.parser')

title_tags = soup.select('article.product > h3 > a')
titles = [tag.get_text() for tag in title_tags]

soup.select('[title*=Human]')

soup.select('button.btn-primary[data-loading-text][class*=primary]')
