from random import shuffle

Aluno1 = str(input('Primeiro aluno: '))
Aluno2 = str(input('Segundo aluno: '))
Aluno3 = str(input('Terceiro aluno: '))
Aluno4 = str(input('Quarto aluno: '))
lista = [Aluno1, Aluno2, Aluno3, Aluno4]

shuffle(lista)

print('A ordem de apresentação será ')
print(lista)