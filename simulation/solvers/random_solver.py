import random
import pygame

class RandomSolver:
    def __init__(self, game, max_moves=10000):
        """
        Initialize the random solver
        
        Args:
            game (SnakeGame): The game instance
            max_moves (int): Maximum number of moves to prevent infinite loops
        """
        self.game = game
        self.max_moves = max_moves
        self.moves_count = 0
        
        # Possible movement directions
        self.directions = ["UP", "DOWN", "LEFT", "RIGHT"]

    def choose_direction(self):
        """
        Randomly choose a direction, avoiding 180-degree turns
        
        Returns:
            str: Chosen direction
        """
        current_dir = self.game.snake.direction
        
        # Prevent 180-degree turns
        if current_dir == "UP":
            valid_dirs = ["UP", "LEFT", "RIGHT"]
        elif current_dir == "DOWN":
            valid_dirs = ["DOWN", "LEFT", "RIGHT"]
        elif current_dir == "LEFT":
            valid_dirs = ["LEFT", "UP", "DOWN"]
        elif current_dir == "RIGHT":
            valid_dirs = ["RIGHT", "UP", "DOWN"]
        elif current_dir is None:
            valid_dirs = self.directions
        
        return random.choice(valid_dirs)

    def solve(self):
        """
        Solve the game using random movements
        """
        # Initialize first move if no direction is set
        if self.game.snake.direction is None:
            self.game.snake.direction = random.choice(self.directions)
        
        # Choose a random direction
        self.game.snake.direction = self.choose_direction()
        
        # Move the snake
        self.game.snake.move()
        
        # Increment move counter
        self.moves_count += 1
        
        # Prevent infinite loops
        if self.moves_count >= self.max_moves:
            self.game.running = False

def run_random_solver(game):
    """
    Helper function to run the random solver
    
    Args:
        game (SnakeGame): The game instance
    """
    solver = RandomSolver(game)
    
    while game.running:
        # Handle pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                break
        
        # Solve the game
        solver.solve()
        
        # Update game state
        game.update()
        game.draw()
        
        # Check for game end conditions
        if not game.running:
            break
