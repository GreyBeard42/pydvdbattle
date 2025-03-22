from classes import Rect

import pygame
import sys
import random
import math

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("DvD Battle")
clock = pygame.time.Clock()
print("\nThe games have begun!\n\n---")

players = []
players.append(Rect(150, 150, random.randint(60, 150)*1.5, random.randint(60, 150)*1.5, random.randint(0, 2), random.randint(0, 2), (245, 66, 126), (112, 17, 49)))
players.append(Rect(450, 450, players[0].h, players[0].w, players[0].vx, players[0].vy, (66, 245, 233), (15, 82, 77)))
restarttimer = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("\nBye for now!\n\n---")
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    
    if restarttimer == 1:
        pygame.display.set_caption("DvD Battle")
        players = []
        players.append(Rect(150, 150, random.randint(60, 150)*1.5, random.randint(60, 150)*1.5, random.randint(0, 2), random.randint(0, 2), (245, 66, 126), (112, 17, 49)))
        players.append(Rect(450, 450, players[0].h, players[0].w, players[0].vx, players[0].vy, (66, 245, 233), (15, 82, 77)))
    if restarttimer > 0:
        restarttimer -= 1
    if players[0].s > 0.3 and players[1].s > 0.3 and restarttimer == 0:
        players[0].rect = pygame.draw.rect(screen, players[0].fill, (players[0].x, players[0].y, players[0].w*players[0].s, players[0].h*players[0].s))
        pygame.draw.rect(screen, players[0].stroke, (players[0].x, players[0].y, players[0].w*players[0].s, players[0].h*players[0].s), 5)
        pygame.draw.rect(screen, players[0].stroke, (players[0].x, players[0].y, players[0].w*players[0].s, 15))
        pygame.draw.rect(screen, players[0].stroke, (players[0].x, players[0].y+players[0].h*players[0].s-15, players[0].w*players[0].s, 15))

        players[1].rect = pygame.draw.rect(screen, players[1].fill, (players[1].x, players[1].y, players[1].w*players[1].s, players[1].h*players[1].s))
        pygame.draw.rect(screen, players[1].stroke, (players[1].x, players[1].y, players[1].w*players[1].s, players[1].h*players[1].s), 5)
        pygame.draw.rect(screen, players[1].stroke, (players[1].x, players[1].y, 15, players[1].h*players[1].s))
        pygame.draw.rect(screen, players[1].stroke, (players[1].x+players[1].w*players[1].s-15, players[1].y, 15, players[1].h*players[1].s))
    else:
        if restarttimer == 0: restarttimer = 180
        if players[0].s > 0.3:
            pygame.display.set_caption("Red Wins! - DvD Battle")
            pygame.draw.rect(screen, players[0].fill, (players[0].x, players[0].y, players[0].w*players[0].s, players[0].h*players[0].s))
            pygame.draw.rect(screen, players[0].stroke, (players[0].x, players[0].y, players[0].w*players[0].s, players[0].h*players[0].s), 5)
            pygame.draw.rect(screen, players[0].stroke, (players[0].x, players[0].y, players[0].w*players[0].s, 15))
            pygame.draw.rect(screen, players[0].stroke, (players[0].x, players[0].y+players[0].h*players[0].s-15, players[0].w*players[0].s, 15))
        else:
            pygame.display.set_caption("Blue Wins! - DvD Battle")
            pygame.draw.rect(screen, players[1].fill, (players[1].x, players[1].y, players[1].w*players[1].s, players[1].h*players[1].s))
            pygame.draw.rect(screen, players[1].stroke, (players[1].x, players[1].y, players[1].w*players[1].s, players[1].h*players[1].s), 5)
            pygame.draw.rect(screen, players[1].stroke, (players[1].x, players[1].y, 15, players[1].h*players[1].s))
            pygame.draw.rect(screen, players[1].stroke, (players[1].x+players[1].w*players[1].s-15, players[1].y, 15, players[1].h*players[1].s))

    n1 = math.ceil(max(abs(players[0].vx), abs(players[0].vy)))
    n2 = math.ceil(max(abs(players[1].vx), abs(players[1].vy)))
    for i in range(max(n1, n2)):
        if i <= n1: players[0].move(players[1], n1)
        if i <= n2: players[1].move(players[0], n2)
        if players[0].rect.colliderect(players[1].rect) and players[0].s > 0.3 and players[1].s > 0.3:
            players[0].col(players[1])

    pygame.display.flip()
    clock.tick(60)
