#importe a biblioteca usada para consultar uma URL
import requests

#importe as funções BeautifulSoup para analisar os dados retornados do site
from bs4 import BeautifulSoup

#especifique o URL
url = "https://ge.globo.com/futebol/brasileirao-serie-a/"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

result = soup.find('table', attrs={'class': "tabela__equipes tabela__equipes--com-borda"})

print(result)

