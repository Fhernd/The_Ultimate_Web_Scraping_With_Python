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
    # Find all image tags which have both the srcset and sizes attributes:
    images = tree.css('img[srcset][sizes]')
    
    return images


def main():
    url = 'https://unsplash.com/s/photos/Galaxy'
    html = fetch_page(url)
    tree = parse_html(html)
    
    images = extract_images(tree)
    
    print(len(images))


if __name__ == "__main__":
    main()
