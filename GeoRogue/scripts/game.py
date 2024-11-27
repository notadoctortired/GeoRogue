import pygame, time, random

# Initialises mixer so that music can be loaded and played
pygame.mixer.init()
pygame.mixer.music.load("GeoRogue/Music/beethoven3rd.mp3")
pygame.mixer.music.play(-1,0,0)

def round_init(enemy_moves):
    global rounds
    global health

    rounds += 1
    round_move = random.choice(enemy_moves)

    if geo_choice == "circle" and round_move[1] == "Physical":
        health -= (round_move[2]*1.15)
    elif geo_choice == "square" and round_move[1] == "Magic":
        health -= (round_move[2]*1.15)
    else:
        health -= round_move[2]
    print(rounds)

# Window creation & Customisation
pygame.init() # initialises pygame
ssize = (900,500)
screen = pygame.display.set_mode(ssize) 
pygame.display.set_caption("GeoRogue - Battle")
icon = pygame.image.load("GeoRogue/icon.png")
pygame.display.set_icon(icon)

# Empty Containers
rounds = 0
uptime = 0

# Geo Config
with open("GeoRogue/config.txt") as file:
    geo_choice = file.read()

    if geo_choice == "square":
        health = 125
        dmg = 1
    elif geo_choice == "circle":
        health = 100
        dmg = 1.20
    else:
        print("Critical error! Geo not found in config.txt file!")
        time.sleep(3)
        quit()

total_health = health

# Enemy Geo Config
enemy_geo_num = random.randint(1,10)

if geo_choice == "circle": # Circle Players have a 60% chance to face a square geo
    if enemy_geo_num <= 6:
        enemy_geo = "square"
        enemy_health = 125
    elif enemy_geo_num > 6:
        enemy_geo = "circle"
        enemy_health = 100
elif geo_choice == "square": # Whereas Square Players have a 60% chance to face a circle geo
    if enemy_geo_num <= 6:
        enemy_geo = "circle"
        enemy_health = 100
    elif enemy_geo_num > 6:
        enemy_geo = "square"
        enemy_health = 125

enemy_total_health = enemy_health

# Physical Moves
physmoves = [
    ("Scream","Physical",8),
    ("Punch","Physical",10),
    ("Slap","Physical",10),
    ("Chop","Physical",12),
    ("Kick","Physical",15),
    ("Rock Throw","Physical",20)
]

# Magic Moves
magicmoves = [
    ("Spark","Magic",5),
    ("Magic Missile","Magic",10),
    ("Psychic Knife","Magic",10),
    ("Magic Meteor","Magic",15),
    ("Psy-ray","Magic",20),
    ("Mind Infiltration","Magic",25)
]

# FPS & Running
clock = pygame.time.Clock() # assigns pygame fps to clock
running = True

# Generic Button Config
button_colour = (157,157,157)
font = pygame.font.Font(None,30)
smallfont = pygame.font.Font(None, 20)
screen.fill("white")

# Health label pos
healthx = 30
healthy = 300
en_healthx = 760
en_healthy = 300
movesx = 30
movesy = 320
en_movesx = 760
en_movesy = 320

moves = []
if geo_choice == "square":
    for x in range(0,4):
        if x == 0 or x == 1:
            moves.append(random.choice(physmoves))
        elif x == 2 or x == 3:
            moves.append(random.choice(magicmoves))
elif geo_choice == "circle":
    for x in range(0,4):
        if x == 0 or x == 1:
            moves.append(random.choice(magicmoves))
        elif x == 2 or x == 3:
            moves.append(random.choice(physmoves))

enemy_moves = []
if enemy_geo == "square":
    for x in range (0,4):
        if x == 0 or x == 1:
            enemy_moves.append(random.choice(magicmoves))
        elif x == 2 or x == 3:
            enemy_moves.append(random.choice(physmoves))
elif enemy_geo == "circle":
    for x in range (0,4):
        if x == 0 or x == 1:
            enemy_moves.append(random.choice(physmoves))
        elif x == 2 or x == 3:
            enemy_moves.append(random.choice(magicmoves))

for x in moves:
    print(x)
print("--------")
for x in enemy_moves:
    print(x)

