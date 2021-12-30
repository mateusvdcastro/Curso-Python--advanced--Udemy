import json

with open('87c-abc.txt', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)  # converteu de json para um dicionário, para poder iterar

for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)
