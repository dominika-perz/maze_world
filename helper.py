from heapq import *


class Legend:
    WALL = 'x'
    START = '>'
    END = '!'
    CORRIDOR = '_'
    AGENT = 'o'
    VISITED = '-'

    color = {WALL: "#444444",
             START: "#c76dc3",
             END: "#983a94",
             CORRIDOR: "#ececec",
             AGENT: "#84d6e0",
             VISITED: "#f2def1"
             }


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Position(x, y)

    def __str__(self):
        return f'P({self.x}, {self.y})'

    def __repr__(self):
        return f'Position({self.x}, {self.y})'

    def __hash__(self):
        return hash(self.x+self.y)

    def __eq__(self, other):
        eq_x = self.x == other.x
        eq_y = self.y == other.y
        return eq_x and eq_y

    def __lt__(self, other):
        return self.x + self.y < self.y == other.y

    def __le__(self, other):
        return self.x + self.y <= self.y == other.y

    def __gt__(self, other):
        return self.x + self.y > self.y == other.y

    def __ge__(self, other):
        return self.x + self.y >= self.y == other.y


MOVES = {'UP': Position(-1, 0),
         'RIGHT': Position(0, 1),
         'DOWN': Position(1, 0),
         'LEFT': Position(0, -1)}


class PriorityQueue:
    def __init__(self):
        self._min_heap = []
        heapify(self._min_heap)
        self._dict = {}

    def pop(self):
        priority, item = heappop(self._min_heap)
        del self._dict[item]
        return priority, item

    def push(self, priority, item):
        if item in self._dict:
            old_priority = self._dict[item]
            if old_priority > priority:
                for idx, items in enumerate(self._min_heap):
                    p_, i_ = items
                    if i_ == item and p_ == old_priority:
                        del self._min_heap[idx]
                        break
                heapify(self._min_heap)
                heappush(self._min_heap, (priority, item))
                self._dict[item] = priority
        else:
            heappush(self._min_heap, (priority, item))
            self._dict[item] = priority

    def __len__(self):
        return len(self._min_heap)


