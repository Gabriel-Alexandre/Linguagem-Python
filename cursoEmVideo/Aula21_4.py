def LeiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digte Um Número Inteiro Válido.')
        if ok:
            break
    return valor


#Programa Principal
n = LeiaInt('Digite um número: ')
print(f'Você acabou de digitar {n}.')
