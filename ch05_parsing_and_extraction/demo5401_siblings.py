from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com'
response = requests.get(url)

content = response.text

soup = BeautifulSoup(content, 'html.parser')

parent = soup.ul
print('Parent:')
print(parent)

print()

print('First element:')
first_element = parent.li
print(first_element)

print()

print('Next sibling:')
next_sibling = first_element.find_next_sibling()
print(next_sibling)

print()

print('Previous sibling:')
previous_sibling = next_sibling.find_previous_sibling()
print(previous_sibling)
