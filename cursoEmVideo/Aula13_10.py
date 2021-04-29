for cont in range(1, 6):
    peso = float(input('Peso da {}ª pessoa (Em Kg): '.format(cont)))

    if cont == 1:
        maior = peso
        menor = peso

    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior valor é: {:.1f} Kg'.format(maior))
print('O menor valor é: {:.1f} Kg'.format(menor))