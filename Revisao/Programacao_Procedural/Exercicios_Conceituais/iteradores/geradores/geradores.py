# Gerador: é um procedimento especial que pode ser usado para controlar iteradores

# - Geradores são mais leves, pois ocupam menos espaço na memória.
# - Os valores são gerados em tempo de execução do programa.
# - Geralmente são usados juntos com algum tipo de estrutura de dados.
# - São usados principalmente para gerar sequências de valores.
# - É importante conhecer, pois muitas funções importantes são implementadas com geradores internamente.

# Eu posso enchergar como um novo conceito que é UM POUCO parecido com funções, porém diferente e mais eficiente para grandes
# estruturas de dados, pois não retorna todos os valores de uma vez, seu funcionamento é seguindo o sentido de um iterador, no
# sentido que, quando o gerador é chamado ele só retorna um valor, e esse comportamento se repete até que sua estrutura tenha 
# sido totalmente retornada. Em síntese, em minha cabeça posso enchegar os geradores como funções que retornam iteradores.

# Seu funcionamento é tão semelhante ao de iteradores que, assim como listas podem ser iteradas em um for, os geradores também
# podem.

from time import sleep

# Criando geradores a partir de função:

def gerador():
    for i in range(10):
        yield i
        sleep(0.1)
        
g = gerador()
print(next(g))
print(next(g))
print(next(g))

# Criando geradores a partir de compressão:
l1 = (x for x in range(100000))



