def area(largura, comprimento):
    a = largura * comprimento
    print(f'Área = {a:.2f}m²')


print('Controle de Terrenos!')
print('-' * 20)
l = float(input('Largura: '))
c = float(input('Comprimento: '))
area(l, c)
