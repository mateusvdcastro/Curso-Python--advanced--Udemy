# https://docs.python.org/3/library/exceptions.html

def divide(n1,n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print(error)
        return False

# note que o segundo Try não rodou, ou seja, caso outro desenvolvedor tente tratar uma def
# que já foi tratada, ele não conseguiria
try:
    print(divide(2, 0))
except:
    print('Erro2')

print('-'*56)


def divide1(n1,n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log: ', error)
        raise  #  com isso você pode relancar uma excessão

try:
    print(divide1(2, 0))
except ZeroDivisionError as error:
    print('Erro2')

print('-'*56)


def divide2(b1, b2):  # com isso você cria sua própria excessão no console
    if b2 == 0:
        raise ValueError("n2 não pode ser 0.")
    return b1/b2

#  print(divide2(b1=2, b2=0)) --  digite só isso e a mensagem aparece no console em vermelho
try:
    print(divide2(b1=2, b2=0))
except ValueError as error:
    print('Você está tentando dividir um número por zero')
    print('Log:', error)
