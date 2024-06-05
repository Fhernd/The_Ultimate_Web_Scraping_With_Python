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

    book_link = b.find('h3').find('a').attrs['href']
    book_link = f'https://books.toscrape.com/{book_link}'
    
    response = requests.get(book_link)
    content = response.text
    book_page = BeautifulSoup(content, 'html.parser')
    book_title = book_page.find('div', class_='product_main')
    book_title = book_title.find('h1').get_text()
    book['title'] = book_title

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
