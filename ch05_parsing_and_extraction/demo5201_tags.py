from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com'
response = requests.get(url)

content = response.text

soup = BeautifulSoup(content, 'html.parser')

print(soup.name)
print()

print(soup.title)
print(soup.h1)
print(soup.div)

print()

first_div = soup.div
print(type(first_div))
print(first_div.attrs)
print()

print(first_div.div.div.attrs)
