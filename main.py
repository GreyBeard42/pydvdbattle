import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Window Name")
clock = pygame.time.Clock()
print("\nThe games have begun!\n\n---")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("\nBye for now!\n\n---")
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    pygame.display.flip()
    clock.tick(60)
