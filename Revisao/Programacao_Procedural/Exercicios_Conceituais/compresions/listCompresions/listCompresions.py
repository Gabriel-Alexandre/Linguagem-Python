l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# [(O que vou fazer com cade item da lista) for (variável que representa cada item da lista) in (lista)]
l2 = [v*2 for v in l1]
# Raciocínio semelhante ao for acima
# Esse modelo funciona de maneira semelhante a um for dentre de outro
# É executado 1 vez o primeiro for, depois o segundo for realiza todas suas execuções
# Isso pode acontecer tanto para uma lista quanto para um range, já que ele retorna uma tupla
l3 = [(v, v2) for v in range(2) for v2 in range(3)]
# Quando o if não tem else ele é colocado no final
l4 = [v for v in l1 if v % 2 == 0 if v % 3 == 0]
# Quando o if tem else ele é colocado no Início
# Assim sendo, ele recebe v se for par, e 0 caso contrário
l4 = [v if v % 2 == 0 else 0 for v in l1]

print(l2)
print(l3)
print(l4)

