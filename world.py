from maze.maze import *
from helper import *


class World:
    def __init__(self, generator, solver):
        self._maze = Maze(5, generator)
        self._solver = solver()
        self._position = self._maze.start_pos

    def __str__(self):
        world_str = 'Maze World\n'
        world_str += str(self._maze)
        world_str += '\nCurrent position: '
        world_str += str(self._position)
        return world_str

    def __repr__(self):
        pass

    @property
    def position(self):
        return self._position

    def show_world(self):
        current_world = ''
        for r in range(self._maze.width):
            for c in range(self._maze.height):
                if Position(r, c) == self._position:
                    current_world += Legend.AGENT
                else:
                    current_world += self._maze[Position(r, c)]
                current_world += ' '
            current_world += '\n'
        print(current_world)

    def solve_maze(self):
        while not self._maze.is_end(self._position):
            new_pos = self._maze.start_pos + self._solver.next_move()
            print(f'New position: {new_pos}')
            if not new_pos:
                print('This maze is unsolvable!')
                return False
            if not self._maze.is_wall(new_pos):
                self._solver.update()
                self._position = new_pos
                self.show_world()
        print('Maze solved. Congrats!')
        return True

