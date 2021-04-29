ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    opcao = str(input('Deseja continuar ? (S/N) '))
    if opcao in 'Nn':
        break

print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
print('-' * 26)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    opc = int(input('Mostrar notas de qual aluno? (-1 para finalizar) '))
    if opc == -1:
        break
    if opc < len(ficha):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    else:
        print('Opção inválida!')
        continue
print('Fim!')
