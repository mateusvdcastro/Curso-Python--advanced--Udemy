import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

'''cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')
'''

'''#cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Mateus", 105.5)')
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
               {'nome': 'joão', 'peso': 25})
cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
               {'id': None, 'nome': 'Daniel', 'peso': 95})
conexao.commit()'''

#cursor.execute('UPDATE clientes SET nome = :nome WHERE id=:id',
#               {'nome': 'Joana', 'id': 2})
#cursor.execute('DELETE FROM clientes WHERE id=:id',
#               {'id': 3})

#cursor.execute('SELECT * FROM clientes')

#cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso',
#               {'peso': 50})

for linha in cursor.fetchall():
    identificador, nome, peso = linha
    print(identificador, nome, peso)

cursor.close()
conexao.close()
