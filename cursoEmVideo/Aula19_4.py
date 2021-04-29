dados = dict()
partidas = list()

dados['Nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {dados["Nome"]} jogou ? '))

for c in range(0, total):
    partidas.append(int(input(f'    Quantos gols na partida {c+1} ? ')))

dados['Gols'] = partidas[:]
dados['Total de Gols'] = sum(partidas)

print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f' - O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["Nome"]} jogou {len(dados["Gols"])} partidas.')
for c, v in enumerate(dados['Gols']):
    print(f'    => Na partida {c+1} fez {v}.')
print(f'Total de gols = {dados["Total de Gols"]}')