import requests
from selectolax.parser import HTMLParser


def fetch_page(url):
    """
    Fetches the HTML content of a page.
    
    Args:
        url (str): The URL of the page to fetch.
    
    Returns:
        str: The HTML content of the page.
    """
    
    response = requests.get(url)

    response.raise_for_status()
    
    return response.text
