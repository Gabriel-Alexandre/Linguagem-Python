cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
        'Seis', 'Sete', 'Oito', 'Nove', 'Dez')

while True:

    while True:
        num = int(input('Digite um número entre 0 e 10: '))
        if num >= 0 and num <= 10:
            break
        print('Tente novamente!')
    print(f'Você digitou o número {cont[num]}')

    opcao = ' '
    while True:
        opcao = str(input('Você quer continuar? (S/N) ')).strip().upper()
        if opcao in 'NS':
            break
    if opcao == 'N':
        break
print('Fim!')