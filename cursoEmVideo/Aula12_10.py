from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
(0) Pedra
(1) Papel
(2) Tesoura''')

jogada = int(input('Qual sua jogada: '))

if jogada > 2 or jogada < 0:
    print('Jogada inválida!')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    sleep(1)

    print('-=' * 11)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogada]))
    print('-=' * 11)

    if computador == 0:
        if jogada == 0:
            print('EMPATE!')
        elif jogada == 1:
            print('JOGADOR Venceu!')
        elif jogada == 2:
            print('COMPUTADOR Venceu!')
        else:
            print('Jogada INVÁLIDA!')
    elif computador == 1:
        if jogada == 0:
            print('COMPUTADOR Venceu!')
        elif jogada == 1:
            print('EMPATE!')
        elif jogada == 2:
            print('JOGADOR Venceu!')
        else:
            print('Jogada INVÁLIDA!')
    elif computador == 2:
        if jogada == 0:
            print('JOGADOR Venceu!')
        elif jogada == 1:
            print('COMPUTADOR Venceu!')
        elif jogada == 2:
            print('EMPATE!')
        else:
            print('Jogada INVÁLIDA!')
