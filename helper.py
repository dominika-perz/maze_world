from collections import namedtuple


class Legend:
    WALL = 'x'
    START = '>'
    END = '!'
    CORRIDOR = '_'


Position = namedtuple('Position', ['x', 'y'])


class Moves:
    UP = Position(-1, 0)
    DOWN = Position(1, 0)
    RIGHT = Position(0, 1)
    LEFT = Position(0, -1)

