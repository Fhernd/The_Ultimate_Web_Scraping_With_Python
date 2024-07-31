import time
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
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    session = requests.Session()
    response = session.get(url, headers=headers)
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
    images = tree.css('img[loading="lazy"][sizes][srcset]')
    return images

def main():
    url = 'https://unsplash.com/s/photos/Galaxy'
    try:
        html = fetch_page(url)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return

    tree = parse_html(html)
    
    images = extract_images(tree)
    
    print("Number of images found:", len(images))
    for img in images:
        src = img.attributes.get('src')
        if src:
            print(f"Image src: {src}")
        for attr, value in img.attributes.items():
            print(f"{attr}: {value}")
        print("-" * 20)
        time.sleep(1)  # Wait 1 second between processing each image

if __name__ == "__main__":
    main()
