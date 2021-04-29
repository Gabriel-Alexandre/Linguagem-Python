def ajuda(com):
    help(com)


def titulo(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


#Programa Principal
comando = ''
while True:
    titulo('Sistema de ajuda PyHelp')
    comando = str(input('Função ou Biblioteca -> ')).strip()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até Logo!')
