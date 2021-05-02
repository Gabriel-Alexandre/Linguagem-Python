contador = 0

while contador < 10:
    print(contador)
    contador += 1

    if contador == 8:
        continue
else:
    #quando a condição se torna falsa, o programa executa o else.
    #a menos que o laço seja enterronpido por um break.
    print("Else")
    