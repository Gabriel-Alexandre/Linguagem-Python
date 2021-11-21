#importe a biblioteca usada para consultar uma URL
import requests

#importe as funções BeautifulSoup para analisar os dados retornados do site
from bs4 import BeautifulSoup

#especifique o URL
url = "https://g1.globo.com/"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

result = soup.find_all('div', attrs={'class': "feed-post-body"})

for v in result:    
    # print(v.prettify())

    titulo = v.find('a', attrs={'class': "feed-post-link"}).text
    print(f"Titulo: {titulo}")

