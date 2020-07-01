from helper import *


class Solver:
    def __init__(self):
        self._visited = set()
        self._queued = set()
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
        pass

    def reset(self):
        self.__init__()


class DFSSolver(Solver):
    def __init__(self):
        super(DFSSolver, self).__init__()
        self._to_go = [Position(0, 0)]

    def next_move(self):
        if self._to_go:
            self._position = self._to_go.pop()
            self._visited.add(self._position)
            return self._position
        else:
            return None

    def update(self):
        for move in MOVES.values():
            if (self._position + move) not in self._visited | self._queued:
                self._to_go.append(self._position + move)
                self._queued.add(self._position + move)


class BFSSolver(Solver):
    def __init__(self):
        super(DFSSolver, self).__init__()
        self._to_go = [Position(0, 0)]

    def next_move(self):
        if self._to_go:
            self._position = self._to_go.pop(0)
            self._visited.add(self._position)
            return self._position
        else:
            return None

    def update(self):
        for move in MOVES.values():
            if (self._position + move) not in self._visited | self._queued:
                self._to_go.append(self._position + move)
                self._queued.add(self._position + move)


class DijkstraSolver(Solver):
    def __init__(self):
        super(DijkstraSolver, self).__init__()
        self._cost = 0
        self._to_go = PriorityQueue()
        self._to_go.push(0, Position(0, 0))

    def next_move(self):
        if self._to_go:
            self._cost, self._position = self._to_go.pop()
            self._visited.add(self._position)
            return self._position
        else:
            return None

    def update(self):
        for move in MOVES.values():
            if (self._position + move) not in self._visited:
                self._to_go.push(self._cost + 1, self._position + move)

