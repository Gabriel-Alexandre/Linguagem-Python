from Aula22_2 import Moeda

preco = float(input('Digite o Preço: R$'))
print(f'A metade de {Moeda.moeda(preco)} é {Moeda.moeda(Moeda.metade(preco))}')
print(f'O dobro de {Moeda.moeda(preco)} é {Moeda.moeda(Moeda.dobro(preco))}')
print(f'Aumentando {Moeda.moeda(preco)} em 10%, temos {Moeda.moeda(Moeda.aumento(preco, 10))}')
