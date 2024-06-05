import re

from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com'
response = requests.get(url)

content = response.text

soup = BeautifulSoup(content, 'html.parser')

books = soup.find_all('article', class_='product_pod')
print('Books:', len(books))

data = []

stars = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}

pattern = r'\d+\.\d+'

for b in books:
    book = {}

    book['title'] = b.find('h3').find('a').get_text()

    rating = b.find('p', class_='star-rating')
    book['rating'] = stars[rating.attrs['class'][1]]

    price = b.find('p', class_='price_color')
    price = price.get_text()
    price = re.search(pattern, price)
    book['price'] = float(price.group())

    data.append(book)

print()

for d in data:
    print(d)
