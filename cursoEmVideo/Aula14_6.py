primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro
cont = 1
total = 0
continua = 10

while continua != 0:
    total += continua
    while cont <= total:
        print('{} -> '.format(termo), end='')
        cont += 1
        termo += razao
    print('Pausa')
    continua = int(input('Quantos números você quer mostrar a mais? '))
print('Progressão finalizado com {} termos mostrados!'.format(total))