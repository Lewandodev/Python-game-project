import pygame

pygame.init() #initialising pygame

window=pygame.display.set_mode((600,600)) #displaying the window

pygame.display.set_caption("Python Game Project")

x=50
y=50
width=30
height=60
velocity=5

run=True
while run is True:
    pygame.time.delay(100)