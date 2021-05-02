n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

maior = n1
menor = n1

#Operadores lógicos = 'and'; 'or'; '>/</>=/=<';
#Operador diferente = 'in'

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3


print('O maior é: {}'.format(maior))
print('O menor é: {}'.format(menor))
