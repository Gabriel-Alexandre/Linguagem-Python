import sqlite3

conn = sqlite3.connect('db.sqlite3')

result = conn.execute('select titulo, categoria, modelo, marca, ano, tipoVeiculo, cor from cars')

for car in result:
    for v in car:
        print(v)
    print()

conn.close()