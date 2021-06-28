# List Comprehension
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for v in l1:
ex1 = [var for var in l1]
ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex1)
print(ex2)
print(ex3)
l2 = ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@').upper() for v in l2]
print(ex4)
tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
ex5 = [(y, x) for x, y in tupla]  # invertendo o (x, y) por (y, x) trocamos chave por valor e vice versa
ex5 = dict(ex5)
print(ex5)
l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]  # numeros divisiveis por 3 e por 8
print(ex6)

# Dicionary Comprehension
lista = [
    ('chave', 'valor1'),
    ('chave1', 'valor2')
]
d1 = {x.capitalize(): y.upper() for x, y in lista}   # d1 = {x(chave): y(valor) for x, y in lista}
print(d1)
