'''n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2'''

'''if (media >= 7):
    print('Aprovado!')
else:
    print('Reprovado!')'''

'''print('Aprovado!' if (media >= 7) else 'Reprovado!')'''

'''import random

numero = int(input('Digite um número inteiro entre 0 e 5 (Contando com os mesmos): '))

lista = [1, 2, 3, 4, 5]

aux = random.choice(lista)

if(numero == aux):
    print('Você ganhou!')
else:
    print('Você perdeu! {}'.format(aux))'''

from random import randint
from time import sleep

numero = int(input('Digite um número inteiro entre 0 e 5 (Contando com os mesmos): '))
print('Processando...')
sleep(1)

aux = randint(0, 5)

if(numero == aux):
    print('Você ganhou!')
else:
    print('Você perdeu! {}'.format(aux))

