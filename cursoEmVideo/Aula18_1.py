'''pessoas = list()
dados = list()

for c in range(0, 5):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()

for p in pessoas:
    print(f'Nome: {p[0]}')
    print(f'Idade: {p[1]}')'''

cadastro = list()
dados = list()
total = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    cadastro.append(dados[:])
    dados.clear()

    opcao = str(input('Deseja continuar ? (S/N) '))

    total += 1

    if opcao in 'Nn':
        break

cont = 0

for p in cadastro:
    cont += 1

    if cont == 1:
        maior = p[1]
        menor = p[1]
        NomeMaior = p[0]
        NomeMenor = p[0]
    else:
        if p[1] > maior:
            maior = p[1]
            NomeMaior = p[0]
        elif p[1] < menor:
            menor = p[1]
            NomeMenor = p[0]


print(f'{total} pessoas foram cadastradas!')
print(f'{maior:.2f} foi o maior peso cadastrado! -> ({NomeMaior})')
print(f'{menor:.2f} foi o menor peso cadastrado! -> ({NomeMenor})')