cont = soma = 0

while True:
    num = int(input('Digite um valor: '))
    if num == -1:
        break
    soma += num
    cont += 1

print(f'Você digitou {cont} números!')
print(f'A soma entre eles vale: {soma}')

