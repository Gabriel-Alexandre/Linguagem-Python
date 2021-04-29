somaIdade = 0
somaMulheres = 0

for cont in range(1, 5):
    print('---- {}ª Pessoa ----'.format(cont))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()

    somaIdade += idade

    if cont == 1:
        maiorIdadeHomem = idade
    elif idade > maiorIdadeHomem and sexo == 'M':
        maiorIdadeHomem = idade
        nomeHomem = nome

    if idade < 20 and sexo == 'F':
        somaMulheres += 1

mediaGrupo = somaIdade / 4
print('Média de idade: {}'.format(mediaGrupo))
print('{} é o homem mais velhor e tem {} anos'.format(nomeHomem, maiorIdadeHomem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(somaMulheres))