from random import randint

num = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))

print(f'Números sorteados: {num}')

'''cont = 0

for n in range(0, 5):
    cont += 1

    if cont == 1:
        maior = num[n]
        menor = num[n]

    if num[n] > maior:
        maior = num[n]
    elif num[n] < menor:
        menor = num[n]

print(f'O maior valor foi: {maior}')
print(f'O menor valor foi: {menor}')'''

print(f'O maior valor foi: {max(num)}')
print(f'O menor valor foi: {min(num)}')
