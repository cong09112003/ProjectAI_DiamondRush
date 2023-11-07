import pygame
import sys
from pygame.locals import *
pygame.init()
DISPLAYSURF=pygame.display.set_mode((500,400))
pygame.display.set_caption("Hello, world!")
# color
GRAY = (100,100,100)
NAVYBLUE=(60,60,60)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
ORANGE=(255,128,0)
PURPLE=(255,0,255)
CYAN=(0,255,255)
#Rect objects
# x, y, width, height
Myrect = pygame.Rect(50,50,100,100)
print(Myrect.centerx)
while True:
    for event in pygame.event.get():
        # constant variable
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()  
    pygame.display.update()