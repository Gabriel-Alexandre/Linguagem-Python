lista = [2, 4, 6, 7, 8]

ehPar = lambda x: x % 2 == 0

for valor in lista:
    if(ehPar(valor)):
        print(f"{valor} Eh par!")
    else:
        print(f"{valor} Eh impar!")
