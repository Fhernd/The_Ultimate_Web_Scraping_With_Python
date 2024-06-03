import requests as r

url = 'https://httpbin.org/delete'

response = r.delete(url)

print(response.json())
