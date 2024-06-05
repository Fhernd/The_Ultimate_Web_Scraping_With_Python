from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com'
response = requests.get(url)

content = response.text

soup = BeautifulSoup(content, 'html.parser')

books = soup.find_all('article', class_='product_pod')
print('Books:', len(books))

for b in books:
    pass
