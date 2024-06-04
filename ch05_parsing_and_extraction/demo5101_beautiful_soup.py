from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com'
response = requests.get(url)

content = response.text

soup = BeautifulSoup(content, 'html.parser')

print(type(soup))
print()

print(soup.title)
print()

print(soup.prettify())
print()

print(soup.name)
