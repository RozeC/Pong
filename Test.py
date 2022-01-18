import pygame

pygame.init()
screen = pygame.display.set_mode((720, 480))
pygame.display.set_caption('Ping Pong')
clock = pygame.time.Clock()
FPS = 60
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
clock.tick(FPS)

screen.fill(BLACK)
pygame.draw.rect(screen, WHITE, (10, 50, 20, 60))
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()