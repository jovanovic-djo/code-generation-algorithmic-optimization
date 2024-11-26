from solvers import spiral_solver
from src.game import SnakeGame

if __name__ == "__main__":
    
    for _ in range(3):
        game = SnakeGame()
        try:
            spiral_solver.run_spiral_solver(game)
        finally:
            game.show_game_over()


