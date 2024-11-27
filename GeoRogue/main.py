# Modules
import pygame

# Ensures that config file is empty upon execution of the main.py scr when a player starts the game
with open("config.txt","w") as file:
    file.write("")

# Window creation & Customisation
pygame.init() # initialises pygame
ssize = (625,300)
screen = pygame.display.set_mode(ssize) 
pygame.display.set_caption("GeoRogue")

# FPS & Running
clock = pygame.time.Clock() # assigns pygame fps to clock
running = True

# Generic Button Config
button_colour = (157,157,157)
font = pygame.font.Font(None, 24)

# Square Button
button_surface_square = pygame.Surface((150,50)) # A button surface is its size in x and y
text_square = font.render("Square Geo", True, (0,0,0))
text_square_display = text_square.get_rect(center=(button_surface_square.get_width()/2, button_surface_square.get_height()/2))
button_square = pygame.Rect(125,125,150,50)

# Circle Button
button_surface_circle = pygame.Surface((150,50))
text_circle = font.render("Circle Geo",True, (0,0,0))
text_circle_display = text_circle.get_rect(center=(button_surface_square.get_width()/2, button_surface_square.get_height()/2))
button_circle = pygame.Rect(350,125,200,50)          

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Triggers when mb1 clicked
        if button_square.collidepoint(event.pos): # Triggers when square button clicked
            print("Square!")

            with open("config.txt","w") as file: # Writes player's choice to config
                file.write("square")
            with open("game.py") as file: # executes game.py
                exec(file.read())

            pygame.QUIT

        if button_circle.collidepoint(event.pos):
            print("Circle!")

            with open("config.txt","w") as file:
                file.write("circle")
            with open("game.py") as file:
                exec(file.read())

            pygame.QUIT

    
    # Button hover effects
    if button_square.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect((button_surface_square), (180,180,180), (0,0,150,50))
    else:
        pygame.draw.rect((button_surface_square), (button_colour), (0,0,150,50))

    if button_circle.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect((button_surface_circle), (180,180,180), (0,0,150,50))
    else:
        pygame.draw.rect((button_surface_circle), (button_colour), (0,0,150,50))

    # Button rendering
    button_surface_square.blit(text_square,text_square_display)
    screen.blit(button_surface_square, (button_square.x, button_square.y))

    button_surface_circle.blit(text_circle,text_circle_display)
    screen.blit(button_surface_circle, (button_circle.x, button_circle.y))

    pygame.display.update() # Updates the game every frame

    clock.tick(60) # game runs at 60fps

pygame.quit()