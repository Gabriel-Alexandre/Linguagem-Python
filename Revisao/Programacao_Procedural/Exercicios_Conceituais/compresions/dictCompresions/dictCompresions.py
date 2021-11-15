# O Funcionamente é semelhante ao de listCompresions
# O que mudo é a forma de implementar, que a compressão é em um dicionario

# Geralmente é utilizado para criar dicionários, ou transformar listas em dicionários

d1 = [
    (1, 'Um'),
    (2, 'Dois'),
    (3, 'Três'),
]

d2 = {x * 2: y.upper() for x, y in d1}
print(d2)

d3 = {x: y for x, y in enumerate(range(5))}
print(d3)
