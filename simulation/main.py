from solvers import spiral_solver, zigzag_solver, random_solver
from src.game import SnakeGame

if __name__ == "__main__":

    for _ in range(3):
        game = SnakeGame()
        try:
            zigzag_solver.run_solver(game)
        finally:
            game.show_game_over()
    
    for _ in range(3):
        game = SnakeGame()
        try:
            random_solver.run_solver(game)
        finally:
            game.show_game_over()

    for _ in range(3):
        game = SnakeGame()
        try:
            spiral_solver.run_solver(game)
        finally:
            game.show_game_over()


    

