totalPessoas = 0
totalHomens = 0
totalMulheres = 0

while True:
    print('-' * 25)
    print('CADASTRE UMA PESSOA')
    print('-' * 25)

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: (M/F) ')).strip().upper()[0]
    if idade > 18:
        totalPessoas += 1
    if sexo == 'M':
        totalHomens += 1
    if sexo == 'F' and idade < 20:
        totalMulheres += 1

    print('-' * 25)
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('Quer continuar? (S/N) ')).strip().upper()[0]

    if opcao == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {totalPessoas}')
print(f'Ao todo temos {totalHomens} homens cadastrados')
print(f'Temos {totalMulheres} com menos de 20 anos')
