from helper import *


class Solver:
    def __init__(self):
        pass

    def next_move(self):
        pass


class SimpleSolver(Solver):
    def __init__(self):
        self._visited = set()
        self._to_go = [Position(0, 0)]
        self._position = None

    def __str__(self):
        to_go_str = '['
        for pos in self._to_go:
            to_go_str += str(pos) + ', '
        to_go_str = to_go_str[:-2] + ']'
        visited_str = '{'
        for pos in self._visited:
            visited_str += str(pos) + ', '
        visited_str = visited_str[:-2] + '}'
        return f'''Initial position: (0, 0)
                    Current position: {self._position}
                    Visited: {self._visited}
                    To go: ''' + to_go_str

    def __repr__(self):
        return f'''s = {self.__class__.__name__}()
                    s._visited = {self._visited}
                    s._to_go = {self._to_go}
                    s._position = ''' + repr(self._position)

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

    def reset(self):
        self.__init__()

