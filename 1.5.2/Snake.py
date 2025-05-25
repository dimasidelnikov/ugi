import pygame
import random

pygame.init()

# Налаштування вікна
display = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Змійка')

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 15)

# Основні кольори
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (213, 50, 80)

# Розміри змійки та швидкість
snake_block = 10
snake_speed = 15

# Функція для малювання змійки
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

# Головна функція
def gameLoop():
    game_over = False
    game_close = False

    x1 = 300
    y1 = 200

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, 600 - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, 400 - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            display.fill(white)
            message = font_style.render("Гра закінчена! Натисни C - продовжити або Q - вийти", True, red)
            display.blit(message, [50, 180])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change
        
        if x1 >= 600 or x1 < 0 or y1 >= 400 or y1 < 0:
            game_close = True

        display.fill(black)
        pygame.draw.rect(display, red, [foodx, foody, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, 600 - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, 400 - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()