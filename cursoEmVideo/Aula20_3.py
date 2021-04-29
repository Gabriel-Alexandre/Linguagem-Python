from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        print('-=' * 20)
        for c in range(i, f+1, p):
            print(f'{c} ', end='', flush=True)
            sleep(0.3)
        print()
        print('-=' * 20)
    else:
        print('-=' * 20)
        for c in range(i, f-1, -p):
            print(f'{c} ', end='', flush=True)
            sleep(0.3)
        print()
        print('-=' * 20)


contador(1, 10, 1)
contador(10, 0, 2)

print('Vamos Fazer Uma Contagem Personalizada')
while True:
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    contador(inicio, fim, passo)
    while True:
        opcao = str(input('Deseja realizar outra contagem ? (S/N) ')).strip().upper()[0]
        if opcao not in 'SN':
            print('Opção inválida. Tente novamente!')
        else:
            break
    if opcao == 'N':
        break
    print('Vamos Realizar Outra Contagem')
print('<< ENCERRADO >>')
