from time import sleep

def maior(* num):
    cont = maior = 0
    print('\nAnalisando Valores...')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont}.')
    print(f'O maior valor foi {maior}.')


#Programa Principal

maior(9, 0, 1, 2, 3)
maior(9, 9, 2, 3)
