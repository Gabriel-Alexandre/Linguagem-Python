numeros = list()
pares = list()
impares = list()

while True:
    numeros.append(int(input('Digite um valor: ')))
    opcao = str(input('Deseja continuar ? (S/N) '))

    if opcao in 'Nn':
        break

'''for c in range(0, len(numeros)):
        if numeros[c] % 2 == 0 and numeros[c] not in pares:
            pares.append(numeros[c])
        elif numeros[c] % 2 == 1 and numeros[c] not in impares:
            impares.append(numeros[c])'''

for c, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'Lista (Todos os números): {numeros}')
print(f'Lista (Números pares): {pares}')
print(f'Lista (Números impares): {impares}')
