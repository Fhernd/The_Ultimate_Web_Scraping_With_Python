import requests
from httpx import get
from selectolax.parser import HTMLParser

def fetch_page(url):
    """
    Fetches the HTML content of a page.
    
    Args:
        url (str): The URL of the page to fetch.
    
    Returns:
        str: The HTML content of the page.
    """
    response = get(url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the page: {response.status_code}")
    
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
    images = tree.css('img.spacing_noMargin__F5u9R.MediaCard_image__yVXRE')
    return images

def main():
    url = 'https://www.pexels.com/search/Galaxy/'
    try:
        html = fetch_page(url)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return

    print(html)
    tree = parse_html(html)
    
    images = extract_images(tree)
    
    print("Number of images found:", len(images))


if __name__ == "__main__":
    main()
