import unittest
import solvers
from helper import *


class SimpleSolverTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = solvers.SimpleSolver()

    def test_init(self):
        self.assertIsInstance(self.solver, solvers.Solver)
        self.assertIsInstance(self.solver, solvers.SimpleSolver)

        self.assertEqual(self.solver._position, None)
        self.assertIn(Position(0, 0), self.solver._to_go)

    def test_printing(self):
        sol_str = ('''Initial position: (0, 0)
                    Current position: None
                    Visited: set()
                    To go: [P(0, 0)]''')
        self.assertEqual(str(self.solver), sol_str)

        sol_repr = ('''s = SimpleSolver()
                    s._visited = set()
                    s._to_go = [Position(0, 0)]
                    s._position = None''')
        self.assertEqual(repr(self.solver), sol_repr)

    def test_next_move(self):
        self.assertEqual(self.solver.next_move(), Position(0, 0))
        self.assertEqual(self.solver._position, Position(0, 0))
        self.assertIn(self.solver._position, self.solver._visited)
        self.assertEqual(self.solver.next_move(), None)

    def test_update(self):
        self.solver.next_move()
        self.solver.update()
        self.assertIn(Position(-1, 0), self.solver._to_go)
        self.assertIn(Position(0, 1), self.solver._to_go)
        self.assertEqual(self.solver.next_move(), Position(0, -1))
        self.solver.update()
        self.assertEqual(self.solver.next_move(), Position(0, -2))


if __name__ == '__main__':
    unittest.main()
