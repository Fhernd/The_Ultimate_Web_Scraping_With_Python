import requests

url = 'https://httpbin.org/headers'

response = requests.get(url)

print(response.json())
