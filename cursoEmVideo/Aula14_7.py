num = int(input('Quantos números você quer mostrar: '))

cont = 3
t1 = 0
t2 = 1

print('{} -> {} -> '.format(t1, t2), end='')

while cont <= num:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    cont += 1
    t1 = t2
    t2 = t3
print('Fim!')