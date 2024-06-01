import requests

url = 'https://api.coinbase.com/v2/exchange-rates?currency=BTC'

response = requests.get(url)

print(response.json())

print()
print()

url = 'https://api.coinbase.com/v2/exchange-rates'

params = {'currency': 'COP'}

response = requests.get(url, params=params)

print(response.json())
