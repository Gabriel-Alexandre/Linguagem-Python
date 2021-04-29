from datetime import datetime

dados = dict()
dados['Nome'] = str(input('Nome: '))
anoNasc = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - anoNasc
dados['Ctps'] = int(input('Carteira de trabalho: '))
if dados['Ctps'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)

for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
