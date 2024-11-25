from src.game import SnakeGame
# from solvers.zigzag_solver import ZigzagSolver
# from solvers.spiral_solver import SpiralSolver
from solvers.base_solver import BaseSolver
import threading

def run_solver(solver_class):
    game = SnakeGame()
    solver = solver_class(game)
    
    solver_thread = threading.Thread(target=solver.solve)
    solver_thread.start()
    
    game.run()

if __name__ == "__main__":
    run_solver(BaseSolver)