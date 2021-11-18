# Iteráveis: São tipos de objetos que possuem um conjunto de iteradores (valores)

# Iteradores: Um iterador é sempre um iterável, mas que produz um valor a cada vez 
# que é usado como argumento da função nativa next()

l1 = (x for x in range(10))
l2 = [1,2,3,4,5]

print(hasattr(l1, '__iter__')) # Se tem esse método, então é um objeto iterável
print(hasattr(l1, '__next__')) # Se tem esse método, então é um iterador

print(hasattr(l2, '__iter__'))
print(hasattr(l2, '__next__')) 

# Transformando a lista, que é um objeto iterável, em um iterador:
# (Isso vai permitir que eu produza os seus valores um de cada vez, assim com o for faz)
# (Internamento o for do python funciona dessa maneira, transformador a lista em um iterador e a partir daí ele vai
# iterando sobre cada elemento)

l2 = iter(l2)

print(hasattr(l2, '__iter__'))
print(hasattr(l2, '__next__'))

print(next(l2))
print(next(l2))
print(next(l2))