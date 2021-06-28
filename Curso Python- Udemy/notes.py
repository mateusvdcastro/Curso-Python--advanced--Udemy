idade = '''idade'''
print(type(idade))

nome = 'Mateus'
idade = 18
peso = 62
print('{0} {2} {0} {1} {2} {1}'.format(nome, idade, peso))  # format(0, 1 - Python Orientado a Objetos, 2)
print('{n} {p} {n} {i} {p} {i}'.format(n=nome, i=idade, p=peso))

print('"Já sei!"')

variavel = '5.5'
outra_variavel = (int(float(variavel)))
print(outra_variavel)

valor = False
if valor:
    ...   # isso se chama Ellipsis, pode se usar aqui tbm o "Pass"
else:
    print('Tchau')

# a troca de um tipo Int para para uma float por exemplo se chama "Type Cast"

'''começa_com = ['Mateus', 'João', 'Alicate', 'Ponte']
começa = False
p = str(input('Começa com?: '))
for palavra in começa_com:
    if palavra.lower().startswith(f'{p}'):
        começa = True
if começa == True:
    print(f'Há uma palavra que começa com {p}')
else:
    print(f'Não há palavra que comece com {p}')'''

nomes = ['Luiz', 'Maria', 'José', 1, 2, 3, 4, 5, 60]
n1, n2, n3, *outra_lista, ultimo = nomes
print(n3, outra_lista, ultimo)

x = 10
y = 'Luiz'
z = 5
x, y, z = z, y, x    # podemos trocar variáveis simplesmente assim
print(f'x={x}, y={y}, z={z}')

'''nome = str(input('Digite um nome: ')).strip()
print(nome or 'Você não digitou nada!')'''

lista = [
    ['P1', 150],
    ['P2', 56],
    ['P3', 15],
    ['P4', 0.5],
    ['P5', 350]
]
# ordenou do maior para o menor
print(sorted(lista, key=lambda item: item[1], reverse=True))
