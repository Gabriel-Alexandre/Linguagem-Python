from random import randint

vit = 0

print('-*' * 15)
print('Vamos jogar Par ou Impar!')
print('-*' * 15)

while True:
    num = int(input('Digite um valor: '))
    palavra = ' '
    while palavra not in 'PI':
        palavra = str(input('Par ou Impar? (P/I) ')).strip().upper()[0]
    computador = randint(0, 10)
    total = num + computador
    print(f'Você jogou {num} e o Computador jogou {computador}')
    print(f'Total: {total}')
    print('Deu Par!' if total % 2 == 0 else 'Deu Impar!')
    if palavra == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vit += 1
        else:
            break
    elif palavra == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            vit += 1
        else:
            break
    print('Vamos jogar novamente!')
print('Game Over!')
print(f'Você venceu {vit} vezes')
