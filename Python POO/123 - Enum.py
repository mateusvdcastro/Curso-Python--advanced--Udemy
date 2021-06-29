# usar sempre que houver um grande número de coisas a seres definidas
# neste caso digamos que a gt quer mover o personagem de um jogo

from enum import Enum, auto


class Directions(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()
    corner_right = auto()


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('Cannot move in this direction')

    return f'Moving {direction.name}'


if __name__ == "__main__":
    print(move(Directions.right))
    print(move(Directions.left))
    print(move(Directions.up))
    print(move(Directions.down))
    print(move(Directions.corner_right))

    for direction in Directions:
        print(f' Para entender as variáveis --> '
              f'{direction}, {direction.value}, {direction.name}')
