expressao = str(input('Digite um a expressão: '))
pilha = list()
'''soma1 = 0
soma2 = 0

for simb in expressao:
    if simb == '(':
        soma1 += 1
    elif simb == ')':
        soma2 += 1

if soma1 == soma2:
    print('Sua expressão está correta!')
else:
    print('Sua expressão não é válida!')'''

for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão não é válida!')
