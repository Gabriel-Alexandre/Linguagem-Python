from random import randint
from operator import itemgetter
from time import sleep

jogadores = {'Jogador1': randint(1, 6),
             'Jogador2': randint(1, 6),
             'Jogador3': randint(1, 6),
             'Jogador4': randint(1, 6)}
ranking = []
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
#[['jogador3', 6], ['jogador4', 6], ['jogador1', 3], ['jogador2', 2]]

for k, v in jogadores.items():
    print(f' - {k} tirou {v} no dado.')
    sleep(1)

print('-=' * 5, 'RANKING', '-=' * 5)
for i, v in enumerate(ranking):
    print(f' - {i+1}° Lugar = {v[0]} com {v[1]}.')
    sleep(1)

