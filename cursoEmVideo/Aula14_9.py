soma = maior = menor = cont = 0
opcao = 'S'

while not 'N' in opcao:
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input('Quer continuar? (S/N) ')).strip().upper()[0]

media = soma / cont
print('Você digitou {} números!'.format(cont))
print('A média entre eles foi {:.2f}!'.format(media))
print('O maior foi {}!'.format(maior))
print('O menor foi {}!'.format(menor))