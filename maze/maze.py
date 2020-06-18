from helper import *


class Maze:
    def __init__(self, size, generator):
        self.width = size
        self.height = size
        self.start_pos, self.end_pos, self.maze = generator()

    def __str__(self):
        maze_str = ''
        for rows in self.maze:
            maze_str += str(rows)
            maze_str += '\n'
        return maze_str

    def __repr__(self):
        return f'{self.__class__}({self.width}x{self.height})'

    def __getitem__(self, key):
        return self.maze[key.x][key.y]

    def is_wall(self, pos):
        if pos.x < 0 or pos.x >= self.height:
            return True
        if pos.y < 0 or pos.y >= self.width:
            return True
        return self.maze[pos.x][pos.y] == Legend.WALL

    def is_end(self, pos):
        return self.maze[pos.x][pos.y] == Legend.END




