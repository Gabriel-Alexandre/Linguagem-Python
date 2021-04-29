from Aluguel_de_Carros.Biblioteca.Interface import *
from Aluguel_de_Carros.Biblioteca.Arquivo import *

cabecalho('SISTEMA DE ALUGUEL DE CARROS')

arq = 'Carros_Disponíveis.txt'

if ArquivoExiste(arq):
    print(f'Arquivo {arq} encontrado com sucesso!')
else:
    print(f'Arquivo {arq} não encontrado!')
    CriarArquivo(arq)

while True:
      reposta = menu(['Alugar um carro',
                      'Editar',
                      'Sair do programa'])
      if reposta == 1:
            # Opção de alugar um novo carro.
            print()
      elif reposta == 2:
            # Opção para editar o aluguel do carro.
            print()
      elif reposta == 3:
            # Opção de sair do sistema.
            cabecalho('Saindo do sistema... Até logo!')
            break
      else:
            # Digitou uma opção errada no menu.
            cabecalho('ERRO: Digite uma opção válida!')

'''
-> Falta decidir como vou organizar o meu sistema para controle dos carros alugados e disponíveis.
'''

