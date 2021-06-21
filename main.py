import pygame

#initiate pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,900))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False