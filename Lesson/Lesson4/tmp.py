import requests

url = 'https://www.lotto.pl'
response = requests.get(url)

print(response.content)