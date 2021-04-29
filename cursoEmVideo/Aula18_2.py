numeros = [[], []]

for c in range(1, 8):
    numero = int(input(f'Digite o {c}° valor: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

numeros[0].sort()
numeros[1].sort()
print(f'Todos valores: {numeros}')
print(f'Todos valores pares: {numeros[0]}')
print(f'Todos valores impares: {numeros[1]}')
