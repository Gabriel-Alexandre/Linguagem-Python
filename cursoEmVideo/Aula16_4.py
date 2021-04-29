num = (int(input('Primeiro número: ')),
       int(input('Segundo número: ')),
       int(input('Terceiro número: ')),
       int(input('Quarto número: ')))

soma = 0

print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu pela primeira vez na {num.index(3) + 1}ª posção')
else:
    print('O valor 3 não foi digitado')
print(f'Os números pares digitados são ', end='')

for n in num:
    if n % 2 == 0:
        print(n, end=' ')
        soma += 1
if soma == 0:
    print('N/A (Não foi digitado números pares)')
