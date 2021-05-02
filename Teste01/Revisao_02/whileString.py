contador = 0
nome = "gabriel alexandre"
tamanho = len(nome)
novoNome = ''

letra = input("Letra maiúsculas: ")

#Iteração:
while contador < len(nome):
    if letra == nome[contador]:
        novoNome += nome[contador].upper()
    else:
        novoNome += nome[contador]

    contador += 1
 
print(novoNome)
