"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(indice, estados, cidades)  # une listas conforme a menor lista
# print(list(cidades_estados)) # note que o for abaixo não é executado caso esse código esteja em funcionamento
# isso ocorre pois zip cria um iterador pra você consumir... Ao usar list, você consumiu esse iterador chegando ao fim
# dele. No for já não existem mais valores no seu iterador.
for indice, estados, cidades in list(cidades_estados):
    print(indice, estados, cidades)

cidades1 = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
estados1 = ['SP', 'MG', 'BA']

cidades_estados_todos = zip_longest(estados1, cidades1, fillvalue='Estado')  # exibe todos valores, os que não possuem correspondência ele
print(list(cidades_estados_todos))            # escreve como "none" mas pode trocar isso com fillvalue que só existe em zip_longest
# não usar o zip_longest com o count (função de contador) pois gera um loop infinito

# exercício
listaA = [1, 2, 3, 4, 5, 6, 7]
listaB = [1, 2, 3, 4]
lista_s = zip(listaA, listaB)
lista_soma = []
for v in lista_s:
    lista_soma.append(v[0] + v[1])
print(list(lista_soma))

lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]  # melhor solução do exercício acima usando list comprehension
print(lista_soma)

# lista_soma = []
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lis    ta_b[i])
# print(lista_soma)

# lista_soma = []
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

from itertools import zip_longest
# para pegar os valores maiores também 
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma) # output: [22, 4, 6, 10, 55, 60, 70]'''
