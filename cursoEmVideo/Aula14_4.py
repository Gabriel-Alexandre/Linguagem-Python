'''from math import factorial

num = int(input('Digite um número para calcular seu fatorial: '))
fatorial = factorial(num)

print('O fatorial de {} é {}).format(num, fatorial))'''

'''num = int(input('Digite um número para calcular seu fatorial: '))
aux = num
fatorial = 1

while aux != 0:
    fatorial = aux * fatorial
    aux -= 1

if num == 0 or num == 1:
    fatorial = 1

print('{}! = {}'.format(num, fatorial))'''

num = int(input('Digite um número para calcular seu fatorial: '))

cont = num
fatorial = 1

print('{}! = '.format(num), end='')

while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial *= cont
    cont -= 1
print('{}'.format(fatorial))