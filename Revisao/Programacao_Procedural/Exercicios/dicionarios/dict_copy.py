import copy 

dicionario = {
    1: 'Um',
    2: 'Dois',
    3: 'Três',
}

# Em python isso significa que copyDictionary está apontando para dicionario, então não posso fazer uma copia
# de um dicionario assim.

# copyDictionary = dicionario

# copyDictionary[1] = 'um'

# ***********************************************************************************************************

# Se eu fizer uma copia assim, quando eu for tentar alterar uma lista dentro de copyDictionary, vai mudar em dicionario
# tbm, então essa também não é uma maneira correta de fazer uma copia de um dicionario.

# copyDictionary = dicionario.copy()

# copyDictionary[1] = 'um'

# ***********************************************************************************************************

## O mesmo raciocínio se aplica para listas

copyDictionary = copy.deepcopy(dicionario) # Essa é a maneira correta de fazer uma copia de um dicionario

copyDictionary[1] = 'um'

print(dicionario)
print(copyDictionary)

lista = [1, 2, 3, 4]

l = copy.deepcopy(lista) # Essa é a maneira correta de fazer uma copia de uma lista

l[0] = 'Um'

print(lista)
print(l)