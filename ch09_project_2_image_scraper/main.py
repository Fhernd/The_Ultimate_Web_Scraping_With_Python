from datetime import datetime

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
    images = tree.css('img.post-image.entry-image')
    return images


def download_image(url):
    """
    Downloads an image from a URL.
    
    Args:
        url (str): The URL of the image to download.
    """
    response = get(url)
    
    if response.status_code != 200:
        print(f"Failed to download the image: {response.status_code}")
        return
    
    filename = url.split('/')[-1]
    
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    
    with open(f"images/{date_time}/{filename}", 'wb') as file:
        file.write(response.content)


def main():
    url = 'https://thegraphicsfairy.com/?s=computer'
    try:
        html = fetch_page(url)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return

    tree = parse_html(html)
    
    images = extract_images(tree)
    
    print("Number of images found:", len(images))
    
    print()
    
    for image in images:
        download_image(image.attributes['src'])
    
    print("Images downloaded successfully.")


if __name__ == "__main__":
    main()
