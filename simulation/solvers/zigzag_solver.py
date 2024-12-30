import pygame
import time
from datetime import datetime
from src.game import SnakeGame
from assets.utils import log_to_csv

class ZigZagSolver:
    def __init__(self, game, initial_speed=100000, horizontal_steps=1000):
        self.game = game
        self.game.snake_speed = initial_speed
        
        # ZigZag movement parameters
        self.horizontal_steps = horizontal_steps
        self.current_steps = 0
        self.moving_right = True
        self.just_moved_down = False
        
        # Metrics tracking
        self.moves_count = 0
        self.start_time = time.time()
        self.end_time = None
        self.success = False
        self.finished = False
        self.initial_speed = initial_speed
        self.current_speed = initial_speed
        self.turn_count = 0

    def change_speed(self, new_speed):
        self.current_speed = new_speed
        self.game.snake_speed = new_speed

    def get_metrics(self):
        """Collect metrics for CSV logging"""
        self.end_time = time.time()
        solving_time = self.end_time - self.start_time
        
        return {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'solver_type': 'zigzag',
            'total_moves': self.moves_count,
            'time': round(solving_time, 2),
            'finished': "False" if self.finished else "True",
            'turns': self.turn_count
        }

    def solve(self):
        # Initialize direction if None
        if self.game.snake.direction is None:
            self.game.snake.direction = "RIGHT" if self.moving_right else "LEFT"
        
        # Check if we need to move down
        if self.current_steps >= self.horizontal_steps and not self.just_moved_down:
            self.game.snake.direction = "DOWN"
            self.just_moved_down = True
            self.current_steps = 0
            self.moving_right = not self.moving_right  # Switch horizontal direction
            self.turn_count += 1
        
        # After moving down, switch to horizontal movement
        elif self.just_moved_down:
            self.game.snake.direction = "RIGHT" if self.moving_right else "LEFT"
            self.just_moved_down = False
            self.turn_count += 1
        
        # Continue horizontal movement
        self.current_steps += 1
        self.moves_count += 1
        
        # Check if apple is found
        if self.game.snake.position == self.game.apple.position:
            self.success = True
            self.finished = True
            self.end_time = time.time()
        
        # Check if maximum moves reached
        if self.moves_count >= self.game.A * self.game.B * 35:
            self.finished = True
            self.success = False
            self.end_time = time.time()

def run_solver(game):
    solver = ZigZagSolver(game)
    
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                solver.finished = True
                break
        
        solver.solve()
        game.update()
        game.draw()
        
        if not game.running or solver.finished:
            metrics = solver.get_metrics()
            log_to_csv(metrics)
            break

def main():
    game = SnakeGame()
    run_solver(game)
    pygame.quit()
    time.sleep(1)

if __name__ == "__main__":
    main()