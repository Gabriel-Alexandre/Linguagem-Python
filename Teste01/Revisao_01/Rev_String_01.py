#Projeto criado apenas para facilitar a revisão do conteúdo de python;

nome = str(input('Digite seu nome completo: ')).strip()
print('Em maiusculas: {}'.format(nome.upper()))
print('Em minusculas: {}'.format(nome.lower()))
print('Quantidade de letras: {}'.format(len(nome) - nome.count(' ')))
#print('Quantidade de letra do primeito nome: {}'.format(nome.find(' ')))
separa = nome.split()
print(separa)
print('Seu primeiro nome é: {}'.format(separa[0]))
print('Quantidade de letas do primeiro nome: {}'.format(len(separa[0])))
