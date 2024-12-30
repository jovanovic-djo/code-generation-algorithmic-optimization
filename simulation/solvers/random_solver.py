import pygame
import time
import random
from datetime import datetime
from src.game import SnakeGame
from assets.utils import log_to_csv

class RandomSolver:
    def __init__(self, game, initial_speed=100000):
        self.game = game
        self.game.snake_speed = initial_speed
        
        # Movement parameters
        self.directions = ["UP", "RIGHT", "DOWN", "LEFT"]
        self.current_direction = None
        
        # Metrics tracking
        self.moves_count = 0
        self.start_time = time.time()
        self.end_time = None
        self.success = False
        self.finished = False
        self.initial_speed = initial_speed
        self.current_speed = initial_speed
        self.direction_changes = 0

    def change_speed(self, new_speed):
        self.current_speed = new_speed
        self.game.snake_speed = new_speed

    def get_metrics(self):
        """Collect metrics for CSV logging"""
        self.end_time = time.time()
        solving_time = self.end_time - self.start_time
        
        return {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'solver_type': 'random',
            'total_moves': self.moves_count,
            'time': round(solving_time, 2),
            'finished': "False" if self.finished else "True",
            'turns': self.direction_changes
        }

    def choose_direction(self):
        """Choose a random direction that isn't opposite to current direction"""
        current_dir = self.game.snake.direction
        
        if current_dir == "UP":
            valid_dirs = ["UP", "LEFT", "RIGHT"]
        elif current_dir == "DOWN":
            valid_dirs = ["DOWN", "LEFT", "RIGHT"]
        elif current_dir == "LEFT":
            valid_dirs = ["LEFT", "UP", "DOWN"]
        elif current_dir == "RIGHT":
            valid_dirs = ["RIGHT", "UP", "DOWN"]
        else:
            valid_dirs = self.directions
            
        new_direction = random.choice(valid_dirs)
        if new_direction != current_dir:
            self.direction_changes += 1
        return new_direction

    def solve(self):
        if self.game.snake.direction is None:
            self.game.snake.direction = random.choice(self.directions)
        
        # Randomly change direction (20% chance each move)
        if random.random() < 0.2:
            self.game.snake.direction = self.choose_direction()
        
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
    solver = RandomSolver(game)
    
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
    time.sleep(1)  # Small delay between tests

if __name__ == "__main__":
    main()