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


def parse_html(html):
    """
    Parses the HTML content of a page.
    
    Args:
        html (str): The HTML content of the page.
    
    Returns:
        HTMLParser: The parsed HTML content of the page.
    """
    tree = HTMLParser(html)
    return tree


def extract_images(tree):
    """
    Extracts the image URLs from the parsed HTML content of a page.
    
    Args:
        tree (HTMLParser): The parsed HTML content of the page.
    
    Returns:
        list: The image URLs extracted from the page.
    """
    container = tree.css_first('div#\\:ro\\:')
    if container:
        images = container.css('img.I7OuT.DVW3V.L1BOa')
        return images
    
    return []


def main():
    pass


if __name__ == "__main__":
    main()
