from maze.maze_generators import *


class Maze:
    def __init__(self, size):
        self.size = size
        self.maze = SimpleGenerator.generate()

    def __str__(self):
        return str(self.maze)

    def __repr__(self):
        return f'{self.__class__}({self.size})'

    def isWall(self, pos):
        x, y = pos
        if x < 0 or x >= self.size:
            return True
        if y < 0 or y >= self.size:
            return True
        return self.maze[x][y] == Legend.WALL

    def isEnd(self, pos):
        x, y = pos
        return self.maze[x][y] == Legend.END


