import requests
from bs4 import BeautifulSoup as BS

url = 'https://rp5.am/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%95%D1%80%D0%B5%D0%B2%D0%B0%D0%BD%D0%B5'
class_name = 't_0'

r = requests.get(url)
html = BS(r.text, 'html.parser')
t = html.find(class_ = class_name).text

print('Погода в Ереване ->  ' + t)