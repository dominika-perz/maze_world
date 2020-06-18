from collections import namedtuple


class Legend:
    WALL = 'x'
    START = '>'
    END = '!'
    CORRIDOR = '_'
    AGENT = 'o'


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Position(x, y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __hash__(self):
        return hash(self.x+self.y)

    def __eq__(self, other):
        eq_x = self.x == other.x
        eq_y = self.y == other.y
        return eq_x and eq_y


MOVES = {'UP': Position(-1, 0),
         'RIGHT': Position(0, 1),
         'DOWN': Position(1, 0),
         'LEFT': Position(0, -1)}


# class State:
#     def __init__(self, initial_pos):
#         self.position = initial_pos
#         self.maze = [Legend.START]
#
#     def __str__(self):
#         state_str = ''
#         for rows in self.maze:
#             state_str += str(rows)
#             state_str += '\n'
#         return state_str

