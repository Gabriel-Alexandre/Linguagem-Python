palavras = ('Aprender', 'Programar', 'Linguagem', 'Python',
            'Curso', 'Gratis', 'Estudar', 'Praticar',
            'Trabalhar', 'Mercado', 'Programador', 'Futuro')

for p in palavras:
    print(f'\nPara cada palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
