import re

from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com'
response = requests.get(url)

content = response.text

soup = BeautifulSoup(content, 'html.parser')

print()

soup.find_all(text='Fiction')

soup.find_all(text=re.compile('Fiction', re.IGNORECASE))

all_text = list(soup.stripped_strings)
result = [text for text in all_text if 'fiction' in text.lower()]

soup.finda_all('a', text=re.compile('fiction', re.IGNORECASE))

all_text = list(soup.strings)
result = [text.parent for text in all_text if 'fiction' in text.lower() and text.parent.name == 'a']
