valores = list()

while True:
    valor = int(input('Digite um valor: '))

    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado!')
    else:
        print('Esse valor já foi adicionado. Tente novamente!')

    opcao = str(input('Quer continuar: (S/N) ')).strip().upper()

    if opcao == 'N':
        break

#valores.sort()
print(f'Os valores digitados foram: {sorted(valores)}')
