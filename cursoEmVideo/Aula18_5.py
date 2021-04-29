from random import randint
lista = list()
jogos = list()
quant = int(input('Quantos jogos você quer sortear ? '))
tot = 0

while tot < quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    tot += 1
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print('-=' * 3, f' Sorteando {quant} Jogos', '-=' * 3)

for i, v in enumerate(jogos):
    print(f'Jogo {i + 1}: {v}')

