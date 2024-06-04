from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com'
response = requests.get(url)

content = response.text

soup = BeautifulSoup(content, 'html.parser')

print()

print(soup.a.get_text())
print()

print(soup.a.text)
print()

print(soup.a.string)
print()

print()
print()

print(type(soup.a.get_text()))
print()

print(type(soup.a.text))
print()

print(type(soup.a.string))
print()
