import random
import pygame

class RandomSolver:
    def __init__(self, game, max_moves=10000):
        self.game = game
        self.max_moves = max_moves
        self.moves_count = 0
        
        self.directions = ["UP", "DOWN", "LEFT", "RIGHT"]

    def choose_direction(self):
        current_dir = self.game.snake.direction
        
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
        if self.game.snake.direction is None:
            self.game.snake.direction = random.choice(self.directions)
        
        self.game.snake.direction = self.choose_direction()
        
        self.game.snake.move()
        
        self.moves_count += 1
        
        if self.moves_count >= self.max_moves:
            self.game.running = False

def run_solver(game):

    solver = RandomSolver(game)
    
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                break
        
        solver.solve()
        
        game.update()
        game.draw()
        
        if not game.running:
            break
