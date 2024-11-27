import pygame, time, random
# Reminder - Commit this to game.py on codeberg

def round_init(enemy_moves):
    global rounds
    global health
    global status_rounds
    global status_active
    global target

    rounds += 1
    round_move = random.choice(enemy_moves)

    if status_rounds <= 0:
        status_active = False
        target = ""
        status_user = ""

    if round_move[1] == "Special" and target != "enemy":
        if round_move[0] == "Burn":
            status_user = "enemy"
            burn(status_user)
        if round_move[0] == "Freeze Ray":
            status_user = "enemy"
            freeze(status_user)
    else:
        if geo_choice == "circle" and round_move[1] == "Physical" and target != "enemy":
            health -= (round_move[2]*1.15)
        elif geo_choice == "square" and round_move[1] == "Magic" and target != "enemy":
            health -= (round_move[2]*1.15)
    print(rounds)

def burn(status_user):
    global status_active
    global status_rounds
    global status_type
    global target
    global health
    global total_health
    global enemy_health
    global enemy_total_health

    if status_active == False:
        status_type = "burn"
        status_active = True
        status_rounds = random.randrange(3,5)

        if status_user == "enemy":
            target = "user"
            health -= (total_health * 0.03)
            print("burn used!") 
        elif status_user == "user":
            target = "enemy"
            enemy_health -= (enemy_total_health * 0.03)
            print("burn used!")

    else:
        if target == "user":
            health -= (total_health * 0.03)
        elif target == "enemy":
            enemy_health -= (enemy_total_health * 0.03)

        print("applying burn damage!")
    
    status_rounds -= 1

def freeze(status_user):
    global status_rounds
    global status_active
    global status_type
    global target

    if status_active == False:
        status_type = "frozen"
        status_active = True
        status_rounds = random.randrange()

        if status_user == "enemy":
            target = "user"
        elif status_user == "user":
            target = "enemy"

        print("You're frozen!")
    elif status_active == True:
        print("Target already frozen!")

        if status_user == "enemy":
            status_rounds -= 1



# Window creation & Customisation
pygame.init() # initialises pygame
ssize = (900,500)
screen = pygame.display.set_mode(ssize) 
pygame.display.set_caption("GeoRogue - Battle")

# Empty Containers
rounds = 0
uptime = 0
status_rounds = 0
status_active = False
status_type = ""
status_user = ""
target = ""

# Health and Damage Boost
health = 100
dmgboost = 1

# Geo Config
with open("config.txt") as file:
    geo_choice = file.read()

    if geo_choice == "square":
        health = 125
    elif geo_choice == "circle":
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
        enemy_dmg = 1
    elif enemy_geo_num > 6:
        enemy_geo = "circle"
        enemy_health = 100
        enemy_dmg = 1.25
elif geo_choice == "square": # Whereas Square Players have a 60% chance to face a circle geo
    if enemy_geo_num <= 6:
        enemy_geo = "circle"
        enemy_health = 100
        enemy_dmg = 1.25
    elif enemy_geo_num > 6:
        enemy_geo = "square"
        enemy_health = 125
        enemy_dmg = 100

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

# Special Moves
specmoves = [
    ("Burn","Special","burnt"),
    ("Freeze Ray","Special","frozen"),
]

# FPS & Running
clock = pygame.time.Clock() # assigns pygame fps to clock
running = True

# Generic Button Config
button_colour = (157,157,157)
font = pygame.font.Font(None,30)
screen.fill("white")

# Health label pos
healthx = 30
healthy = 300
en_healthx = 760
en_healthy = 300

moves = []
if geo_choice == "square":
    for x in range(0,3):
        y = random.randint(0,2)
        if y == 0 or y == 1:
            moves.append(random.choice(physmoves))
        elif y == 2:
            moves.append(random.choice(magicmoves))
    moves.append(random.choice(specmoves))
if geo_choice == "circle":
    for x in range(0,3):
        y = random.randint(0,2)
        if y == 0 or y == 1:
            moves.append(random.choice(magicmoves))
        elif y == 2:
            moves.append(random.choice(physmoves))
    moves.append(random.choice(specmoves))

enemy_moves = []
if geo_choice == "square":
    for x in range (0,3):
        y = random.randint(0,2)
        if y == 0 or y == 1:
            enemy_moves.append(random.choice(magicmoves))
        elif y == 2:
            enemy_moves.append(random.choice(physmoves))
    enemy_moves.append(random.choice(specmoves))
elif geo_choice == "circle":
    for x in range (0,3):
        y = random.randint(0,2)
        if y == 0 or y == 1:
            enemy_moves.append(random.choice(physmoves))
        elif y == 2:
            enemy_moves.append(random.choice(magicmoves))
    enemy_moves.append(random.choice(specmoves))
for x in moves:
    print(x)
for x in enemy_moves:
    print(x)

while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 and target != "user":
                enemy_health -= moves[0][2]
                round_move = round_init(enemy_moves)
            if event.key == pygame.K_2 and target != "user":
                enemy_health -= moves[1][2]
                round_move = round_init(enemy_moves)
            if event.key == pygame.K_3 and target != "user":
                enemy_health -= moves[2][2]
                round_move = round_init(enemy_moves)
            if event.key == pygame.K_4 and target != "user":
                print(moves[3][0])
                status_user = "user"
                if moves[3][0] == "Burn":
                    burn(status_user)
                elif moves[3][0] == "Freeze Ray":
                    freeze(status_user)
                
                round_move = round_init(enemy_moves)

    if status_active == True and target == "user":
        status_rounds -= 1
        round_init(enemy_moves)

    # Uptime
    uptime_remove = pygame.Rect(450,100,100,50)
    pygame.draw.rect(screen,(255,255,255),uptime_remove)

    uptime_label = font.render(f"{round(uptime)}",True,(0,0,0))
    screen.blit(uptime_label,(450,100))

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

    # Health
    plr_health = pygame.Rect(healthx,healthy,150,50)
    pygame.draw.rect(screen,(255,255,255),plr_health)

    en_health = pygame.Rect(en_healthx,en_healthy, 150,50)
    pygame.draw.rect(screen,(255,255,255),en_health)

    plr_health_text = font.render(f"Health: {health}",True,(0,0,0))
    screen.blit(plr_health_text,(healthx,healthy))

    en_health_text = font.render(f"Health: {enemy_health}",True,(0,0,0))
    screen.blit(en_health_text,(en_healthx,en_healthy))

    # Game Over
    if enemy_health <= 0 or health <= 0:
        
        if enemy_health <= 0 and health > 0:
            with open("condition.txt","w") as file:
                file.write("") # Ensures previous game result is wiped
                file.write("win")
            with open("victories.txt",) as file:
                temp = file.readline()
                temp = int(temp) + 1
            with open("victories.txt","w") as file:
                file.write(str(temp))
        
        with open("end.py") as file:
            exec(file.read())
        pygame.QUIT


    pygame.display.update() # Updates the game every frame

    clock.tick(60) # game runs at 60fps
    uptime = uptime+(1/60)

pygame.quit()