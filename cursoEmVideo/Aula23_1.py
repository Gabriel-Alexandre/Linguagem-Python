def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um número inteiro válido.')
            continue
        else:
            return n


def LeiaReal(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um número real válido')
            continue
        else:
            return n


#Programa Principal
numInt = LeiaInt('Digite um número inteiro: ')
numReal = LeiaReal('Digite um número real: ')
print(f'O númeor inteiro digitado foi: {numInt}')
print(f'O númeor real digitado foi: {numReal}')
