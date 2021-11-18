# São usados para unir objetos iteráveis

"""
Zip - Unindo iteráveis (Vai até a menor estrutura)
Zip_longest - Itertools (Vai até a maior estrutura, o que tiver a mais e não tiver na outra estrutura ele completa com None, ou
com o valor que for indicador no parâmetro "fillvalue")
"""
from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
estados = ['SP', 'MG', 'BA']

cidades_estados1 = zip(
    indice,
    estados,
    cidades
)

for indice, estado, cidade in cidades_estados1:
    print(indice, estado, cidade)

# Não usar zip_longest com count (Pois, como count é um gerador eu poderia gerar um loop infinito)
cidades_estados2 = zip_longest(
    cidades,
    estados,
    fillvalue='Estado'
)

print(list(cidades_estados2))
