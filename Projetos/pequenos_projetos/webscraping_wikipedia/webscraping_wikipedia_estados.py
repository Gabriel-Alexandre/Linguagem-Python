#importe a biblioteca usada para consultar uma URL
import urllib.request

#importe as funções BeautifulSoup para analisar os dados retornados do site
from bs4 import BeautifulSoup

#especifique o URL
wiki = "https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil"

#Consulte o site e retorne o html para a variável 'page'
page = urllib.request.urlopen(wiki)

#Passe o html na variável 'page' e armazene-o no formato BeautifulSoup
soup = BeautifulSoup(page, 'html5lib')

#Insira a tag <li> e adicione sua classe
for c in range(6, 33):
    list_item = soup.find('li', attrs={'class': f'toclevel-2 tocsection-{c}'})

    #Separe o HTML do texto com o código abaixo
    name = list_item.text[4:].strip()
    print(name)