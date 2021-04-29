from random import randint

print('--- Jogo da Adivinhação ---\n')

computador = randint(0, 10)
acertou = False

contador = 0

while not acertou:
    jogador = int(input('Digite um número entre 0 e 10: '))
    if jogador > computador:
        print('Menos... Tente novamente!')
    if jogador < computador:
        print('Mais... Tente novamente!')
    if jogador == computador:
        acertou = True
    contador += 1
print('Acertou!')
print('Você precisou de {} tentativas!'.format(contador))
