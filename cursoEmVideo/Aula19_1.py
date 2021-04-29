aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input('Média: '))
if aluno['Media'] >= 7:
    aluno['Situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['Situacao'] = 'Recuperação'
else:
    aluno['SGituacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
