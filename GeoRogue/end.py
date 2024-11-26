# Modules
import pygame, time, random

# Window creation & Customisation
pygame.init() # initialises pygame
ssize = (900,500)
screen = pygame.display.set_mode(ssize) 
pygame.display.set_caption("GeoRogue - Game Over!")

# FPS & Running
clock = pygame.time.Clock() # assigns pygame fps to clock
running = True

# Generic Button Config
button_colour = (157,157,157)
font = pygame.font.Font(None,30)
screen.fill("white")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

    clock.tick(60)