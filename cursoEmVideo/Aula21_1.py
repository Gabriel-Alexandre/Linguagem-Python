def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    elif 18 <= idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


nasc = int(input('Ano de Nascimento: '))
print(voto(nasc))
