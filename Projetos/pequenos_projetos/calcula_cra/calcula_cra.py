medias = {
    "C1": 7.8,
    "CVET": 8.6,
    "CL1": 7.0,
    "IEC": 7.4,
    "IP": 8.6,
    "LIP": 8.6,
    "MET": 9.9,
    "LC": 9.8,
    "C2": 9.0,
    "F1": 8.0,
    "FEX": 7.8,
    "IAL": 7.9,
    "CP1": 7.9,
    "CS": 9.4,
    "ELE1": 7.0,
    "LP1": 10.0,
    "LLP1": 10.0,
    "PA": 9.4,
}

medias["C3"] = 8.7
medias["CL2"] = 9.5
medias["ED"] = 9.8
medias["LP2"] = 10.0
medias["MAT"] = 10.0
medias["MEC"] = 10.0

print("Calculando CRA...")

soma = 0
for k, v in medias.items():
    soma += v

cra = soma / len(medias)

print(f"Seu CRA é: {cra}")