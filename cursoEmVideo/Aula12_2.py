num = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão: ')
print('(1) Binário')
print('(2) Octal')
print('(3) Hexadecimal')

num2 = int(input('Sua opção: '))

if num2 == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)[2:]))
elif num2 == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif num2 == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente!')