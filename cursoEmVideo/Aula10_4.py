distancia = (float(input('Digite a distância: ')))

if (distancia <= 200):
    valor = distancia * 0.50
else:
    valor = distancia * 0.45

print('O valor da viajem é R$ {}'.format(valor))