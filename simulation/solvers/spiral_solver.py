import pygame

class SpiralSolver:
    def __init__(self, game):
        self.game = game
        self.directions = ["UP", "RIGHT", "DOWN", "LEFT"]
        self.current_dir_index = 0
        self.steps_in_current_dir = 1
        self.steps_taken = 0
        self.total_steps_in_dir = 1
        self.turn_count = 0

    def solve(self):
        """
        Implements a spiral solving strategy:
        1. Move in a spiral pattern increasing the spiral size
        2. Change direction after a set number of steps
        3. Increase spiral size after two direction changes
        """
        # If no direction is set, start moving
        if self.game.snake.direction is None:
            self.game.snake.direction = self.directions[self.current_dir_index]
        
        # Change direction if needed
        if self.steps_taken >= self.steps_in_current_dir:
            # Reset steps taken
            self.steps_taken = 0
            
            # Move to next direction
            self.current_dir_index = (self.current_dir_index + 1) % 4
            self.game.snake.direction = self.directions[self.current_dir_index]
            
            # Increment turn count
            self.turn_count += 1
            
            # Increase spiral size after two complete turns
            if self.turn_count % 2 == 0:
                self.total_steps_in_dir += 1
            
            # Update steps for next direction
            self.steps_in_current_dir = self.total_steps_in_dir
        
        # Move snake
        self.game.snake.move()
        self.steps_taken += 1

def run_spiral_solver(game):
    """
    Helper function to run the spiral solver
    """
    solver = SpiralSolver(game)
    
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

