from Dados import produtos, pessoas, lista

# nova_lista = [x * 2 for x in lista]
nova_lista = map(lambda x: x * 2, lista)  # A função map não retorna uma lista, mas um iterador por isso precisa ser
# convertida depois, por este motivo list comprehension se torna mais eficaz para esse tipo de uso
print(nova_lista)
print(list(nova_lista))  # type cast


precos = map(lambda p: p['preço'], produtos)

for preco in precos:
    print(preco, end=', ')
print()


def aumenta_preco(p):
    p['preço'] = round(p['preço'] * 1.05, 2)
    return p


novos_produtos = map(aumenta_preco, produtos)
for produton in novos_produtos:
    print(produton)

'''nomes = []
nome = [nomes.append(pessoas['nome']) for pessoas in pessoas]
print(nomes)'''

nomes = map(lambda p: p['nome'], pessoas)
for pessoa in nomes:
    print(pessoa, end=', ')
