import pygame

class ZigZagSolver:
    def __init__(self, game):
        self.game = game
        
        self.is_moving_right = True
        self.current_vertical_direction = "DOWN"
        self.steps_in_current_row = 1
        self.steps_taken_in_row = 0
        self.rows_completed = 0
        self.max_grid_size = 1000

    def solve(self):
        if self.game.snake.direction is None:
            self.game.snake.direction = "RIGHT"
        
        if self.is_moving_right:
            self.game.snake.direction = "RIGHT"
        else:
            self.game.snake.direction = "LEFT"
        
        self.game.snake.move()
        self.steps_taken_in_row += 1
        
        if self.steps_taken_in_row >= self.steps_in_current_row:
            self.steps_taken_in_row = 0
            
            self.current_vertical_direction = "DOWN" if self.current_vertical_direction == "UP" else "UP"
            self.game.snake.direction = self.current_vertical_direction
            
            self.game.snake.move()
            
            self.is_moving_right = not self.is_moving_right
            
            self.rows_completed += 1
            self.steps_in_current_row += 1
        
        if self.rows_completed >= self.max_grid_size:
            self.game.running = False

def run_solver(game):
    solver = ZigZagSolver(game)
    
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
