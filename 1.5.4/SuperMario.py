import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

clock = pygame.time.Clock()

# Основні кольори
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Гравець
player = pygame.Rect(100, 500, 40, 60)
velocity_y = 0
jumping = False
ground = pygame.Rect(0, 580, WIDTH, 20)

run = True
while run:
    clock.tick(60)
    screen.fill(WHITE)

    # Події
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_SPACE] and not jumping:
        velocity_y = -15
        jumping = True

    # Гравітація
    velocity_y += 1
    player.y += velocity_y

    # Колізія з підлогою
    if player.colliderect(ground):
        player.y = ground.top - player.height
        velocity_y = 0
        jumping = False

    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, (0, 255, 0), ground)
    pygame.display.update()

pygame.quit()