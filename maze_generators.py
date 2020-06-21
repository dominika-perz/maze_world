from helper import *


def simple_generator_5x5():
    maze = [[Legend.START, Legend.WALL, Legend.WALL, Legend.CORRIDOR, Legend.CORRIDOR],
            [Legend.CORRIDOR, Legend.CORRIDOR, Legend.WALL, Legend.CORRIDOR, Legend.WALL],
            [Legend.CORRIDOR, Legend.WALL, Legend.WALL, Legend.CORRIDOR, Legend.WALL],
            [Legend.CORRIDOR, Legend.WALL, Legend.CORRIDOR, Legend.CORRIDOR, Legend.CORRIDOR],
            [Legend.CORRIDOR, Legend.CORRIDOR, Legend.CORRIDOR, Legend.WALL, Legend.END],
            ]

    return Position(0, 0), Position(4, 4), maze


def simple_generator_10x10():
    maze = [['>', 'x', '_', '_', '_', '_', '_', '_', 'x', '_'],
            ['_', 'x', '_', 'x', 'x', 'x', '_', '_', 'x', '_'],
            ['_', 'x', '_', 'x', '_', 'x', 'x', '_', '_', '_'],
            ['_', 'x', '_', '_', '_', 'x', '_', '_', 'x', 'x'],
            ['_', 'x', '_', 'x', '_', 'x', '_', 'x', 'x', '_'],
            ['_', 'x', '_', 'x', '_', 'x', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', 'x', 'x', 'x', 'x', '_'],
            ['_', 'x', 'x', 'x', '_', 'x', '_', '_', 'x', '_'],
            ['_', '_', '_', 'x', '_', 'x', 'x', '_', 'x', '_'],
            ['_', 'x', 'x', 'x', '_', '_', '_', '_', 'x', '!'],
            ]

    return Position(0, 0), Position(9, 9), maze
