nome = str(input('Digite seu nome completo: ')).strip()

print('Maiúsculo: {}'.format(nome.upper()))
print('Minúsculo: {}'.format(nome.lower()))
print('Total de letra: {}'.format(len(nome) - nome.count(' ')))

separa = nome.split()
print(separa)

print('Primeiro nome: {}'.format(separa[0]))
print('Total de letras do primeiro nome: {}'.format(nome.find(' ')))
#print('Número de letras do primeiro nome: {}'.format(len(separa[0])))