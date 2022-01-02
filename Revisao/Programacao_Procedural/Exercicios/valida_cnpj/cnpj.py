def remover_caracteres(cnpj):
  # Remove caracteres que não são números
  cnpj = cnpj.replace('/','')
  cnpj = cnpj.replace('.','')
  cnpj = cnpj.replace('-','')
  return cnpj


def remover_ultimos_digitos(cnpj):
  # Remove os últimos 2 dígitos do cnpj
  return cnpj[:-2]


# Soma valores dos digitos do cnpj de acordo com o número de elementos
def soma_valores(cnpj):
  # Transforma o cnpj em uma lista
  cnpj = list(cnpj)
  # Valores fixos de multiplicação
  aux = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
  # Acumulador
  total = 0

  # Determina inicio dos valores fixos de acordo com número de elementos
  if len(cnpj) == 12:
    c = 1
  elif len(cnpj) == 13:
    c = 0

  # Realiza multiplicação dos valores de acordo com número de elementos
  for v in cnpj:
    total += int(v) * aux[c]
    c += 1
  
  return total


# Verificar qual é o dígito a ser gerado
def verifica_digito(soma):
  # Formula
  aux = 11 - (soma % 11)

  if aux > 9:
    aux = 0
  
  return aux


# Adiciona digito ao cnpj
def adiciona_digito(cnpj, digito):
  # Transforma em uma lista
  cnpj = list(cnpj)
  # Adiciona o novo dígito no fim
  cnpj.append(str(digito))
  # Transforma lista em string
  cnpj = "".join(cnpj) 

  return cnpj


# Valida cnpj
def valida_cnpj(cnpj):
  # Processa cnpj original
  cnpj_original = cnpj
  cnpj_original = remover_caracteres(cnpj_original)

  # Processa cnpj a ser gerado
  cnpj = remover_caracteres(cnpj)
  cnpj = remover_ultimos_digitos(cnpj)
  soma_valores_um = soma_valores(cnpj)
  digito_um = verifica_digito(soma_valores_um)
  cnpj = adiciona_digito(cnpj, digito_um)
  soma_valores_dois = soma_valores(cnpj)
  digito_dois = verifica_digito(soma_valores_dois)
  cnpj = adiciona_digito(cnpj, digito_dois)

  # Valida cnpj
  if cnpj_original == cnpj:
    return True
  else:
    return False