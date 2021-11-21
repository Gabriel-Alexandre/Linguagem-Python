#importe a biblioteca usada para consultar uma URL
import requests

#importe as funções BeautifulSoup para analisar os dados retornados do site
from bs4 import BeautifulSoup

#especifique o URL
url = "https://www.python.org/"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

result = soup.find_all('div', attrs={'class': "small-widget"})

for v in result:
    print(v.h2.text)

