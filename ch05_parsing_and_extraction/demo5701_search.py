from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com'
response = requests.get(url)

content = response.text

soup = BeautifulSoup(content, 'html.parser')

all_elements = soup.find_all()
print(len(all_elements))

print()

links = soup.find_all('a')
print('Links:', len(links))

print()

links_paras = soup.find_all(['a', 'p'])
print('Links and paragraphs:', len(links_paras))

print()

prices = soup.find_all('p', attrs={'class': 'price_color'})
print('Prices:', len(prices))

print()

prices = [price.get_text() for price in prices]
print('Prices:')
print(prices)
print('Total:', len(prices))

print()

prices = soup.find_all('p', class_='price_color')
print('Prices:', len(prices))

print()

add_buttons = soup.find_all('a', attrs={
    'add-loading-text': lambda x: 'add' in x.lower() or 'remove' in x.lower()
})
print('Add buttons:', len(add_buttons))
