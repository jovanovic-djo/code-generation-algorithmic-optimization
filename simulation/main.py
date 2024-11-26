from solvers import spiral_solver
from src.game import SnakeGame

if __name__ == "__main__":
    game = SnakeGame()
    
    spiral_solver.run_spiral_solver(game)
    
    game.show_game_over()
