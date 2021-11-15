# O Funcionamente é semelhante ao de listCompresions
# O que mudo é a forma de implementar, que a compressão é em um set
# Raciocínio semelhante ao dictCompresions

s1 = {v for v in range(0, 17, 2)}

print(s1, type(s1))