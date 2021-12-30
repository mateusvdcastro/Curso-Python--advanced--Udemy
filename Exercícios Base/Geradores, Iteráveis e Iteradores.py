# list, str and tuples - they are iterables
lista = [1, 2, 3, 4]
lista2 = 12345
lista3 = iter(lista)   # torna a lista um iterador

print(hasattr(lista, '__iter__'))
print(hasattr(lista2, '__iter__'))  # verificando se estes valores são iteráveis
print(hasattr(lista, '__next__'))   # o método next está verificando se a lista é um iterador 
print(hasattr(lista3, '__next__'))

print(next(lista3))
print(next(lista3))
print(next(lista3))
print(next(lista3))
print('-'*30)
nome = 'Mateus Castro'
gerador = iter(nome)
print(next(gerador))
print(next(gerador))        # este processo é completamente otimizado pela função for
print(next(gerador))
print(next(gerador))
print(next(gerador))

# Geradores são usados para códigos que sejam pesados e levam tempo para serem processados
import sys
import time
l1 = [x for x in range(100000)]
l2 = (x for x in range(100000))  # perceba que o type() retornou gerador, ou seja, esta é uma forma de criar um gerador
print(type(l1))
print(type(l2))
print(sys.getsizeof(l1))   # pega o tamanho dos códigos, em bytes
print(sys.getsizeof(l2))   # perceba que a lista l1 e o gerador l2 são iguais, porém seu ttamanho são completamente
# diferentes, pois as listas salvam todos os dados na memória e os geradores não, ele irá te exibir o nº desejado
# usando o método next() como mostrado acima

def gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)   # para simular um código pesado e seu tempo até terminar
    return r
def gera1():
    for n in range(100):
        yield n
        time.sleep(0.1)
g = gera()
for v in g:
    print(v, end='')  # note que a def gera() espera toda a lista ser preenchida para exibir as informações
h = gera1()           # e a def gera1() exibe antes mesmo da conclusão, podendo ser útil
print()
for v1 in h:
    print(v1, end='')
print()
print(next(gera1()))

# exercício
carrinho = []
carrinho.append(('Produto', 30.5))
carrinho.append(('Produto', '20'))
carrinho.append(('Produto', 50))

l1 = sum([float(produto[1]) for produto in carrinho])
print(l1)
