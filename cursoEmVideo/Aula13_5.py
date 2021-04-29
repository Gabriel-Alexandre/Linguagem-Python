soma = 0

for cont in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma += num
print('A soma dos números pares é: {}'.format(soma))