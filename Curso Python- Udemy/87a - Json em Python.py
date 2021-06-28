import json

d1 = {
    'Pessoa 1 - Python Orientado a Objetos': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    }
}

d1_json = json.dumps(d1, indent=True)  # converteu o dicionário para json

with open('87c-abc.txt', 'w+') as file1:
    file1.write(d1_json)
