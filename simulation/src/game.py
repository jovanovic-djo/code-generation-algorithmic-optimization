import pygame
import random
from src.snake import Snake
from src.apple import Apple
from src.grid import Grid
import os

class SnakeGame:
    def __init__(self):
        pygame.init()
        
        # Get the display info
        display_info = pygame.display.Info()
        SCREEN_WIDTH = display_info.current_w
        SCREEN_HEIGHT = display_info.current_h

        self.A = random.randint(1, 1000)
        self.B = random.randint(1, 1000)
        
        self.CELL_SIZE = min(
            (SCREEN_WIDTH - 100) // self.A,
            (SCREEN_HEIGHT - 100) // self.B
        )
        
        # Ensure minimum cell size
        self.CELL_SIZE = max(self.CELL_SIZE, 2)
        
        # Calculate actual screen dimensions based on cell size
        self.SCREEN_WIDTH = self.A * self.CELL_SIZE
        self.SCREEN_HEIGHT = self.B * self.CELL_SIZE
        
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        
        # Center the game window on the screen
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        
        self.clock = pygame.time.Clock()
        
        # Initialize game objects with calculated cell size
        self.grid = Grid(self.A, self.B, self.CELL_SIZE, self.screen)
        self.snake = Snake(self.A, self.B, self.CELL_SIZE)
        self.apple = Apple(self.A, self.B, self.CELL_SIZE)
        
        self.running = True
        self.win = False
        self.snake_speed = 1

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

        self.show_game_over()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.snake.change_direction(event.key)

    def update(self):
        self.snake.move()
        self.snake.teleport()

        if self.snake.position == self.apple.position:
            self.win = True
            self.running = False
        if self.snake.move_count >= self.A * self.B * 35:
            self.running = False

    def draw(self):
        self.screen.fill(self.WHITE)
        self.grid.draw()
        self.apple.draw(self.screen)
        self.snake.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(self.snake_speed)

    def show_game_over(self):
        self.screen.fill(self.WHITE)
        # Scale font size based on cell size
        font_size = max(30, min(50, self.CELL_SIZE * 10))
        font = pygame.font.SysFont(None, font_size)
        text = font.render("W" if self.win else "L", True, self.BLACK)
        text_rect = text.get_rect(center=(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(1000)