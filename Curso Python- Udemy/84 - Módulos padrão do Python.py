# Veja os módulos padrão do Python:
# https://docs.python.org/3/library/cgi.html#module-cgi
# clique em ctrl + spacebar para ver as outras funções de um módulo

from sys import platform as so
print(so)  # saber em que plataforma o Python está rodando (Windows, Linux, Mac ...)

from random import randint, random

'''def randint(*args):
        return 'hahaha'''  # cuidado para não sobrescrever a função em código grande

for i in range(10):
    print(randint(0, 20), end=', ')
print(random(), end=', ')

