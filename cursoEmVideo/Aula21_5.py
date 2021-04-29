def notas(*n, sit=False):
    """
    -> Função Para Analisar Situação das Notas de Vários Alunos
    :param n: Uma ou Mais Notas (Aceita Várias)
    :param sit: Valor Opcional Indicando Se Deve ou Não Mostrar a Situação dos Alunos
    :return: Dicionário com Informações Sobre As Notas Da Turma
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n) / len(n)

    if sit:
        if r['Media'] >= 7:
            r['Situação'] = 'Boa'
        elif r['Media'] >= 5:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'Ruim'

    return r


#Programa Principal
resp = notas(5, 6, 4, sit=True)
print(resp)
