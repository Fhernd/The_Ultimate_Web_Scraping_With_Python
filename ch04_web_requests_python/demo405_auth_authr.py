import requests

url = 'https://httpbin.org/basic-auth/user/passwd'

response = requests.get(url, auth=('user', 'passwd'))

print(response.json())
