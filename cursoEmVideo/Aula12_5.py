n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

if media >= 7:
    print('APROVADO!')
#elif media < 7 and media >= 5:
elif 7 > media >= 5:
    print('RECUPERAÇÃO!')
else:
    print('REPROVADO!')