#https://docs.python.org/3/library/functions.html#open
#https://docs.python.org/3/library/io.html#io.IOBase.seek

arquivo = open('87abc.txt', 'w+')
arquivo.write('Linha 1 - Python Orientado a Objetos\n')
arquivo.write('Linha 2\n')
arquivo.write('Linha 3\n')


arquivo.seek(0, 0)  # colocou o cursor para a posição inicial do arquivo
# (2, 0) começar do segundo caracter em diante
# (0, 1 - Python Orientado a Objetos) o 1 - Python Orientado a Objetos é relativo a posição em que o cursor está naquele momento
# (0, 2) 2 é relativa a posição final do arquivo
print('Lendo linhas')
print(arquivo.read())
print('###########')

arquivo.seek(0, 0)  # voltou o cursor para o começo do arquivo
print(arquivo.readline(), end='')
print(arquivo.readline(), end='')
print(arquivo.readline(), end='')
print('###########')

arquivo.seek(0, 0)
print(arquivo.readlines())
#   OU
'''for linha in arquivo.readlines():
    print(linha, end='')'''

arquivo.close()

'''try:
    file = open('87a-abc.txt', 'w+')
    file.write('Linha')
    file.seek(0, 0)
    print(file.read())
finally:
    file.close()'''

with open('87b-abc.txt', 'w+') as file:
    file.write('Linha 1 - Python Orientado a Objetos\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')
    file.seek(0)
    print(file.read())

#import os
#os.remove('abc.txt')    # para excluir o arquivo
