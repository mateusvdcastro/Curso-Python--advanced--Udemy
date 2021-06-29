

x: int = 10
y: float = 9.5
z: dict = {}


def funcao(p1: int, p2: float, p3: dict):
    """

    :param p1: mostrar que o : é utilizado para definir o tipo de uma variável
    :param p2: mostrar que o : é utilizado para definir o tipo de uma variável
    :param p3: mostrar que o : é utilizado para definir o tipo de uma variável
    :return:
    """
    return print(f'{p1}{p2}{p3}')


def qualquer() -> float:                      # consigo desta forma definir o tipo de variável retornada
    return 10.5


from typing import Union


def qualquer_outra() -> Union[dict, float]:         # consigo definir mais de um tipo de retorno para uma variável
    return {}


print(type(qualquer()))
