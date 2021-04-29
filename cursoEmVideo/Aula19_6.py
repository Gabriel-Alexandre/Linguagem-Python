jogadores = dict()
gols = list()
lista = list()

while True:
    jogadores.clear()
    gols.clear()

    jogadores['Nome'] = str(input('Nome: '))
    total = int(input(f'Quantas partidas {jogadores["Nome"]} Jogou ? '))
    for c in range(1, total+1):
        gols.append(int(input(f' - Quantos gols foram marcados na {c}° partida: ')))
    jogadores['Gols'] = gols[:]
    jogadores['Total'] = sum(gols)

    lista.append(jogadores.copy())

    while True:
        opcao = str(input('Deseja continuar ?(S/N) ')).upper().strip()[0]
        if opcao in 'SN':
            break
        else:
            print('Digite S ou N.')
    if opcao == 'N':
        break

print('-=' * 30)
print('cod ', end='')
for i in jogadores.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(lista):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador ? (-1 para parar) '))
    if busca == -1:
        break
    if busca >= len(lista):
        print(f'Jogador com código {busca} não encontrado. Tente novamente!')
    else:
        print(f'LEVANTAMENTO DO JOGADOR: {lista[busca]["Nome"]}')
        for i, g in enumerate(lista[busca]['Gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
        print('-' * 40)
print('<< ENCERRADO >>')