from classes import Cliente

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1  # composição pois ao apagar cliente1 da classe cliente também apagamos os endereços do cliente1 na class
# Endereco
print()

clientes2 = Cliente('Maria', 55)
clientes2.insere_endereco('Salvador', 'BH')
clientes2.insere_endereco('Rio de Janeiro', 'RJ')
print(clientes2.nome)
clientes2.lista_enderecos()
print()

clientes3 = Cliente('Maria', 55)
clientes3.insere_endereco('Salvador', 'BH')
clientes3.insere_endereco('Rio de Janeiro', 'RJ')
print(clientes3.nome)
clientes3.lista_enderecos()
print()

print('################################################')


