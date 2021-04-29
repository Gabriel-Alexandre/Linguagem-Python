print('-' *  20)
print('LOJA GABRIEL BONITÃO')
print('-' * 20)

contador = contProd = total = 0

while True:
    contador += 1

    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))

    total += preco

    if preco > 1000:
        contProd += 1
    if contador == 1:
        nProdBarato = nome
        pProdBarato = preco
    else:
        if preco < pProdBarato:
            nProdBarato = nome
            pProdBarato = preco

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? (S/N) ')).strip().upper()[0]

    if opcao == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi {total:.2f}')
print(f'Temos {contProd} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nProdBarato} que custa R$ {pProdBarato:.2f}')