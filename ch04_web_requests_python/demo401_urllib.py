from urllib.request import urlopen

url = 'https://quotes.toscrape.com'

response = urlopen(url)

content = response.read()

# Read the content as a string:
content_str = content.decode('utf-8')

print(content_str)
