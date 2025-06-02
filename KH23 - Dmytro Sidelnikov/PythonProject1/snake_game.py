import pygame
import sys
import random


pygame.init()

# Розмір вікна
WIDTH, HEIGHT = 700, 500
CELL_SIZE = 20

# Кольори
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Вікно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змійка")

# Змінні гри
clock = pygame.time.Clock()
snake = [(100, 100)]
snake_dir = (CELL_SIZE, 0)  # Напрямок: вправо
food = (300, 200)
score = 0

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

def draw_food():
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

def move_snake():
    global food, score

    head = snake[0]
    new_head = (head[0] + snake_dir[0], head[1] + snake_dir[1])
    snake.insert(0, new_head)

    if new_head == food:
        food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
        score += 1
    else:
        snake.pop()

def check_collision():
    head = snake[0]
    if head in snake[1:] or head[0] < 0 or head[1] < 0 or head[0] >= WIDTH or head[1] >= HEIGHT:
        return True
    return False

# Основний цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):
                snake_dir = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):
                snake_dir = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):
                snake_dir = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):
                snake_dir = (CELL_SIZE, 0)

    move_snake()

    if check_collision():
        print(f"Гра закінчена! Рахунок: {score}")
        pygame.quit()
        sys.exit()

    screen.fill(BLACK)
    draw_snake()
    draw_food()
    pygame.display.flip()
    clock.tick(10)