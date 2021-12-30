'''
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
'''

from itertools import combinations, permutations, product
pessoas = ['Luiz', 'André', 'Eduardo', 'Mateus', 'Iago']
for grupo in combinations(pessoas, 2): # todas as combinações possíveis em grupos de 2 nessa lista
    print(grupo, end=' ')
print('-'*50)
for grupo2 in permutations(pessoas, 2):
    print(grupo2, end=' ')  # aqui a ordem importa
print('-'*50)
for grupo3 in product(pessoas, repeat=2):
    print(grupo3, end=' ')
