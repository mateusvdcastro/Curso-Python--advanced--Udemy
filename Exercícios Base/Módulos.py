import math

pi = math.pi


def dobra_lista(lista):
    return [x*2 for x in lista]


def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r

print(__name__)


if __name__ == '__main__':  # isso faz com que os códigos abaixo não sejam executados caso este módulo seja importado
    lista = [1, 2, 3, 4, 5, 6]  # como podemos ver em '85 - Como criar módulos'
    print(multiplica(lista))
    print(pi)
