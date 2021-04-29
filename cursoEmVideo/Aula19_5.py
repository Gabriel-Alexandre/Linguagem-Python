cadastro = dict()
lista = list()
soma = media = 0

while True:
    cadastro.clear()

    cadastro['Nome'] = str(input('Nome: '))
    while True:
        cadastro['Sexo'] = str(input('Sexo: (M/F) ')).upper().strip()[0]
        if cadastro['Sexo'] in 'MF':
            break
        else:
            print('Digite M ou F.')
    cadastro['Idade'] = int(input('Idade: '))
    soma += cadastro['Idade']

    lista.append(cadastro.copy())

    while True:
        opcao = str(input('Deseja continuar ? (S/N) ')).upper().strip()[0]
        if opcao in 'SN':
            break
        else:
            print('Digite S ou N.')

    if opcao in 'N':
        break
media = soma / len(lista)

print(f'Foram cadastradas {len(lista)} pessoas')
print(f'A média de idade é de {media:5.2f}')
print('A mulheres cadastradas foram ', end='')
for p in lista:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ', end='')
print()
print('Pessoas com idade acima da média ')
for p in lista:
    if p['Idade'] >= media:
        print('  ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')


