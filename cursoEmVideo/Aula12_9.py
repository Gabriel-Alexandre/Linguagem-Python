print('{:=^40}'.format('LOJAS GABRIEL BONITÃO'))

preco = float(input('Preço das compras: R$ '))

print('''Formas de pagamento:
(1) À vista dinheiro/cheque
(2) À vista cartão
(3) 2x cartão (Sem juros)
(4) 3x ou mais cartão (Com juros)''')

opcao = int(input('Qual opção: '))

if opcao == 1:
    total = preco - (preco * 0.1)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
    parcela = preco / 2
    print('Parcela: 2 x R$ {:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 0.2)
    totalParc = int(input('Quantas parcelas você deseja: '))
    parcela = total / totalParc
    print('Parcela: {} x R$ {:.2f}'.format(totalParc, parcela))
else:
    total = preco
    print('Opção inválida!')

print('Total: R$ {:.2f}'.format(total))


