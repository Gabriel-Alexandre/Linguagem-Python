from Aula22_1 import Moeda

preco = float(input('Digite o Preço: R$ '))
print(f'A metade de R${preco} é R${Moeda.metade(preco)}')
print(f'O dobro de R${preco} é R${Moeda.dobro(preco)}')
print(f'Aumentando R${preco} em 10%, temos R${Moeda.aumento(preco, 10)}')

