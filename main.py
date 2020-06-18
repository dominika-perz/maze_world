from world import *
from maze.maze_generators import *
from solvers.solvers import *


if __name__ == '__main__':
    world = World(simple_generator_5x5, SimpleSolver)
    print(world)
    world.solve_maze()
