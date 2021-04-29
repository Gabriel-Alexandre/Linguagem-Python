num = soma = cont = 0

while num != -1:
    num = int(input('Digite um número: '))
    if num != -1:
        soma += num
        cont += 1
print('Você digitou {} números!'.format(cont))
print('A soma entre eles vale {}!'.format(soma))
