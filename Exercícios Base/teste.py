import requests
from bs4 import BeautifulSoup

url = 'https://www.instagram.com/engenharia_deprod/'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for post in html.select('.eo2As '):
    titulo = post.select_one('.Jv7Aj  MqpiF  ')
    print(titulo.text)
