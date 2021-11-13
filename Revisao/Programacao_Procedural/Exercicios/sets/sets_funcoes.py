# Sets são conjuntos, ou seja, são listas de valores únicos
# Sets não tem índices, seu acesso é realizado usando o valor

# maneiras de iniciar um set

numero = set()
print(numero, type(numero))
numero = {1, 2, 3, 4, 5}
print(numero, type(numero))

numero.add(6)
print(numero)
numero.update('python')
print(numero)
numero.discard('p')
print(numero)
numero.clear()
print(numero)

set1 = {1,2, 3, 4, 5, 7}
set2 = {1,2, 3, 4, 5, 6}
set3 = set1 | set2
set4 = set1 & set2
set5 = set2 - set1
set6 = set1 ^ set2

print(set3)
print(set4)
print(set5)
print(set6)

# add (Adiciona)
# update (Atualiza) - Pode ser usado para iterar 
# clear (limpa)
# discard (remove)
# union | (Une)
# intersection & (Elementos em comum)
# difference - (Elementos apenas do set a esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

