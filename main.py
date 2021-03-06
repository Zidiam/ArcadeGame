# Made by Jason Melnik
# Date: 12/18/2017
# Version of game: 6.6

# Imports
import pygame
import time
import random
import operator
import fileinput
import os
import sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


global names_text
filep = "Resources//"
names_text = resource_path(filep + "list_of_names.txt")
words = resource_path(filep + "LemonMilkbold.otf")
# The size of the screen
WIDTH = 500
HEIGHT = 500
FPS = 30

# A set list of high scores
for line in fileinput.FileInput(names_text, inplace=1):
    if line.rstrip():
        print(line, end='')

global list_of_names
list_of_names = {}
with open(names_text) as f:
    for line in f:
        (key, val) = line.split()
        list_of_names[str(key)] = int(val)
f.close()

# Color codes
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
AQUA = (0, 255, 255)
VIOLET = (148, 0, 211)
YELLOW = (255, 255, 0)
BROWN = (165, 42, 42)
GRAY = (128, 128, 128)


# Bullet object
class Bullet(pygame.sprite.Sprite):
    # Bullet that shoots up
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = rocketpic
        self.rect = self.image.get_rect()
        self.rect.center = ship.rect.center

    def update(self):
        global fast_enemy
        if self.rect.top <= HEIGHT:  # if the bullet is not greather than top we want it to keep going up by increasing the y
            self.rect.y -= 5
        if self.rect.top <= 0:  # but if it reachest the top it gets reset back into the ship
            Bullets.remove(self)

        for i in range(len(enemy_ships)):
            if pygame.sprite.collide_rect(self, enemy_ships.sprites()[i]):
                global points_counter
                points_counter += 1
                enemy_ships.remove(enemy_ships.sprites()[i])
                Bullets.remove(self)
                if i == fast_enemy:
                    fast_enemy = random.randint(0, (len(enemy_ships.sprites())))
                if i < fast_enemy:
                    fast_enemy -= 1
        if pygame.sprite.collide_rect(self, CoinObject):
            CoinObject.update()
            Bullets.remove(self)
            global coins
            coins += coinadd


# Ship Object
class Ship(pygame.sprite.Sprite):
    # Ship that moves around
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = goodship
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 20)

    def update(self, x):
        if x == 0:  # if pressing right move right
            self.rect.x += 5
        else:  # move left
            self.rect.x -= 5


# Enemy Object
class Easy_Enemy(pygame.sprite.Sprite):
    # Enemy Ship that moves around
    def __init__(self, enemy_ship_x, enemy_ship_y):  # These are its features
        pygame.sprite.Sprite.__init__(self)
        self.image = enemyship
        self.rect = self.image.get_rect()
        self.rect.center = (enemy_ship_x, enemy_ship_y)

    def update(self):  # Moves down unless it touches the bottom creating a game over
        global points_counter
        self.rect.y += 5
        if self.rect.bottom >= HEIGHT:
            global game_over_2
            game_over_2 = True


# Coin Object
class Coin_Object(pygame.sprite.Sprite):
    def __init__(self):
        coin_random_x = random.randint(20, 480)
        coin_random_y = random.randint(20, 400)
        pygame.sprite.Sprite.__init__(self)

        self.image = gcoin
        self.rect = self.image.get_rect()
        self.rect.center = (coin_random_x, coin_random_y)

    def update(self):
        coin_random_x = random.randint(20, 480)
        coin_random_y = random.randint(20, 400)
        self.rect.center = (coin_random_x, coin_random_y)


