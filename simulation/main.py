from solvers import spiral_solver
from solvers import zigzag_solver
from src.game import SnakeGame

if __name__ == "__main__":

    for _ in range(1):
        game = SnakeGame()
        try:
            zigzag_solver.run_spiral_solver(game)
        finally:
            game.show_game_over()
    
    # for _ in range(1):
    #     game = SnakeGame()
    #     try:
    #         spiral_solver.run_spiral_solver(game)
    #     finally:
    #         game.show_game_over()


    

