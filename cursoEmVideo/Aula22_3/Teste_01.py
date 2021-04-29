from Aula22_3 import Moeda

preco = float(input('Digite o Preço: R$'))
print(f'A metade de {Moeda.moeda(preco)} é {Moeda.metade(preco, True)}')
print(f'O dobro de {Moeda.moeda(preco)} é {Moeda.dobro(preco, True)}')
print(f'Aumentando {Moeda.moeda(preco)} em 10%, temos {Moeda.aumento(preco, 10, True)}')
print(f'Diminuindo {Moeda.moeda(preco)} em 20%, temos {Moeda.diminuir(preco, 20, True)}')
