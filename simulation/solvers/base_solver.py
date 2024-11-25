import pygame

class BaseSolver:
    def __init__(self, snake_game):
        self.game = snake_game
        self.moves = []
        self.relative_x = 0
        self.relative_y = 0
        
    def make_move(self, direction):
        if direction == "RIGHT":
            pygame.event.post(pygame.event.Event(pygame.KEYDOWN, 
                            {'key': pygame.K_RIGHT}))
            self.relative_x += 1
        elif direction == "LEFT":
            pygame.event.post(pygame.event.Event(pygame.KEYDOWN, 
                            {'key': pygame.K_LEFT}))
            self.relative_x -= 1
        elif direction == "DOWN":
            pygame.event.post(pygame.event.Event(pygame.KEYDOWN, 
                            {'key': pygame.K_DOWN}))
            self.relative_y += 1
        elif direction == "UP":
            pygame.event.post(pygame.event.Event(pygame.KEYDOWN, 
                            {'key': pygame.K_UP}))
            self.relative_y -= 1
        
        self.moves.append(direction)
    
    def solve(self):
        raise NotImplementedError