while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if moves[0][1] == "Physical" and enemy_geo == "circle":
                    enemy_health -= moves[0][2]*(1.15*dmg)
                elif moves[0][1] == "Magic" and enemy_geo == "square":
                    enemy_health -= moves[0][2]*(1.15*dmg)
                else:
                    enemy_health -= moves[0][2]*dmg
                
                round_init(enemy_moves)
            elif event.key == pygame.K_2:
                if moves[1][1] == "Physical" and enemy_geo == "circle":
                    enemy_health -= moves[1][2]*(1.15*dmg)
                elif moves[1][1] == "Magic" and enemy_geo == "square":
                    enemy_health -= moves[1][2]*(1.15*dmg)
                else:
                    enemy_health -= moves[1][2]*dmg
                round_init(enemy_moves)
            elif event.key == pygame.K_3:
                if moves[2][1] == "Physical" and enemy_geo == "circle":
                    enemy_health -= moves[2][2]*(1.15*dmg)
                elif moves[2][1] == "Magic" and enemy_geo == "square":
                    enemy_health -= moves[2][2]*(1.15*dmg)
                else:
                    enemy_health -= moves[2][2]*dmg
                round_init(enemy_moves)
            elif event.key == pygame.K_4:
                if moves[3][1] == "Physical" and enemy_geo == "circle":
                    enemy_health -= moves[3][2]*(1.15*dmg)
                elif moves[3][1] == "Magic" and enemy_geo == "square":
                    enemy_health -= moves[3][2]*(1.15*dmg)
                else:
                    enemy_health -= moves[3][2]*dmg
                round_init(enemy_moves)

    # Uptime
    uptime_remove = pygame.Rect(450,100,100,50)
    pygame.draw.rect(screen,(255,255,255),uptime_remove)
    uptime_label = font.render(f"{round(uptime)}",True,(0,0,0))
    screen.blit(uptime_label,(450,100))

    rounds_remove = pygame.Rect(450,150,100,50)
    pygame.draw.rect(screen,(255,255,255),rounds_remove)
    rounds_label = font.render(f"{rounds}",True,(0,0,0))
    screen.blit(rounds_label,(450,150))

    if geo_choice == "square":
        plr_geo = pygame.Rect(150,50,200,200)
        pygame.draw.rect(screen,(0,0,255),plr_geo)
    elif geo_choice == "circle":
        pygame.draw.circle(screen,(0,0,255),(250,150),100)

    if enemy_geo == "square":
        npc_geo = pygame.Rect(570,50,200,200)
        pygame.draw.rect(screen,(255,0,0),npc_geo)
    elif enemy_geo == "circle":
        pygame.draw.circle(screen,(255,0,0),(650,150),100)

    # Health and Move Labels
    plr_health = pygame.Rect(healthx,healthy,150,50)
    pygame.draw.rect(screen,(255,255,255),plr_health)
    en_health = pygame.Rect(en_healthx,en_healthy, 150,50)
    pygame.draw.rect(screen,(255,255,255),en_health)

    plr_health_text = font.render(f"Health: {health}",True,(0,0,0))
    screen.blit(plr_health_text,(healthx,healthy))
    en_health_text = font.render(f"Health: {enemy_health}",True,(0,0,0))
    screen.blit(en_health_text,(en_healthx,en_healthy))

    plr_moves = pygame.Rect(movesx,movesy,150,500)
    pygame.draw.rect(screen,(255,255,255),plr_moves)
    en_moves = pygame.Rect (en_movesx,en_movesy, 150,500)
    pygame.draw.rect(screen,(255,255,255),en_moves)

    # Move Text is rendered line by line using separate labels in a for loop, as pygame does not allow for usage of string formatting
    y = 330
    for x in range(0,4):
        move_text = smallfont.render(f"{moves[x][0]} - {moves[x][2]}",True,(0,0,0))
        screen.blit(move_text,(movesx,y))
        en_move_text = smallfont.render(f"{enemy_moves[x][0]} - {enemy_moves[x][2]}",True,(0,0,0))
        screen.blit(en_move_text,(en_movesx,y))
        y += 20

    # Game Over
    if enemy_health <= 0 or health <= 0:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        
        if enemy_health <= 0 and health > 0:
            with open("GeoRogue/condition.txt","w") as file:
                file.write("") # Ensures previous game result is wiped
                file.write("win")
            with open("GeoRogue/victories.txt",) as file:
                temp = file.readline()
                temp = int(temp) + 1
            with open("GeoRogue/victories.txt","w") as file:
                file.write(str(temp))
        
        with open("GeoRogue/scripts/end.py") as file:
            exec(file.read())
        pygame.QUIT


    pygame.display.update() # Updates the game every frame

    clock.tick(60) # game runs at 60fps
    uptime = uptime+(1/60)

pygame.quit()