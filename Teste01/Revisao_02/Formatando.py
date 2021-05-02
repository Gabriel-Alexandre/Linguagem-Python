num1 = 10
num2 = 3
divisao = 10 / 3
nome = "Gabriel"

#Para entender melhor a formatação, olha anotações da aulas

print(f"{divisao:.2f}")
print(f"{nome:#^20}")
print(f"{nome:/>20}")
nome = nome.ljust(20, "#")
print(nome)
nome = "Gabriel Alexandre"
print(nome.upper())
print(nome.lower())
print(nome.title())
