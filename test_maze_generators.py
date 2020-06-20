import unittest
from helper import *
import maze_generators


class GeneratorTest(unittest.TestCase):
    def test_simple_generator(self):
        start, end, simple_maze = maze_generators.simple_generator_5x5()
        self.assertEqual(len(simple_maze), 5)
        self.assertEqual(len(simple_maze[0]), 5)

        self.assertEqual(start, Position(0, 0))
        self.assertEqual(simple_maze[start.x][start.y], Legend.START)

        self.assertEqual(end, Position(4, 4))
        self.assertEqual(simple_maze[end.x][end.y], Legend.END)


if __name__ == '__main__':
    unittest.main()
