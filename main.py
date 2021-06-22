import pygame
import random
import math

#initiate pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#background image
background = pygame.image.load('images/background.jpg')
#title and icon 
pygame.display.set_caption("space Invader")
icon =pygame.image.load('images/alien.png') # how to upload an icon on a window header
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('images/astronomy.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(playerImg, (x,y))

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('images/monster.png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))

#Bullet (ready state means that you can not see the bullet)
bulletImg = pygame.image.load('images/bullet.png')
bulletX = 0
bulletY = 480
buletX_change = 0
bulletY_change = 1
bullet_state = "ready"
score = 0
collision_image= pygame.image.load('images/explosion.png')

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def is_collision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY,2))
    if distance <27:
        return True
    else:
        return False
   


#Game loop
running = True
while running:
    screen.fill((0, 0, 0)) # red green blue
    # background Image
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
    
        # if a keystroke is placed check if it is left or right.
        if event.type == pygame.KEYDOWN: # KEYDOWN is when we place a keyboard 
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY) 

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


# making sure a player does not get out of screen
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX>= 736:
        playerX = 736

#manaing enemy movements
    enemyX += enemyX_change
    for i in range(num_of_enemies):
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        collision = is_collision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
        
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i],enemyY[i], i)

#bullet movement
    if bulletY <=0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY,)
        bulletY -= bulletY_change

    #collision 
  

    player(playerX,playerY)
   
    pygame.display.update()