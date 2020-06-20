import unittest
from helper import *
import maze


class MazeTest(unittest.TestCase):
    @staticmethod
    def mock_maze_generator():
        simple_maze = [['>', 'x', 'x', '_', '_'],
                       ['_', '_', 'x', '_', 'x'],
                       ['_', 'x', 'x', '_', 'x'],
                       ['_', 'x', '_', '_', '_'],
                       ['_', '_', '_', 'x', '!'],
                       ]
        return Position(0, 0), Position(4, 4), simple_maze

    def setUp(self) -> None:
        self.simple_maze = maze.Maze(self.mock_maze_generator)

    def test_init(self):
        self.assertIsInstance(self.simple_maze, maze.Maze)

        self.assertEqual(self.simple_maze.width, 5)
        self.assertEqual(self.simple_maze.height, 5)
        self.assertEqual(self.simple_maze.start_pos, Position(0, 0))
        self.assertEqual(self.simple_maze.end_pos, Position(4, 4))

    def test_is_wall(self):
        self.assertTrue(self.simple_maze.is_wall(Position(0, 2)))
        self.assertTrue(self.simple_maze.is_wall(Position(2, 4)))
        self.assertFalse(self.simple_maze.is_wall(Position(3, 2)))
        self.assertFalse(self.simple_maze.is_wall(Position(0, 0)))

    def test_is_end(self):
        self.assertTrue(self.simple_maze.is_end(self.simple_maze.end_pos))
        self.assertFalse(self.simple_maze.is_end(self.simple_maze.start_pos))
        self.assertFalse(self.simple_maze.is_end(Position(2, 4)))
        self.assertFalse(self.simple_maze.is_end(Position(2, 3)))
        self.assertFalse(self.simple_maze.is_end(Position(0, 1)))

    def test_printing(self):
        maze_str = '> x x _ _ \n_ _ x _ x \n_ x x _ x \n_ x _ _ _ \n_ _ _ x ! \n'
        self.assertEqual(str(self.simple_maze), maze_str)
        self.assertEqual(repr(self.simple_maze), 'Maze(5, 5)')

    def test_getitem(self):
        self.assertEqual(self.simple_maze[self.simple_maze.start_pos], Legend.START)
        self.assertEqual(self.simple_maze[self.simple_maze.end_pos], Legend.END)
        self.assertEqual(self.simple_maze[Position(1, 4)], Legend.WALL)
        self.assertEqual(self.simple_maze[Position(4, 1)], Legend.CORRIDOR)


if __name__ == '__main__':
    unittest.main()
