import pygame
import random
import sys

monitor = None

colorL = ["red", "green", "blue", "yellow", "magenta", "orange"]
color = random.choice(colorL)
color = "white"

pygame.init()
x = 1920 
y = 1080

monitor = pygame.display.set_mode((x, y))
dao = pygame.image.load("dao.png")

speed = 2
tx, ty = 0, 0
run = False
keys = []


while True : 
    monitor.fill(color)
    
    if (run) :
        tx = 0
        ty = 0
    elif (len(keys) != 0) :
        if (pygame.K_RIGHT in keys and (int(x / 2 + dao.get_width() / 2) + tx + speed) in range(0, 1920)) :
            tx += speed
        if (pygame.K_LEFT in keys and (int(x / 2 - dao.get_width() / 2) + tx - speed) in range(0, 1920)) :
            tx -= speed
        if (pygame.K_UP in keys and (int(y / 2 - dao.get_height() / 2) + ty - speed) in range(0, 1080)) :
            ty -= speed
        if (pygame.K_DOWN in keys and (int(y / 2 + dao.get_height() / 2) + ty + speed) in range(0, 1080)) :
            ty += speed
    
    monitor.blit(dao, (int(x / 2 - dao.get_width() / 2) + tx, int(y / 2 - dao.get_height() / 2) + ty)) 
    pygame.display.update()
    
    for e in pygame.event.get() :
        if (e.type in [pygame.QUIT]) :
            pygame.quit()
            sys.exit()
        if (e.type in [pygame.KEYDOWN]) :
            if (e.key == pygame.K_SPACE) :
                run = True
            else :
                keys.append(e.key)
        if (e.type in [pygame.KEYUP]) :
            if (e.key == pygame.K_SPACE) :
                run = False
            else :
                keys.remove(e.key)