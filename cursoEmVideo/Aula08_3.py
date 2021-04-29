import math

angulo = float(input('Digite o valor do ângulo: '))

seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O seno é {:.2f}'.format(seno))
print('O coseno é {:.2f}'.format(coseno))
print('O tangente é {:.2f}'.format(tangente))