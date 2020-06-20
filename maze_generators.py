from helper import *


def simple_generator_5x5():
    maze = [[Legend.START, Legend.WALL, Legend.WALL, Legend.CORRIDOR, Legend.CORRIDOR],
            [Legend.CORRIDOR, Legend.CORRIDOR, Legend.WALL, Legend.CORRIDOR, Legend.WALL],
            [Legend.CORRIDOR, Legend.WALL, Legend.WALL, Legend.CORRIDOR, Legend.WALL],
            [Legend.CORRIDOR, Legend.WALL, Legend.CORRIDOR, Legend.CORRIDOR, Legend.CORRIDOR],
            [Legend.CORRIDOR, Legend.CORRIDOR, Legend.CORRIDOR, Legend.WALL, Legend.END],
            ]

    return Position(0, 0), Position(4, 4), maze


