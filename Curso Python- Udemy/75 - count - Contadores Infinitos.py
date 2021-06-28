from itertools import count

contador = count() # cria um contador infinito, cuidado ao executálo para não travar a máquina
contador2 = count(start=20, step=2)  # começa a contar do 20 em passo 2
contador3 = count(start=5, step=0.2)
# contador4 = count(start=9, step=-1 - Python Orientado a Objetos) para fazer um contador de negativos

print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))

for valor in contador3:
    print(round(valor, 2), end=', ')

    if valor > 10:
        break
print()

cont = count()   # utilizou um contador para definir indices a uma lista
lista = ['Luiz', 'João', 'Mateus', 'Maria', 'Júlia']
lista = zip(cont, lista)
print(list(lista))
