nome = str(input('Digite seu nome: ')).strip().upper()
print('A letra (a) apareceu {} vezes'.format(nome.count('A')))
print('A primeira letra (a) apareceu na posição {}'.format(nome.find('A')+1))
print('A última letra (a) apareceu na posição {}'.format(nome.rfind('A')+1))
