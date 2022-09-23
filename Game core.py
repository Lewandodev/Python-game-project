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

    for event in pygame.event.get(): #event is anything that happens "from the user" like using movement keys or clicking
        if event.type==pygame.QUIT:
            run=False

