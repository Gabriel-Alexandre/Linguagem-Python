print('=' * 30)
print('{:^30}'.format('Banco Gabriel Bonitão'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$ '))

total = valor
cedula = 50
totalcedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        totalcedulas += 1
    else:
        if totalcedulas > 0:
            print(f'Total de {totalcedulas} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedulas = 0
        if total == 0:
            break