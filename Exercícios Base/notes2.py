import copy
val = {1: 'a', 2: 'b', 3: 'c', 'd': ['Luiz', 'Mario']}
v = copy.deepcopy(val)   # como copiar dicionários sem fazer uma relação entre eles
v[1] = 'Maria'
v['d'][0] = 'Antônio'
print(val)
print(v)
val1 = {'nome': 'Marta', 'Idade': 52, 'Jogar': 'Fora'}
val.update(val1)   # update para juntar os dicionários
val.pop('Jogar')
print(val)

# sets em Python (conjuntos), são imutáveis e não confundir com dicionários (geralmente usados pr eliminar elementos
# duplicados de uma lista)
s1 = {1,2,3,4}
s2 = set()
s2.add(2)
s2.add(3)
s2.add(3)   # não aceita elementos duplicados
s2.update('Python') # a diferença do update para o add, é que o primeiro é iterável e irá iterar sem respeitar ordens
s2.update([1,2,3,4])
#s2.discard(3)
print(s2)

s3 = {1,2,3,4,5, 7}
s4 = {1,2,3,4,5,6}
s5 = s3 | s4        # pode usar .union ou | para unir os sets
s6 = s3 & s4        # & irá pegar a interseção entre eles, ou seja todos os numeros comuns aos dois sets
s7 = s3 - s4        # irá pegar o elemento que apenas o set da esquerda possui como único.
s8 = s3 ^ s4        # elementos que estão nos dois sets, mas não nos dois ao mesmo tempo
print(f'[{s5} *** {s6} *** {s7}]')
