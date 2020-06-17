from helper import Legend


class MazeGenerator:
    def __init__(self, size):
        self.size = size

    def generate(self):
        pass


class SimpleGenerator(MazeGenerator):
    def __init__(self):
        self.size = 5

    @staticmethod
    def generator(self):
        maze = [[Legend.START, Legend.WALL, Legend.WALL, Legend.CORRIDOR, Legend.CORRIDOR],
                [Legend.CORRIDOR, Legend.CORRIDOR, Legend.WALL, Legend.CORRIDOR, Legend.WALL],
                [Legend.CORRIDOR, Legend.WALL, Legend.WALL, Legend.CORRIDOR, Legend.WALL],
                [Legend.CORRIDOR, Legend.WALL, Legend.CORRIDOR, Legend.CORRIDOR, Legend.CORRIDOR],
                [Legend.CORRIDOR, Legend.CORRIDOR, Legend.CORRIDOR, Legend.WALL, Legend.END],
                ]
        return maze

