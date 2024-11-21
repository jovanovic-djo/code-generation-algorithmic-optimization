import pygame
import random

class Apple:
    def __init__(self, grid_width, grid_height, cell_size):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cell_size = cell_size
        self.position = [random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)]
        self.image = pygame.image.load("simulation/imgs/apple.png")
        self.image = pygame.transform.scale(self.image, (cell_size, cell_size))

    def draw(self, screen):
        screen.blit(self.image, (self.position[0] * self.cell_size, self.position[1] * self.cell_size))
