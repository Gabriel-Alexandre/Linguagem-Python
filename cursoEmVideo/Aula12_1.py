Vcasa = float(input('Valor da casa: R$ '))
Salario = float(input('Salário: R$ '))
Qanos = int(input('Anos: '))

Pmensal = Vcasa / (Qanos * 12)
Psalario = Salario * 0.3

if (Pmensal > Psalario):
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo APROVADO!')