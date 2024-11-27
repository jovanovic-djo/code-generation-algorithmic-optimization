import pygame

class SpiralSolver:
    def __init__(self, game):
        self.game = game
        self.directions = ["UP", "RIGHT", "DOWN", "LEFT"]
        self.current_dir_index = 0
        self.steps_in_current_dir = 1
        self.steps_taken = 0
        self.total_steps_in_dir = 0
        self.turn_count = 1

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

def run_solver(game):
    solver = SpiralSolver(game)
    
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

