import time

from maze import *
from helper import *
from tkinter import *


class World:
    def __init__(self, generator, solver):
        self._maze = Maze(generator)
        self._solver = solver()
        self._position = self._maze.start_pos

    def __str__(self):
        world_str = 'Maze World\n'
        world_str += str(self._maze)
        world_str += '\nCurrent position: '
        world_str += str(self._position)
        return world_str

    def __repr__(self):
        # TODO: Add repr() func for World class
        pass

    @property
    def position(self):
        return self._position

    def show_world(self):
        current_world = ''
        for r in self.rows:
            for c in self.cols:
                current_world += self.__getitem__(Position(r, c))
                current_world += ' '
            current_world += '\n'
        print(current_world)

    def solve_maze(self, labels=None):
        while not self._maze.is_end(self._position):
            shift = self._solver.next_move()
            if not shift:
                print('This maze is unsolvable!')
                return False
            new_pos = self._maze.start_pos + shift
            # print(f'New position: {new_pos}')
            if not self._maze.is_wall(new_pos):
                time.sleep(.3)
                self.update(new_pos, labels)
                # self.show_world()
        print('Maze solved. Congrats!')
        return True

    def update(self, new_pos, labels=None):
        self._solver.update()
        if labels:
            prev_label = labels[self._position.x][self._position.y]
            if self._position == self._maze.start_pos:
                prev_label.config(bg=Legend.color[Legend.START])
            else:
                prev_label.config(bg=Legend.color[Legend.VISITED])
            labels[new_pos.x][new_pos.y].config(bg=Legend.color[Legend.AGENT])
        self._position = new_pos

    @property
    def rows(self):
        return range(self._maze.height)

    @property
    def cols(self):
        return range(self._maze.width)

    def __getitem__(self, key):
        return Legend.AGENT if key == self._position else self._maze[key]

    def reset(self):
        self._solver.reset()
        self._position = self._maze.start_pos

