contador = 0

while True:
    condicao = input("Condição: ")

    if not condicao.isnumeric():
        print("Digite uma condição válida!")
        continue
    else:
        condicao = int(condicao)
        break
    


while contador < condicao:
    print("passo!")
    contador += 1
    print(contador)
    if contador == 10:
        break
    