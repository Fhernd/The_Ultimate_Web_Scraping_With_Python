import re

from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com'
response = requests.get(url)

content = response.text

soup = BeautifulSoup(content, 'html.parser')

soup.find_all(id='messages')

soup.find_all(attrs={'id': 'messages'})

soup.find_all(id=lambda x: x is not None)

soup.find_all(attrs={'id': lambda x: x is not None})

soup.find_all(lambda x: x is not None)


def fiction_category_anchor(tag):
    return tag.name == 'a' and 'category' in tag['href'] and 'fiction' in tag.text


soup.find_all(fiction_category_anchor)
