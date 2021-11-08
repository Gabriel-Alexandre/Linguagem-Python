"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.
"""

def ola_mundo():
    return 'Olá mundo!'


def mestre(funcao):
    return funcao()


print(mestre(ola_mundo))
