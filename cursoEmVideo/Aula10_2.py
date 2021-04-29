velocidade = (float(input('Velocidade (Em Km/h): ')))

if (velocidade < 81):
    print('Continue dirigindo com segurança!')
else:
    print('Você ultrapassou o limite de velocidade!')
    multa = (velocidade - 80) * 7
    print('Multa R$ {}'.format(multa))