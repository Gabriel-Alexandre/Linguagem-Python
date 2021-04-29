salario = (float(input('Digite o valor do seu salário: R$ ')))

if (salario > 1250):
    novoS = salario * 0.1
else:
    novoS = salario * 0.15

print('Seu novo salário é: R$ {}'.format(novoS + salario))