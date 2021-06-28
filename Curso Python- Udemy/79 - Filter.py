from Dados import pessoas, lista, produtos

# nova_listas = [x for x in lista if x > 5]
nova_listas = filter(lambda x: x > 5, lista)
print(nova_listas)
print(list(nova_listas))

novo_produto= filter(lambda p: p['preço'] > 2500, produtos)
for produto in novo_produto:
    print(produto)


def filtra(produto):
    if produto['preço'] > 50:
        return True


novo_produto2 = filter(filtra, produtos)
print(list(novo_produto2))

print('-'*45)


def filtra_idade(pessoas):
    if pessoas['idade'] >= 18:
        return True
    else:
        return False
    

maior_idade = filter(filtra_idade, pessoas)
for maior in maior_idade:
    print(maior)
