from itertools import groupby, tee

alunos = [
    {'nome': 'Mateus', 'nota': 'A'},
    {'nome': 'Ana', 'nota': 'B'},
    {'nome': 'Luiz', 'nota': 'B'},
    {'nome': 'Maria', 'nota': 'A'},
    {'nome': 'Carla', 'nota': 'C'},
    {'nome': 'José', 'nota': 'C'},
    {'nome': 'Isabel', 'nota': 'D'},
]

ordena = lambda item: item['nota']
alunos.sort(key= ordena)  # precisa ordenar os dados antes de usar groupby
for aluno in alunos:
    print(aluno)

alunos_agrupados = groupby(alunos, ordena)
print(alunos_agrupados)
for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)  # impede que o iterador se esgote no "for aluno" e cause problemas
    # va1 e va2 são duas cópias iguais do iterador

    print(f'Agrupamento: {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram nota {agrupamento}')
    print()

'''Groupby é simplesmente o que o nome diz, agrupar por...
Por exemplo, imagine que eu tenha um grupo de
pessoas com idades variadas, porém, algumas delas tem
exatamente a mesma idade. Suponha que eu queira escrever um programa
para separar as pessoas de mesma idade em seus próprios grupos...

Esse é o cenário exato para usar groupby(vamos agrupar por idade).'''

from itertools import groupby

pessoas = [
    {'nome': 'luiz', 'idade': 30},
    {'nome': 'joão', 'idade': 20},
    {'nome': 'maria', 'idade': 40},
    {'nome': 'helena', 'idade': 21},
    {'nome': 'rosana', 'idade': 20},
    {'nome': 'osvaldo', 'idade': 21},
    {'nome': 'eleonor', 'idade': 40},
]


def retorna_idade(pessoa):
    return pessoa['idade']


ordenadas_por_idade = sorted(pessoas, key=retorna_idade)
print(ordenadas_por_idade)
agrupadas_por_idade = groupby(ordenadas_por_idade, key=retorna_idade)
print(agrupadas_por_idade)

for idade, grupo in agrupadas_por_idade:
    print(f'Grupo de pessoas de {idade} anos')

    for pessoa in grupo:
        print('\t', pessoa)

"""
Saída:

Grupo de pessoas de 20 anos
         {'nome': 'joão', 'idade': 20}
         {'nome': 'rosana', 'idade': 20}
Grupo de pessoas de 21 anos
         {'nome': 'helena', 'idade': 21}
         {'nome': 'osvaldo', 'idade': 21}
Grupo de pessoas de 30 anos
         {'nome': 'luiz', 'idade': 30}
Grupo de pessoas de 40 anos
         {'nome': 'maria', 'idade': 40}
         {'nome': 'eleonor', 'idade': 40}
"""