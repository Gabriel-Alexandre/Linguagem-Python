num = int(input('Primeiro termo: '))
raz = int(input('Razão: '))

cont = 1
termo = num

while cont <= 10:
    print('{} -> '.format(termo), end='')
    cont += 1
    termo += raz
print('Fim!')
