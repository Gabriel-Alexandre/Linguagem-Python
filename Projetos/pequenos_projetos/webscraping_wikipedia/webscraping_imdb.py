import requests
from bs4 import BeautifulSoup

#especifique o URL
url = "https://www.imdb.com/chart/top/"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

filmes = []

for numero, filme in enumerate(soup.select('.titleColumn')):
    json = {}
    json['classificacao'] = numero + 1
    titulo = filme.find('a').text
    json['titulo'] = titulo
    ano = filme.find('span', attrs={'class': 'secondaryInfo'}).text
    json['ano'] =  ano

    filmes.append(json)

    # print(numero+1, titulo, ano, sep='\t')

# print(filmes)

lnotas = []

for notas in soup.select('.ratingColumn'):
    try:
        nota = notas.find('strong').text
        lnotas.append(nota)
        # print(nota)
    except:
        pass

listaIMDP = zip(filmes, lnotas)
# print(list(listaIMDP))

for x, notas in listaIMDP:

    for keys, values in x.items():
        print(f'{keys} - {values}')
    print(f'Nota: {notas}')