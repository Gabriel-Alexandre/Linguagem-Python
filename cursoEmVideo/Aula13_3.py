soma = 0
contador = 0

for cont in range(1, 501, 2):
    if cont % 3 == 0:
        contador += 1
        soma += cont
print('Valores solicitados: {}'.format(contador))
print('O resultado é: {}'.format(soma))