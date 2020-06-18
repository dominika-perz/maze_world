from abc import abstractmethod
from helper import *


class Solver:
    def __init__(self):
        pass

    def __str__(self):
        return str(self.state)


class SimpleSolver(Solver):
    def __init__(self):
        self._visited = set()
        self._to_go = [Position(0, 0)]
        self._position = None

    def __str__(self):
        return super(SimpleSolver, self).__str__()

    def next_move(self):
        if self._to_go:
            self._position = self._to_go.pop()
            self._visited.add(self._position)
            return self._position
        else:
            return None

    def update(self):
        for move in MOVES.values():
            if (self._position + move) not in self._visited:
                self._to_go.append(self._position + move)

