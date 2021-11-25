from itertools import count

contador = count(start=5, step=2)

for n in contador:
    print(n)

    if n == 15:
        break

indice = count()
l = ['Gabriel', 'Emanuel', 'Miguel', 'Alex']
lista_final = zip(indice, l)
print(list(lista_final))

    