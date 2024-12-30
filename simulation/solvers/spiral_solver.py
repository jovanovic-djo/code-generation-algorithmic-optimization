import pygame
import time
from datetime import datetime
from src.game import SnakeGame
from assets.utils import log_to_csv

class SpiralSolver:
    def __init__(self, game, initial_speed=300):
        self.game = game
        self.game.snake_speed = initial_speed
        
        # Spiral movement parameters
        self.directions = ["UP", "RIGHT", "DOWN", "LEFT"]
        self.current_dir_index = 0
        self.steps_in_current_dir = 1
        self.steps_taken = 0
        self.total_steps_in_dir = 0
        self.turn_count = 1
        
        # Metrics tracking
        self.moves_count = 0
        self.start_time = time.time()
        self.end_time = None
        self.success = False
        self.finished = False  # New flag for completion status
        self.initial_speed = initial_speed
        self.current_speed = initial_speed

    def change_speed(self, new_speed):
        self.current_speed = new_speed
        self.game.snake_speed = new_speed

    def get_metrics(self):
        """Collect metrics for CSV logging"""
        self.end_time = time.time()
        solving_time = self.end_time - self.start_time
        
        return {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'solver_type': 'spiral',
            'total_moves': self.moves_count,
            'time': round(solving_time, 2),
            'finished': "False" if self.finished else "True",
            'turns': self.turn_count
        }

    def solve(self):
        if self.game.snake.direction is None:
            self.game.snake.direction = self.directions[self.current_dir_index]

        if self.steps_taken >= self.steps_in_current_dir:
            self.steps_taken = 0
            self.current_dir_index = (self.current_dir_index + 1) % 4
            self.game.snake.direction = self.directions[self.current_dir_index]
            self.turn_count += 1

            if self.turn_count % 2 == 0:
                self.total_steps_in_dir += 1

            self.steps_in_current_dir = self.total_steps_in_dir

        self.steps_taken += 1
        self.moves_count += 1
        
        # Check if apple is found
        if self.game.snake.position == self.game.apple.position:
            self.success = True
            self.finished = True
            self.end_time = time.time()
        
        # Check if maximum moves reached
        if self.moves_count >= self.game.A * self.game.B * 35:  # Using your original limit
            self.finished = True
            self.success = False
            self.end_time = time.time()

def run_solver(game):
    solver = SpiralSolver(game)
    
    current_speed_index = 0
    
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                solver.finished = True  # Mark as finished if manually quit
                break
        
        solver.solve()
        game.update()
        game.draw()
        
        if not game.running or solver.finished:
            # Log metrics before closing
            metrics = solver.get_metrics()
            log_to_csv(metrics)
            break

def main():
    
    # Run multiple tests with different speed profiles
        game = SnakeGame()
        run_solver(game)
        pygame.quit()
        time.sleep(1)  # Small delay between tests

if __name__ == "__main__":
    main()