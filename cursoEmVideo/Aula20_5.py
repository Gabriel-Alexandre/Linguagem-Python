from random import randint

def sortear(lista):
    print('Sorteando 5 valores: ', end='')
    for c in range(0, 5):
        lista.append(randint(0, 9))
    for valor in lista:
        print(f'{valor}', end=' ')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares de {lista}, temos {soma}')


#Programa Principal

l = []

sortear(l)
somaPar(l)
