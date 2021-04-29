'''CatetoOP = float(input('Digite o valor do cateto oposto: '))
CatetoAD = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = (CatetoOP ** 2 + CatetoAD ** 2) ** (1/2)
print('A hipotenusa é {:.2f}'.format(hipotenusa))'''

from math import hypot

CatetoOP = float(input('Digite o valor do cateto oposto: '))
CatetoAD = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(CatetoOP, CatetoAD)
print('A hipotenusa é {:.2f}'.format(hipotenusa))