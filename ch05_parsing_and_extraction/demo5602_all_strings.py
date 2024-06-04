from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com'
response = requests.get(url)

content = response.text

soup = BeautifulSoup(content, 'html.parser')

print()

stripped = soup.stripped_strings
all_strings = list(stripped)

print(all_strings)

print()
print()

print(len(all_strings))
print()

print(len(list(soup.strings)))
print()
