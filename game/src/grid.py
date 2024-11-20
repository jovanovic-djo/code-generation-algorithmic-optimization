import pygame

class Grid:
    def __init__(self, grid_width, grid_height, cell_size, screen):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cell_size = cell_size
        self.screen = screen
        self.color = (200, 200, 200)

    def draw(self):
        for x in range(0, self.grid_width * self.cell_size, self.cell_size):
            pygame.draw.line(self.screen, self.color, (x, 0), (x, self.grid_height * self.cell_size))
        for y in range(0, self.grid_height * self.cell_size, self.cell_size):
            pygame.draw.line(self.screen, self.color, (0, y), (self.grid_width * self.cell_size, y))
