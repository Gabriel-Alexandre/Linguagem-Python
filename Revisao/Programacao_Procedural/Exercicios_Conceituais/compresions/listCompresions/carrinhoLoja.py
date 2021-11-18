carrinho = [
    ('Produto 1', 20),
    ('Produto 2', 30),
    ('Produto 3', 40),
    ('Produto 4', 50),
    ('Produto 5', 60),
    ('Produto 6', 70),
]

total = sum([int(y) for x, y in carrinho])
print(total)
