from datetime import date

atual = date.today().year
soma1 = 0
soma2 = 0

for cont in range(1, 8):
    ano = int(input('Digite em que ano a {}ª pessoa nasceu: '.format(cont)))
    idade = atual - ano
    if idade >= 21:
        soma1 += 1
    else:
        soma2 += 1

print('{} são maiores de idade'.format(soma1))
print('{} são menores de idade'.format(soma2))