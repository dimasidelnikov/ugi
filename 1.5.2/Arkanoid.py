import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Арканоїд")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Параметри платформи та м’яча
paddle = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 30, 120, 10)
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)

ball_speed = [5, -5]
clock = pygame.time.Clock()

running = True
while running:
    win.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-10, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(10, 0)

    # Рух м’яча
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Відбиття від стінок
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]

    # Відбиття від платформи
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # Програш
    if ball.bottom >= HEIGHT:
        ball.x, ball.y = WIDTH // 2 - 15, HEIGHT // 2 - 15

    pygame.draw.rect(win, WHITE, paddle)
    pygame.draw.ellipse(win, RED, ball)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()