# This object is just to click on in the shop
class Bullet_Speed(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = buypic
        self.rect = self.image.get_rect()
        self.rect.center = (70, 60)


# This object is just to click on in the shop
class Extra_Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = buypic
        self.rect = self.image.get_rect()
        self.rect.center = (360, 60)


# This object is just to click on in the shop
class Movement_Speed(pygame.sprite.Sprite):
    # Enemy Ship that moves around
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = buypic
        self.rect = self.image.get_rect()
        self.rect.center = (210, 60)


# This object is just to click on in the shop
class Coin_Spawn(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = buypic
        self.rect = self.image.get_rect()
        self.rect.center = (70, 149)


# This object is just to click on in the shop
class Coin_Delay(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = buypic
        self.rect = self.image.get_rect()
        self.rect.center = (210, 149)


# This object is just to click on in the shop
class Coin_Ammount(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = buypic
        self.rect = self.image.get_rect()
        self.rect.center = (360, 149)

# This object is just to click on in the shop
class Points_Exchange(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = buypic
        self.rect = self.image.get_rect()
        self.rect.center = (300, 350)

# This object is for controls
class Controls(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        charRect2 = pygame.Rect((0, 0), (100, 100))
        Controls = pygame.image.load(os.path.abspath(filep + "Controls.png"))
        Controls = pygame.transform.scale(Controls, charRect2.size)
        Controls = Controls.convert()

        self.image = Controls
        self.rect = self.image.get_rect()
        self.rect.center = (200, 450)

# This object is for controls
class SControls(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        charRect2 = pygame.Rect((0, 0), (100, 100))
        SControls = pygame.image.load(os.path.abspath(filep + "SControls.png"))
        SControls = pygame.transform.scale(SControls, charRect2.size)
        SControls = SControls.convert()

        self.image = SControls
        self.rect = self.image.get_rect()
        self.rect.center = (300, 450)


# My level algorith that creates levels for me
def levels(x):
    global enemy_death_count
    enemy_death_count = 0
    global enemy_ship_y
    global enemy_ship_x
    global continue_level
    global enemy_ships
    global enemy_speed
    global enemy_ship
    continue_level = 0
    enemy_ship_y = 50
    enemy_ship_x = 20
    for i in range(
            x):  # Basicly to put it in simple terms if the ships reach the end of the screen it start a new row and so on untill it reachest level 191 then it resets
        enemy_ship = Easy_Enemy(enemy_ship_x, enemy_ship_y)
        enemy_ships.add(enemy_ship)
        enemy_ship_x += 50
        if enemy_ship_x >= 480:
            enemy_ship_x = 20
            enemy_ship_y += 40
            enemy_speed -= 10
        if enemy_ship_y >= 400:
            global total_level
            global level
            enemy_ship_y = 20
            enemy_ship_x = 20
            enemy_speed = 500
            total_level = total_level + level
            level = 10
        continue_level += 1
    global start_level
    start_level = 1


def gameLoop():  # The start of the whole game
    # Global Initiation
    global swait
    global points_buy
    global rocketpic
    global how_many_bullets
    global bullet_counter
    global enemy_ship_location
    global enemy_counter
    global enemy_ship_x
    global enemy_ship_y
    global start_level
    global level
    global total_level
    global enemy_death_count
    global continue_level
    global enemy_ship_location
    global allenemy_counter
    global name
    global left_key
    global right_key
    global points_counter
    global bullet_counter
    global game_over_2
    global buypic
    global enemy_ships
    global ship
    global bullet
    global shop
    global move_timer
    global bullet_timer
    global bullet_speed
    global coins
    global movement
    global speed
    global move
    global wait
    global enemy_speed
    global extra_bullet_object
    global bullet_speed_object
    global PowerUps
    global Extra_Bullet
    global movement_speed
    global Bullets
    global AllCoins
    global coin_timer
    global coin_timer_counter
    global coin_delay
    global coin_ammount
    global coin_delay_counter
    global coin_spawn
    global how_many_coinspeed
    global how_many_coindelay
    global coinadd
    global coinadd_counter
    global listnam
    global oldscore
    global shop_bullet_speed
    global shop_movement_speed
    global shop_extra_bullet
    global shop_coin_speed
    global shop_coin_delay
    global shop_coin_ammount
    global start
    global CoinObject
    global coins
    global gcoin
    global fast_enemy_counter
    global enemy_counter
    global fast_enemy_speed
    global fast_enemy

    # Pygame Setup
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Sets the screen size
    pygame.display.set_caption("Ginza Arcade")  # sets the caption
    charRect3 = pygame.Rect((0, 0), (500, 500))
    space = pygame.image.load(os.path.abspath(filep + "space.png"))
    space = pygame.transform.scale(space, charRect3.size)
    space = space.convert()
    clock = pygame.time.Clock()

    # All starting values
    swait = 0
    points_buy = 5
    fast_enemy_counter = 0
    fast_enemy = random.randint(0, 5)
    fast_enemy_speed = 50
    start = False
    how_many_bullets = 1
    shop_bullet_speed = 50
    shop_movement_speed = 50
    shop_extra_bullet = 500
    shop_coin_speed = 50
    shop_coin_delay = 50
    shop_coin_ammount = 50
    listnam = False
    coin_timer_counter = 0
    coin_delayer = 1000
    coin_delay_counter = 0
    name = ""
    coin_timer = 1000
    coins = 0
    coinadd = 5
    coinadd_counter = 0
    how_many_coinspeed = 0
    how_many_coindelay = 0
    wait = 0
    speed = 0
    move = 0
    enemy_speed = 500
    answer = ''
    total_level = 10
    movement = 500
    bullet_timer = 0
    bullet_speed = 500
    move_timer = 0
    game_over_2 = False
    enemy_ship_location = 0
    points_counter = 0
    bullet_counter = -1
    shop = False
    gameExit = False
    game_over = False
    left_key = 0
    right_key = 0
    enemy_counter = 0
    enemy_ship_x = 20
    enemy_ship_y = 20
    start_level = 0
    level = 10
    enemy_death_count = 0
    continue_level = 0
    all_enemy_counter = 0
    enter = False
    enter2 = False
    inputed_name = False
    global yesorno
    yesorno = False
    while inputed_name == False:  # This code is for entering your name
        list_of_names = {}
        with open(names_text) as f:
            for line in f:
                (key, val) = line.split()
                list_of_names[str(key)] = int(val)
        if yesorno == False:
            pygame.init()
            pygame.mixer.init()
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Ginza Arcade")
            clock = pygame.time.Clock()

            screen.blit(space, [0, 0])

            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Enter Name: ", True, AQUA)
            textrect4 = text4.get_rect()
            textrect4.centerx = 250
            textrect4.centery = 200
            screen.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Press enter to continue!", True, AQUA)
            textrect4 = text4.get_rect()
            textrect4.centerx = 250
            textrect4.centery = 300
            screen.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render("Welcome to Ginza Arcade! ", True, AQUA)
            textrect4 = text4.get_rect()
            textrect4.centerx = 250
            textrect4.centery = 12
            screen.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render(name, True, RED)
            textrect4 = text4.get_rect()
            textrect4.centerx = 250
            textrect4.centery = 250
            screen.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 18)  # This code displays letters onto the screen
            text4 = basicfont4.render("Controls: ", True, RED)
            textrect4 = text4.get_rect()
            textrect4.centerx = 250
            textrect4.centery = 375
            screen.blit(text4, textrect4)

            controls = pygame.sprite.Group()
            control = Controls()
            controls.add(control)
            scontrol = SControls()
            controls.add(scontrol)

            controls.draw(screen)

            pygame.display.flip()
            pygame.display.update()
            for event in pygame.event.get():  # This code is to see what keys you press and input them into name
                if event.type == pygame.QUIT:  # If you click on the X on the screen it asks if you want to close the game
                    exit()
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER:  # If you click enter it jumps to the game if theres no one in the list that has that name
                        enter = True
                    if event.key == pygame.K_a:
                        name = name + "A"
                    if event.key == pygame.K_b:
                        name = name + "B"
                    if event.key == pygame.K_c:
                        name = name + "C"
                    if event.key == pygame.K_d:
                        name = name + "D"
                    if event.key == pygame.K_e:
                        name = name + "E"
                    if event.key == pygame.K_f:
                        name = name + "F"
                    if event.key == pygame.K_g:
                        name = name + "G"
                    if event.key == pygame.K_h:
                        name = name + "H"
                    if event.key == pygame.K_i:
                        name = name + "I"
                    if event.key == pygame.K_j:
                        name = name + "J"
                    if event.key == pygame.K_k:
                        name = name + "K"
                    if event.key == pygame.K_l:
                        name = name + "L"
                    if event.key == pygame.K_m:
                        name = name + "M"
                    if event.key == pygame.K_n:
                        name = name + "N"
                    if event.key == pygame.K_o:
                        name = name + "O"
                    if event.key == pygame.K_p:
                        name = name + "P"
                    if event.key == pygame.K_q:
                        name = name + "Q"
                    if event.key == pygame.K_r:
                        name = name + "R"
                    if event.key == pygame.K_s:
                        name = name + "S"
                    if event.key == pygame.K_t:
                        name = name + "T"
                    if event.key == pygame.K_u:
                        name = name + "U"
                    if event.key == pygame.K_v:
                        name = name + "V"
                    if event.key == pygame.K_w:
                        name = name + "W"
                    if event.key == pygame.K_x:
                        name = name + "X"
                    if event.key == pygame.K_y:
                        name = name + "Y"
                    if event.key == pygame.K_z:
                        name = name + "Z"
                    if event.key == pygame.K_BACKSPACE:  # if you click backspace it gets rid of a letter in name
                        name = list(name)
                        del name[-1]
                        name = ''.join(name)
            if enter == True:  # checks to see if name is in the list of people who played before and if yes you can choose to sign back in or not
                if not (name in list_of_names):
                    inputed_name = True
                    oldscore = -1
                else:
                    yesorno = True
        else:
            screen.blit(space, [0, 0])

            basicfont4 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
            text4 = basicfont4.render(name, True, RED)
            textrect4 = text4.get_rect()
            textrect4.centerx = 250
            textrect4.centery = 200
            screen.blit(text4, textrect4)

            basicfont4 = pygame.font.Font(words, 14)  # This code displays letters onto the screen
            text4 = basicfont4.render("has already played want to log back in?(type yes or no)", True, AQUA)
            textrect4 = text4.get_rect()
            textrect4.centerx = 250
            textrect4.centery = 250
            screen.blit(text4, textrect4)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If you click on the X on the screen it asks if you want to close the game
                    exit()
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        answer = answer + "Y"
                    if event.key == pygame.K_e:
                        answer = answer + "E"
                    if event.key == pygame.K_s:
                        answer = answer + "S"
                    if event.key == pygame.K_n:
                        answer = answer + "N"
                    if event.key == pygame.K_o:
                        answer = answer + "O"
                    if event.key == pygame.K_BACKSPACE:
                        answer = list(answer)
                        del answer[-1]
                        answer = ''.join(answer)
                    if event.key == pygame.K_KP_ENTER:
                        enter2 = True
            basicfont4 = pygame.font.Font(words, 64)  # This code displays letters onto the screen
            text4 = basicfont4.render(answer, True, AQUA)
            textrect4 = text4.get_rect()
            textrect4.centerx = 250
            textrect4.centery = 400
            screen.blit(text4, textrect4)

            if enter2 == True:  # This is the last conformation step to make sure you want to sign back in
                if answer == "YES":
                    # HighScore Setup

                    with open(names_text) as f:
                        for line in f:
                            (key, val) = line.split()
                            list_of_names[str(key)] = int(val)
                    inputed_name = True
                    oldscore = list_of_names[name]
                    inputed_name = True
                if answer == "NO":
                    yesorno = False
                    name = ''
                    enter = False
                    answer = ''
                enter2 = False
            pygame.display.flip()
            pygame.display.update()
    game_over = False
    pygame.init()
    while not gameExit:
        if start == False:
            global goodship
            global enemyship

            charRect = pygame.Rect((0, 0), (50, 50))
            goodship = pygame.image.load(os.path.abspath(filep + "goodship.png"))
            goodship = pygame.transform.scale(goodship, charRect.size)
            goodship = goodship.convert()

            enemyship = pygame.image.load(os.path.abspath(filep + "enemyship.png"))
            enemyship = pygame.transform.scale(enemyship, charRect.size)
            enemyship = enemyship.convert()

            charRect2 = pygame.Rect((0, 0), (10, 20))
            rocketpic = pygame.image.load(os.path.abspath(filep + "rocketpic.png"))
            rocketpic = pygame.transform.scale(rocketpic, charRect2.size)
            rocketpic = rocketpic.convert()

            charRect3 = pygame.Rect((0, 0), (40, 40))
            buypic = pygame.image.load(os.path.abspath(filep + "buypic.png"))
            buypic = pygame.transform.scale(buypic, charRect3.size)
            buypic = buypic.convert()

            charRect4 = pygame.Rect((0, 0), (20, 20))
            gcoin = pygame.image.load(os.path.abspath(filep + "gcoin.png"))
            gcoin = pygame.transform.scale(gcoin, charRect4.size)
            gcoin = gcoin.convert()

            # Object Setup
            Main = pygame.sprite.Group()
            Bullets = pygame.sprite.Group()
            PowerUps = pygame.sprite.Group()
            enemy_ships = pygame.sprite.Group()
            AllCoins = pygame.sprite.Group()
            CoinObject = Coin_Object()
            AllCoins.add(CoinObject)
            extra_bullet_object = Extra_Bullet()
            bullet_speed_object = Bullet_Speed()
            PowerUps.add(bullet_speed_object)
            PowerUps.add(extra_bullet_object)
            movement_speed = Movement_Speed()
            points_exchange = Points_Exchange()
            coin_spawn = Coin_Spawn()
            coin_delay = Coin_Delay()
            coin_ammount = Coin_Ammount()
            PowerUps.add(points_exchange)
            PowerUps.add(coin_ammount)
            PowerUps.add(coin_delay)
            PowerUps.add(coin_spawn)
            PowerUps.add(movement_speed)
            ship = Ship()
            Main.add(ship)
            start = True

        while game_over != False:  # This is the main Code
            screen.blit(space, [0, 0])
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If you click on the X on the screen it asks if you want to close the game
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # Below are the keys that you press during the game
                    left_key = 1
                    right_key = 0
                elif event.key == pygame.K_RIGHT:
                    right_key = 1
                    left_key = 0
                elif event.key == pygame.K_UP:
                    if how_many_bullets > (len(Bullets.sprites())):
                        bullet2 = Bullet()
                        Bullets.add(bullet2)
                elif event.key == pygame.K_a:
                    left_key = 1
                    right_key = 0
                elif event.key == pygame.K_d:
                    right_key = 1
                    left_key = 0
                elif event.key == pygame.K_w:
                    if how_many_bullets > (len(Bullets.sprites())):
                        bullet2 = Bullet()
                        Bullets.add(bullet2)

        if shop == True:  # This is the start of the shop code
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_p]:
                if swait > 5:
                    swait = 0
                    shop = not shop
            swait += 1
            pygame.init()
            pygame.mixer.init()
            screen2 = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Ginza Arcade")

            screen2.blit(space, [0, 0])
            basicfont4 = pygame.font.Font(words, 15)  # This code displays letters onto the screen

            if move <= 10:
                text5 = basicfont4.render("Movement Speed: " + str(move), True, WHITE)
                textrect5 = text5.get_rect()
                textrect5.left = (0)
                textrect5.y = (320)
                screen2.blit(text5, textrect5)

                text5 = basicfont4.render("Movement Speed", True, AQUA)
                textrect5 = text5.get_rect()
                textrect5.centerx = 210
                textrect5.centery = 90
                screen2.blit(text5, textrect5)

                text5 = basicfont4.render("Cost: " + str(shop_movement_speed), True, GREEN)
                textrect5 = text5.get_rect()
                textrect5.centerx = 210
                textrect5.centery = 32
                screen2.blit(text5, textrect5)
            else:
                text5 = basicfont4.render("Movement Speed: MAX", True, RED)
                textrect5 = text5.get_rect()
                textrect5.left = (0)
                textrect5.y = (320)
                screen2.blit(text5, textrect5)
                PowerUps.remove(movement_speed)

            if speed <= 10:
                text5 = basicfont4.render("Bullet Speed", True, AQUA)
                textrect5 = text5.get_rect()
                textrect5.centerx = 70
                textrect5.centery = 90
                screen2.blit(text5, textrect5)

                text5 = basicfont4.render("Cost: " + str(shop_bullet_speed), True, GREEN)
                textrect5 = text5.get_rect()
                textrect5.centerx = 70
                textrect5.centery = 32
                screen2.blit(text5, textrect5)

                text5 = basicfont4.render("Bullet Speed: " + str(speed), True, WHITE)
                textrect5 = text5.get_rect()
                textrect5.left = (0)
                textrect5.y = (340)
                screen2.blit(text5, textrect5)
            else:
                text5 = basicfont4.render("Bullet Speed: MAX", True, RED)
                textrect5 = text5.get_rect()
                textrect5.left = (0)
                textrect5.y = (340)
                screen2.blit(text5, textrect5)
                PowerUps.remove(bullet_speed_object)

            if how_many_bullets <= 5:
                text5 = basicfont4.render("Extra Bullet", True, AQUA)
                textrect5 = text5.get_rect()
                textrect5.centerx = 360
                textrect5.centery = 90
                screen2.blit(text5, textrect5)
                text5 = basicfont4.render("Cost: " + str(shop_extra_bullet), True, GREEN)
                textrect5 = text5.get_rect()
                textrect5.centerx = 360
                textrect5.centery = 32
                screen2.blit(text5, textrect5)

                text5 = basicfont4.render("Bullets: " + str(how_many_bullets), True, WHITE)
                textrect5 = text5.get_rect()
                textrect5.left = (0)
                textrect5.y = (360)
                screen2.blit(text5, textrect5)
            else:
                text5 = basicfont4.render("Bullets: MAX", True, RED)
                textrect5 = text5.get_rect()
                textrect5.left = (0)
                textrect5.y = (360)
                screen2.blit(text5, textrect5)
                PowerUps.remove(extra_bullet_object)

            if how_many_coinspeed <= 10:
                text6 = basicfont4.render("Coin Speed", True, AQUA)
                textrect6 = text6.get_rect()
                textrect6.centerx = 70
                textrect6.centery = 178
                screen2.blit(text6, textrect6)
                text6 = basicfont4.render("Cost: " + str(shop_coin_speed), True, GREEN)
                textrect6 = text6.get_rect()
                textrect6.centerx = 70
                textrect6.centery = 120
                screen2.blit(text6, textrect6)

                text6 = basicfont4.render("Coin Spawn: " + str(how_many_coinspeed), True, WHITE)
                textrect6 = text6.get_rect()
                textrect6.left = (0)
                textrect6.y = (380)
                screen2.blit(text6, textrect6)
            else:
                text6 = basicfont4.render("Coin Spawn: MAX", True, RED)
                textrect6 = text6.get_rect()
                textrect6.left = (0)
                textrect6.y = (380)
                screen2.blit(text6, textrect6)
                PowerUps.remove(coin_spawn)

            if how_many_coindelay <= 10:
                text6 = basicfont4.render("Coin Delay", True, AQUA)
                textrect6 = text6.get_rect()
                textrect6.centerx = 210
                textrect6.centery = 178
                screen2.blit(text6, textrect6)
                text6 = basicfont4.render("Cost: " + str(shop_coin_delay), True, GREEN)
                textrect6 = text6.get_rect()
                textrect6.centerx = 210
                textrect6.centery = 120
                screen2.blit(text6, textrect6)

                text6 = basicfont4.render("Coin Delay: " + str(how_many_coindelay), True, WHITE)
                textrect6 = text6.get_rect()
                textrect6.left = (0)
                textrect6.y = (400)
                screen2.blit(text6, textrect6)
            else:
                text6 = basicfont4.render("Coin Delay: MAX", True, RED)
                textrect6 = text6.get_rect()
                textrect6.left = (0)
                textrect6.y = (400)
                screen2.blit(text6, textrect6)
                PowerUps.remove(coin_delay)

            text6 = basicfont4.render("1 Point", True, YELLOW)
            textrect6 = text6.get_rect()
            textrect6.centerx = 300
            textrect6.centery = 315
            screen2.blit(text6, textrect6)
            text6 = basicfont4.render("Cost: " + str(points_buy), True, GREEN)
            textrect6 = text6.get_rect()
            textrect6.centerx = 300
            textrect6.centery = 380
            screen2.blit(text6, textrect6)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If you click on the X on the screen it asks if you want to close the game
                    gameExit = True
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if bullet_speed_object.rect.collidepoint(pos):
                        if speed <= 10:
                            if coins >= shop_bullet_speed:  # This makes sure you have enough coins
                                bullet_speed -= 25
                                coins -= shop_bullet_speed
                                shop_bullet_speed += round(shop_bullet_speed * .5)
                                speed += 1
                            elif (wait < 1):
                                wait = wait + 25  # if not then add a wait time that will display a sign saying Not enough coins
                    if how_many_bullets <= 5:
                        if extra_bullet_object.rect.collidepoint(pos):
                            if coins >= shop_extra_bullet:
                                how_many_bullets += 1
                                coins -= shop_extra_bullet
                                shop_extra_bullet += round(shop_extra_bullet * 2)
                            elif (wait < 1):
                                wait = wait + 25
                    if move <= 10:
                        if movement_speed.rect.collidepoint(pos):
                            if coins >= shop_movement_speed:
                                movement -= 25
                                coins -= shop_movement_speed
                                shop_movement_speed += round(shop_movement_speed * .5)
                                move += 1
                            elif (wait < 1):
                                wait = wait + 25

                    if how_many_coinspeed <= 10:
                        if coin_spawn.rect.collidepoint(pos):
                            if coins >= shop_coin_speed:
                                coin_timer -= 100
                                coins -= shop_coin_speed
                                shop_coin_speed += round(shop_coin_speed * .5)
                                how_many_coinspeed += 1
                            elif (wait < 1):
                                wait = wait + 25
                    if how_many_coindelay <= 10:
                        if coin_delay.rect.collidepoint(pos):
                            if coins >= shop_coin_delay:
                                coin_delayer += 100
                                coins -= shop_coin_delay
                                shop_coin_delay += round(shop_coin_delay * .5)
                                how_many_coindelay += 1
                            elif (wait < 1):
                                wait = wait + 25

                    if coin_ammount.rect.collidepoint(pos):
                        if coins >= shop_coin_ammount:
                            coinadd += round(coinadd * .5)
                            coins -= shop_coin_ammount
                            shop_coin_ammount += round(shop_coin_ammount * .5)
                            coinadd_counter += 1
                        elif (wait < 1):
                            wait = wait + 25

                    if points_exchange.rect.collidepoint(pos):
                        if coins >= points_buy:
                            points_counter += 1
                            coins -= points_buy
                            points_buy += round(points_buy * .5)
                        elif (wait < 1):
                            wait = wait + 25

            if wait >= 1:
                basicfont4 = pygame.font.Font(words, 42)  # This code displays letters onto the screen
                text4 = basicfont4.render("Not Enough Coins!", True, RED)
                textrect4 = text4.get_rect()
                textrect4.centerx = 250
                textrect4.centery = 250
                screen2.blit(text4, textrect4)
                wait -= 1

            basicfont4 = pygame.font.Font(words, 15)  # This code displays letters onto the screen
            text4 = basicfont4.render("Press P to leave shop!", True, AQUA)
            textrect4 = text4.get_rect()
            textrect4.centerx = 250
            textrect4.centery = 480
            screen2.blit(text4, textrect4)

            text6 = basicfont4.render("Coins: " + str(coins), True, YELLOW)
            textrect6 = text6.get_rect()
            textrect6.right = 500
            screen.blit(text6, textrect6)

            text6 = basicfont4.render("Coin Ammount", True, AQUA)
            textrect6 = text6.get_rect()
            textrect6.centerx = 360
            textrect6.centery = 178
            screen2.blit(text6, textrect6)
            text6 = basicfont4.render("Cost: " + str(shop_coin_ammount), True, GREEN)
            textrect6 = text6.get_rect()
            textrect6.centerx = 360
            textrect6.centery = 120
            screen2.blit(text6, textrect6)

            text6 = basicfont4.render("Coin Ammount: " + str(coinadd), True, YELLOW)
            textrect6 = text6.get_rect()
            textrect6.left = (0)
            textrect6.y = (420)
            screen2.blit(text6, textrect6)

            # Stats:
            text5 = basicfont4.render("Stats: ", True, VIOLET)
            textrect5 = text5.get_rect()
            textrect5.left = (0)
            textrect5.y = (300)
            screen2.blit(text5, textrect5)

            PowerUps.draw(screen)

            mpos = pygame.mouse.get_pos()

            pygame.display.flip()
            pygame.display.update()
        if shop == False:  # The part of the code that makes it happen
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_p]:
                if swait > 5:
                    swait = 0
                    shop = not shop
            swait += 1
            wait = 0
            if start_level == 0:  # Checks if its a new level and if yes then make new ships
                levels(level)
            if len(enemy_ships.sprites()) == 0:
                start_level = 0
                level += 1
                total_level = total_level + 1
                coins = coins + coinadd

            all_enemy_counter += 1
            if all_enemy_counter > enemy_speed:
                for i in range(len(enemy_ships.sprites())):
                    if i != fast_enemy:
                        enemy_ships.sprites()[i].update()
                all_enemy_counter = 0

            fast_enemy_counter += 1
            if fast_enemy_counter > fast_enemy_speed:
                try:
                    enemy_ships.sprites()[fast_enemy].update()
                    fast_enemy_counter = 0
                except IndexError:
                    fast_enemy = random.randint(0, len(enemy_ships.sprites()))
            move_timer += 100
            if move_timer >= movement:  # Movement speed
                if right_key >= 1:
                    if ship.rect.right != WIDTH:
                        ship.update(0)
                if left_key == 1:
                    if ship.rect.left != 0:
                        ship.update(1)
                move_timer = 0

            bullet_timer += 100
            if bullet_timer >= bullet_speed:
                try:
                    for i in range(len(Bullets.sprites())):
                        Bullets.sprites()[i].update()
                except IndexError:
                    continue
                bullet_timer = 0

            basicfont1 = pygame.font.Font(words, 15)
            text1 = basicfont1.render('Level: ' + str(total_level - 9), True, RED)
            textrect1 = text1.get_rect()
            textrect1.right = 500

            screen.blit(text1, textrect1)

            text2 = basicfont1.render('Points: ' + str(points_counter), True, GREEN)
            textrect2 = text2.get_rect()
            textrect2.left = 0

            screen.blit(text2, textrect2)

            text3 = basicfont1.render(name, True, AQUA)
            textrect3 = text3.get_rect()
            textrect3.centerx = 250
            textrect3.centery = 7

            screen.blit(text3, textrect3)

            text6 = basicfont1.render("Coins: " + str(coins), True, YELLOW)
            textrect6 = text6.get_rect()
            textrect6.right = 500
            textrect6.bottom = 450

            screen.blit(text6, textrect6)

            # Draw/Render
            coin_timer_counter += 1
            if coin_timer_counter >= coin_timer:
                AllCoins.draw(screen)
                coin_delay_counter += 1
                if coin_delayer == coin_delay_counter:
                    CoinObject.update()
                    AllCoins.sprites()[0].update()
                    coin_delay_counter = 0
                    coin_timer_counter = 0

            Bullets.draw(screen)
            Main.draw(screen)
            enemy_ships.draw(screen)
            # after drawwing flip display
            pygame.display.flip()

            pygame.display.update()
            screen.blit(space, [0, 0])
            if game_over_2 == True:
                pygame.quit()
                break


game_over_2 = False
done = False
while done == False:
    if game_over_2 == False:
        gameLoop()
        game_over_2 = True
    if game_over_2 == True:
        if listnam == False:
            if points_counter > oldscore:
                f = open(names_text, "r")
                lines = f.readlines()
                f.close()
                s = open(names_text, "w")
                for line in lines:
                    if line != (name + " " + str(oldscore)):
                        s.write(line)
                s.close()

                t = open(names_text, 'a')
                t.write("\n" + name + " " + str(points_counter))
                t.close()
                listnam = True

                for line in fileinput.FileInput(names_text, inplace=1):
                    if line.rstrip():
                        print(line, end='')
            if oldscore == -1 and listnam == False:
                p = open('list_of_names', 'a')
                p.write("\n" + name + " " + str(points_counter))
                p.close()
                listnam = True
        pygame.init()
        pygame.mixer.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("High Scores:")
        clock = pygame.time.Clock()
        charRect3 = pygame.Rect((0, 0), (500, 500))
        space = pygame.image.load(os.path.abspath(filep + "space.png"))
        space = pygame.transform.scale(space, charRect3.size)
        space = space.convert()

        screen.blit(space, [0, 0])

        list_of_names = {}
        with open(names_text) as f:
            for line in f:
                (key, val) = line.split()
                list_of_names[str(key)] = int(val)
        f.close()

        allnames = list_of_names  # sorting code
        allnames = sorted(allnames.items(), key=operator.itemgetter(1))
        allnames.reverse()

        basicfont4 = pygame.font.Font(words, 12)  # This code displays letters onto the screen
        text4 = basicfont4.render(("1: " + str(allnames[0][0]) + "............................" + str(allnames[0][1])),
                                  True, AQUA)
        textrect4 = text4.get_rect()
        textrect4.centerx = 250
        textrect4.centery = 50
        screen.blit(text4, textrect4)

        text4 = basicfont4.render(("2: " + str(allnames[1][0]) + "............................" + str(allnames[1][1])),
                                  True, AQUA)
        textrect4 = text4.get_rect()
        textrect4.centerx = 250
        textrect4.centery = 80
        screen.blit(text4, textrect4)

        text4 = basicfont4.render(("3: " + str(allnames[2][0]) + "............................" + str(allnames[2][1])),
                                  True, AQUA)
        textrect4 = text4.get_rect()
        textrect4.centerx = 250
        textrect4.centery = 120
        screen.blit(text4, textrect4)

        text4 = basicfont4.render(("4: " + str(allnames[3][0]) + "............................" + str(allnames[3][1])),
                                  True, AQUA)
        textrect4 = text4.get_rect()
        textrect4.centerx = 250
        textrect4.centery = 150
        screen.blit(text4, textrect4)

        text4 = basicfont4.render(("5: " + str(allnames[4][0]) + "............................" + str(allnames[4][1])),
                                  True, AQUA)
        textrect4 = text4.get_rect()
        textrect4.centerx = 250
        textrect4.centery = 180
        screen.blit(text4, textrect4)

        text4 = basicfont4.render(("6: " + str(allnames[5][0]) + "............................" + str(allnames[5][1])),
                                  True, AQUA)
        textrect4 = text4.get_rect()
        textrect4.centerx = 250
        textrect4.centery = 210
        screen.blit(text4, textrect4)

        text4 = basicfont4.render(("7: " + str(allnames[6][0]) + "............................" + str(allnames[6][1])),
                                  True, AQUA)
        textrect4 = text4.get_rect()
        textrect4.centerx = 250
        textrect4.centery = 240
        screen.blit(text4, textrect4)

        text4 = basicfont4.render(("8: " + str(allnames[7][0]) + "............................" + str(allnames[7][1])),
                                  True, AQUA)
        textrect4 = text4.get_rect()
        textrect4.centerx = 250
        textrect4.centery = 270
        screen.blit(text4, textrect4)

        text4 = basicfont4.render(("9: " + str(allnames[8][0]) + "............................" + str(allnames[8][1])),
                                  True, AQUA)
        textrect4 = text4.get_rect()
        textrect4.centerx = 250
        textrect4.centery = 300
        screen.blit(text4, textrect4)

        text4 = basicfont4.render(("10: " + str(allnames[9][0]) + "............................" + str(allnames[9][1])),
                                  True, AQUA)
        textrect4 = text4.get_rect()
        textrect4.centerx = 250
        textrect4.centery = 330
        screen.blit(text4, textrect4)

        text4 = basicfont4.render("Press q to quit or c to continue", True, AQUA)
        textrect4 = text4.get_rect()
        textrect4.centerx = 250
        textrect4.centery = 360
        screen.blit(text4, textrect4)

        basicfont5 = pygame.font.Font(words, 24)  # This code displays letters onto the screen
        text4 = basicfont5.render("Credits: ", True, RED)
        textrect4 = text4.get_rect()
        textrect4.centerx = 75
        textrect4.centery = 400
        screen.blit(text4, textrect4)

        text4 = basicfont4.render("Game Developer -- Jason Melnik", True, RED)
        textrect4 = text4.get_rect()
        textrect4.centerx = 250
        textrect4.centery = 425
        screen.blit(text4, textrect4)

        text4 = basicfont4.render("Graphics Design - Carrie-lynn LaFranchi", True, RED)
        textrect4 = text4.get_rect()
        textrect4.centerx = 250
        textrect4.centery = 450
        screen.blit(text4, textrect4)

        pygame.display.flip()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If you click on the X on the screen it asks if you want to close the game
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Quits the whole game
                    gameExit = True
                    game_over_2 = True
                    pygame.quit()
                    done = True
                    break
                if event.key == pygame.K_c:
                    game_over_2 = False
                    pygame.quit()
                    break