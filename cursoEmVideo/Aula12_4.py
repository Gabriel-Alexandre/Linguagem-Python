from datetime import date

atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano

print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))

if idade == 18:
    print('Você deve se alistar imediatamente!')
elif idade < 18:
    saldo = 18 + idade
    anoA = atual - saldo
    print('Faltam {} anos para o seu alistamento!'.format(saldo))
    print('Seu alistamento será em {}'.format(anoA))
else:
    saldo = idade - 18
    anoA = atual - saldo
    print('Você deveria ter se alistado há {} anos!'.format(saldo))
    print('Seu alistamento foi em {}'.format(anoA))