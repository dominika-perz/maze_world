import unittest
from helper import *
from solvers import SimpleSolver
from maze_generators import simple_generator_5x5
import world


class WorldTest(unittest.TestCase):
    def test_simple_world(self):
        self.world = world.World(simple_generator_5x5, SimpleSolver)
        self.assertEqual(self.world._maze.start_pos, self.world._position)
        self.assertTrue(self.world.solve_maze())
        self.assertEqual(self.world._maze.end_pos, self.world._position)
        self.assertTrue(self.world._maze.is_end(self.world._position))

    def test_unsolvable_maze(self):
        def unsolvable_maze():
            maze = [[Legend.START, Legend.WALL, Legend.END, Legend.WALL],
                    [Legend.CORRIDOR, Legend.CORRIDOR, Legend.WALL, Legend.CORRIDOR],
                    [Legend.CORRIDOR, Legend.WALL, Legend.WALL, Legend.CORRIDOR],
                    [Legend.CORRIDOR, Legend.CORRIDOR, Legend.CORRIDOR, Legend.CORRIDOR],
                    ]
            return Position(0, 0), Position(3, 3), maze

        self.world = world.World(unsolvable_maze, SimpleSolver)
        self.assertEqual(self.world._maze.start_pos, self.world._position)
        self.assertFalse(self.world.solve_maze())


if __name__ == '__main__':
    unittest.main()
