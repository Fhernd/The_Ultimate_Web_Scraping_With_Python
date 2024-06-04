from bs4 import BeautifulSoup
from bs4.element import NavigableString
import requests


def remove_non_navitable_strins(element):
    """
    Remove all elements that are not NavigableString

    :param element: BeautifulSoup element

    :return: list of NavigableString elements
    """
    return list(filter(lambda x: isinstance(x, NavigableString), element.children))


url = 'https://books.toscrape.com'
response = requests.get(url)

content = response.text

soup = BeautifulSoup(content, 'html.parser')

children = list(soup.ul.children)

for child in children:
    print(child.name)
