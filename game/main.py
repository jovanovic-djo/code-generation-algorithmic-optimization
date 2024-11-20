import pygame
import random

pygame.init()

A = random.randint(1, 50)
B = random.randint(1, 50)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

CELL_SIZE = 15
SCREEN_WIDTH = A * CELL_SIZE
SCREEN_HEIGHT = B * CELL_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

snake_image = pygame.image.load("game\\imgs\\snake.png")
apple_image = pygame.image.load("game\\imgs\\apple.png")

snake_image = pygame.transform.scale(snake_image, (CELL_SIZE, CELL_SIZE))
apple_image = pygame.transform.scale(apple_image, (CELL_SIZE, CELL_SIZE))

clock = pygame.time.Clock()

snake_pos = [random.randint(0, A - 1), random.randint(0, B - 1)]  # Random start position
snake_direction = None
snake_speed = 10
move_count = 0

apple_pos = [random.randint(0, A - 1), random.randint(0, B - 1)]
while apple_pos == snake_pos:  # Ensure the apple doesn't spawn on the snake
    apple_pos = [random.randint(0, A - 1), random.randint(0, B - 1)]

def teleport(position):
    position[0] %= A
    position[1] %= B

def draw_grid():
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (SCREEN_WIDTH, y))

running = True
win = False
while running:
    screen.fill(WHITE)

    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                move_count += 1
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                move_count += 1
                snake_direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                move_count += 1
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                move_count += 1
                snake_direction = "RIGHT"

    if snake_direction:
        if snake_direction == "UP":
            snake_pos[1] -= 1
        elif snake_direction == "DOWN":
            snake_pos[1] += 1
        elif snake_direction == "LEFT":
            snake_pos[0] -= 1
        elif snake_direction == "RIGHT":
            snake_pos[0] += 1

        teleport(snake_pos)

    if snake_pos == apple_pos:
        win = True
        running = False

    if move_count > 100:
        running = False

    screen.blit(
        apple_image,
        (apple_pos[0] * CELL_SIZE, apple_pos[1] * CELL_SIZE),
    )

    screen.blit(
        snake_image,
        (snake_pos[0] * CELL_SIZE, snake_pos[1] * CELL_SIZE),
    )

    pygame.display.flip()

    clock.tick(snake_speed)

screen.fill(WHITE)
font = pygame.font.SysFont(None, 50)
if win:
    text = font.render("W", True, BLACK)
else:
    text = font.render("L", True, BLACK)
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
screen.blit(text, text_rect)
pygame.display.flip()

pygame.time.wait(2000)
pygame.quit()
