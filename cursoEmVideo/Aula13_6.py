print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

num = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
decimo = num + (11 - 1) * raz

for cont in range(num, decimo, raz):
    print('{} '.format(cont), end='-> ')
print('Acabou!')