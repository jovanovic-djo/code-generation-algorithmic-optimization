import pygame
import random

class Snake:
    def __init__(self, grid_width, grid_height, cell_size):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cell_size = cell_size
        self.position = [random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)]
        self.direction = None
        self.move_count = 0
        self.image = pygame.image.load("game/imgs/snake.png")
        self.image = pygame.transform.scale(self.image, (cell_size, cell_size))

    def change_direction(self, key):
        if key == pygame.K_UP and self.direction != "DOWN":
            self.direction = "UP"
        elif key == pygame.K_DOWN and self.direction != "UP":
            self.direction = "DOWN"
        elif key == pygame.K_LEFT and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif key == pygame.K_RIGHT and self.direction != "LEFT":
            self.direction = "RIGHT"

    def move(self):
        if self.direction:
            self.move_count += 1
            if self.direction == "UP":
                self.position[1] -= 1
            elif self.direction == "DOWN":
                self.position[1] += 1
            elif self.direction == "LEFT":
                self.position[0] -= 1
            elif self.direction == "RIGHT":
                self.position[0] += 1

    def teleport(self):
        self.position[0] %= self.grid_width
        self.position[1] %= self.grid_height

    def draw(self, screen):
        screen.blit(self.image, (self.position[0] * self.cell_size, self.position[1] * self.cell_size))
