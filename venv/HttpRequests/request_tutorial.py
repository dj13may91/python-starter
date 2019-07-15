import requests

url = "https://icanhazdadjoke.com"
res = requests.get(url, headers={"Accept": "application/json"})
data = res.json()
print(data['joke'])  # as we are getting it in key value pair, we can get

print(url.__hash__())
x = 'a'
print(x.__hash__())
x = x + 'b'
print(x.__hash__())
x = x + 'a'
print(x.__hash__())
