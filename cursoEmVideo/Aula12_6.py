from datetime import date

atual = date.today().year
ano = int(input('Digite o seu ano de nascimento: '))

idade = atual - ano

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
elif idade > 25:
    print('MASTER')