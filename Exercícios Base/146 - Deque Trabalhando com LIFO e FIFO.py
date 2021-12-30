"""
Pilhas e filas
Pilha (stack) - LIFO - last in, frist out.
       Exemplo: Pilha de livros que são adicionados um sobre o outro
Fila (queue) - FIFO - first in, first out.
       Exemplo: Uma fila de banco (ou qualquer fila da vida real)
Filas podem ter efeitos colaterais em desempenho, porque a cada item
alterado, todos os índices serão modificados.

"""

from time import sleep
from collections import deque

print('=='*70)

fila = deque()
fila .append('João')
fila .append('Maria')
fila .append('José')
fila .append('Marcos')
fila .append('Danilo')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')

for nome in fila:
    print(nome)

print('=='*70)

fila1 = deque(maxlen=5)
fila1.extend([1, 2, 3, 4])
fila1.append(5)
fila1.append(6)
fila1.append(7)

print(fila1)

print('=='*70)

fila3 = deque(maxlen=10)
fila3.extend([10, 20, 30, 40, 50, 60, 70, 80])
fila3.insert(2, 'Mateus')
print(fila3.index(50))
print(fila3)

print('=='*70)

fila2 = deque(maxlen=10)

for i in range(100):
    fila2.append(i)
    sleep(1)
    print(fila2)
