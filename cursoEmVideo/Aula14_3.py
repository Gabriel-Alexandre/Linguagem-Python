n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

parar = False

while not parar:
    print('=-' * 20)
    print('''    (1) Somar
    (2) Multiplicar
    (3) Maior
    (4) Novos números
    (5) Sair do programa\n''')
    opcao = int(input('Qual é sua opção: '))
    print('=' * 20)

    if opcao == 1:
        print('Resultado: {}'.format(n1 + n2))
    elif opcao ==2:
        print('Resultado: {}'.format(n1 * n2))
    elif opcao == 3:
        if n1 == n2:
            print('Resultado: Iguais')
        elif n1 > n2:
            print('Resultado: {} é maior'.format(n1))
        else:
            print('Resultado: {} é maior'.format(n2))
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        parar = True
    else:
        print('Opção inválida!')
    print('=' * 20)
print('Fim!')