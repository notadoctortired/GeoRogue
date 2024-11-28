# Modules
import pygame

pygame.mixer.init()
pygame.mixer.music.load("GeoRogue/GeoRogue/Music/duelofthefates.mp3")
pygame.mixer.music.play(-1,0,0)

# Window creation & Customisation
pygame.init() # initialises pygame
ssize = (900,500)
screen = pygame.display.set_mode(ssize) 
pygame.display.set_caption("GeoRogue - Game Over!")
icon = pygame.image.load("GeoRogue/GeoRogue/icon.png")
pygame.display.set_icon(icon)

# FPS & Running
clock = pygame.time.Clock() # assigns pygame fps to clock
running = True

# Generic Button Config
button_colour = (157,157,157)
font = pygame.font.Font(None,100)
smallfont = pygame.font.Font(None,50)
screen.fill("white")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    end_text = font.render("Game Over!",True,(0,0,0))
    screen.blit(end_text,(270,160))

    with open("GeoRogue/GeoRogue/condition.txt","r") as file:
        con = file.read()
        if con == "win":
            con_text = smallfont.render("You Win!",True,(54, 63, 235))
            screen.blit(con_text,(385,240))
        else:
            con_text = smallfont.render("You Lose!",True,(255,0,0))
            screen.blit(con_text,(385,240))

    pygame.display.update()

    clock.tick(60)

pygame.QUIT