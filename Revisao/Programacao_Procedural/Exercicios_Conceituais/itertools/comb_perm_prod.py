from itertools import combinations, permutations, product

pessoas = ['Gabriel', 'Emanuel', 'Miguel', 'Alex', 'Cilene']

# print("Combinations")
# for g in combinations(pessoas, 2):
#     print(g)

# print("Permutations")
# for g in permutations(pessoas, 2):
#     print(g)

# Permite valores repetidos
print("Product")
for g in product(pessoas, repeat=3):
    print(g)

