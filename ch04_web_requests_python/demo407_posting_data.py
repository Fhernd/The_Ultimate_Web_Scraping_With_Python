import requests as r

response = r.post('https://httpbin.org/post', data={'key': 'value'})

print(response.json())

print()
print()

response = r.post('https://httpbin.org/post', json={'key': 'value'})

print(response.json())
