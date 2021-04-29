matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaP = somaT = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somaP += matriz[l][c]

for l in range(0, 3):
    somaT += matriz[l][2]

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print('-=' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 15)

print(f'A soma dos valores pares é: {somaP}')
print(f'A soma dos valores da terceira coluna: {somaT}')
print(f'O maior valor da segunda linha é: {maior}')
