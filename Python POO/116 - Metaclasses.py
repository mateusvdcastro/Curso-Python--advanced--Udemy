"""
EM PYTHON TUDO É UM OBJETO: Incluindo classes
Metaclasses são as "classes" que criam classes.
type é uma metaclasse
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        if 'b_fala' not in namespace:
            print(f'Oi, você precisa criar o método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método, não atributo em {name}')

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()


class B(A):
    teste = 'Valor'

    def b_fala(self):
        print('Oi')

    def sei_la(self):
        pass

