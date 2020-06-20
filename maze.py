from helper import *


class Maze:
    def __init__(self, generator, width=-1, height=-1):
        self.start_pos, self.end_pos, self.maze = generator()
        self.width = width if width > 0 else len(self.maze)
        self.height = height if height > 0 else len(self.maze[0])

    def __str__(self):
        maze_str = ''
        for row in self.maze:
            for cell in row:
                maze_str += cell
                maze_str += ' '
            maze_str += '\n'
        return maze_str

    def __repr__(self):
        return f'{self.__class__.__name__}({self.width}, {self.height})'

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




