valor = []
maior = 0
menor = 0

for p in range(0, 5):
    valor.append(int(input(f'Digite um valor para a posição {p}: ')))

    if p == 0:
        maior = valor[p]
        menor = valor[p]
    else:
        if valor[p] > maior:
            maior = valor[p]
        elif valor[p] < menor:
            menor = valor[p]


print(f'Você Digitou os valores: {valor}')
print(f'O maior valor é: {maior}')
print(f'Nas posições: ', end='')

for i, v in enumerate(valor):
    if v == maior:
        print(f'{i}...', end='')
print()

print(f'O menor valor é: {menor}')
print(f'Nas posições: ', end='')

for i, v in enumerate(valor):
    if v == menor:
        print(f'{i}... ', end='')
print()
