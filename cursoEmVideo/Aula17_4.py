valores = list()
cont = 0

while True:
    valores.append(int(input('Digite um valor: ')))
    cont += 1

    opcao = str(input('Deseja continuar ? (S/N) ')).strip().upper()
    if opcao in 'N':
        break
print(f'Você digitou {cont} elementos')
print(f'Os valores em ordem decrescente são {sorted(valores, reverse=True)}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')