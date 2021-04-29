times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo',
         'Atlético-PR')

'''for t in times:
    print(t)'''
print('=' * 30)
print(f'Os 5 primeiros são: {times[:5]}')
print('=' * 30)
print(f'Os quatro últimos são: {times[7:]}')
print('=' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=' * 30)
print(f'O Chapecoese está na {times.index("Chapecoense") + 1}ª Posição')