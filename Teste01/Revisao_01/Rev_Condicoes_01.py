from random import randint

numero = int(input('Digite um numero entre 1 e 5: '))
escolha = randint(1, 5)

if numero == escolha:
    print('Você escolheu o número certo!')
elif numero > 5:
    print('Erro! Digite um número válido!')
else:
    print('Você não escolheu o número certo!')
