import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rogue × Birb")
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        screen.fill((255, 127.5, 127.5))

        pygame.display.flip()
        clock.tick(60)

pygame.quit()