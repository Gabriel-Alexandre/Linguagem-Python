while True:
    num = int(input('Digite o número para ver sua tabuada: '))
    print('_' * 25)
    if num < 0:
        break
    for cont in range(0, 10):
        cont += 1
        multiplicacao = num * cont
        print(f'{num} x {cont} = {multiplicacao}')
    multiplicacao = 0
    print('-' * 25)
print('Fim!')
