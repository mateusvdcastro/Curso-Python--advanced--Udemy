# conhecimento básico sobre estrutura de dados
# aqui estamos recriando as listas em python

class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def __getitem__(self, index):
        return self.__items[index]

    def __setitem__(self, index, valor):  # setitem para conseguir alterar oq estiver dentro de []
        if index >= len(self.__items):
            self.__items.append(valor)
        self.__items[index] = valor

    def __delitem__(self, index):
        del self.__items[index]

    def add(self, valor):
        self.__items.append(valor)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        return f'{self.__class__.__name__}({self.__items})'


if __name__ == "__main__":
    lista = MinhaLista()
    lista.add('Luiz')
    lista.add('Maria')

    #print(next(lista))
    #print(next(lista))

    lista[0] = 'João'
    lista[2] = 'Ana Maria'
    lista[3] = 'Wagner'

    del lista[3]

    print(f'Só funciona por causa da def getitem--> {lista[0]}')

    for valor in lista:
        print(valor)
