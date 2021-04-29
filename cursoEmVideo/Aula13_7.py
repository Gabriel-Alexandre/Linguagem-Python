soma = 0

num = int(input('Digite um número: '))

for cont in range(1, num + 1):
    if num % cont == 0:
        soma += 1

if soma == 2:
    print('{} possui {} divisores'.format(num, soma))
    print('{} É PRIMO!'.format(num))
else:
    print('{} possui {} divisores'.format(num, soma))
    print('{} NÂO É PRIMO!'.format(num))
