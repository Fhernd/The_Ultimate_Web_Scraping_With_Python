import requests

url = 'https://quotes.toscrape.com'

response = requests.get(url)
content = response.text
print(content)

print()

print(response.headers)
