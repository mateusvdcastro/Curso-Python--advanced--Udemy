from Dados import pessoas, lista, produtos
from functools import reduce

# ao inves de criar contadores eu posso usar o reduce
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)  # ac = acumulador; i = item; 0 = primeiro valor
print(soma_lista)

soma_precos = reduce(lambda ac, p: p['preço'] + ac, produtos, 0)
print(soma_precos)

soma_idades = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(round(soma_idades/len(pessoas)))  # média das idades
