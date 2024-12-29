import pygame
import time
import csv
from datetime import datetime

class SpiralSolver:
    def __init__(self, game, snake_speed=10):
        self.game = game
        self.snake_speed = snake_speed
        
        # Spiral movement parameters
        self.directions = ["UP", "RIGHT", "DOWN", "LEFT"]
        self.current_dir_index = 0
        self.steps_in_current_dir = 1
        self.steps_taken = 0
        self.total_steps_in_dir = 0
        self.turn_count = 1
        
        # Metrics tracking
        self.moves_count = 0
        self.start_time = None
        self.end_time = None
        self.success = False
        self.total_distance = 0
        self.prev_pos = None

    def manhattan_distance(self, pos1, pos2):
        """Calculate Manhattan distance between two points"""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def solve(self):
        # Start timing on first move
        if self.start_time is None:
            self.start_time = time.time()
            self.prev_pos = self.game.snake.position.copy()

        # Initialize first direction
        if self.game.snake.direction is None:
            self.game.snake.direction = self.directions[self.current_dir_index]

        # Spiral movement logic
        if self.steps_taken >= self.steps_in_current_dir:
            self.steps_taken = 0
            self.current_dir_index = (self.current_dir_index + 1) % 4
            self.game.snake.direction = self.directions[self.current_dir_index]
            self.turn_count += 1

            if self.turn_count % 2 == 0:
                self.total_steps_in_dir += 1

            self.steps_in_current_dir = self.total_steps_in_dir

        # Update metrics before moving
        current_pos = self.game.snake.position
        self.total_distance += self.manhattan_distance(self.prev_pos, current_pos)
        self.prev_pos = current_pos.copy()
        
        # Make move and update counters
        self.steps_taken += 1
        self.moves_count += 1

        # Check if apple is found
        if self.game.snake.position == self.game.apple.position:
            self.success = True
            self.end_time = time.time()

    def get_metrics(self):
        """Return metrics for the solving attempt"""
        solving_time = self.end_time - self.start_time if self.end_time else time.time() - self.start_time
        final_distance = self.manhattan_distance(
            self.game.snake.position,
            self.game.apple.position
        )
        
        return {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'solver_type': 'spiral',
            'success': self.success,
            'moves': self.moves_count,
            'time_taken': round(solving_time, 2),
            'snake_speed': self.snake_speed,
            'total_distance': self.total_distance,
            'final_distance': final_distance,
            'grid_width': self.game.A,
            'grid_height': self.game.B,
            'turns': self.turn_count
        }

def log_metrics(metrics, filename='solver_metrics.csv'):
    """Log metrics to CSV file"""
    file_exists = False
    try:
        with open(filename, 'r') as f:
            file_exists = True
    except FileNotFoundError:
        pass
    
    with open(filename, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=metrics.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(metrics)

def run_spiral_solver(game, snake_speed=10):
    """Run the spiral solver with specified snake speed"""
    solver = SpiralSolver(game, snake_speed=snake_speed)
    clock = pygame.time.Clock()
    
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                break
        
        solver.solve()
        game.update()
        game.draw()
        
        # Control snake speed
        clock.tick(snake_speed)
        
        if not game.running:
            # Log metrics before closing
            metrics = solver.get_metrics()
            log_metrics(metrics)
            break

def main():
    from src.game import SnakeGame  # Import your game class
    
    game = SnakeGame()
    run_spiral_solver(game, snake_speed=10)  # Adjust speed as needed
    game.show_game_over()
    pygame.quit()

if __name__ == "__main__":
    main()