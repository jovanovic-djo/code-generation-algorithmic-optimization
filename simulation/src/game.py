import pygame
import random
from src.snake import Snake
from src.apple import Apple
from src.grid import Grid

class SnakeGame:
    def __init__(self):
        pygame.init()

        self.A = random.randint(1, 40)
        self.B = random.randint(1, 40)
        self.CELL_SIZE = 20
        self.SCREEN_WIDTH = self.A * self.CELL_SIZE
        self.SCREEN_HEIGHT = self.B * self.CELL_SIZE

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")

        self.clock = pygame.time.Clock()

        self.grid = Grid(self.A, self.B, self.CELL_SIZE, self.screen)
        self.snake = Snake(self.A, self.B, self.CELL_SIZE)
        self.apple = Apple(self.A, self.B, self.CELL_SIZE)

        self.running = True
        self.win = False
        self.snake_speed = 5

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
        font = pygame.font.SysFont(None, 50)
        text = font.render("W" if self.win else "L", True, self.BLACK)
        text_rect = text.get_rect(center=(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(1000)
