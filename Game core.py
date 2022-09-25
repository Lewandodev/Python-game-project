import pygame

pygame.init() #initialising pygame

window=pygame.display.set_mode((600,600)) #displaying the window

pygame.display.set_caption("Python Game Project")

screen_border=600
x=50
y=425
width=30
height=60
velocity=10 #speed of our character

run=True
while run is True:
    pygame.time.delay(100)

    for event in pygame.event.get(): #event is anything that happens "from the user" like using movement keys or clicking
        if event.type==pygame.QUIT:  #thanks to this function we wont get error after exiting game
            run=False

    #movement
    #coordinates of object are stored in top left of the character
    move_keys=pygame.key.get_pressed()
    if move_keys[pygame.K_LEFT] and x>velocity:
        x-=velocity
    elif move_keys[pygame.K_RIGHT] and x<screen_border-width-velocity:
        x+=velocity
    elif move_keys[pygame.K_UP] and y > velocity:
        y-=velocity
    elif move_keys[pygame.K_DOWN] and y < screen_border-height-velocity:
        y+=velocity

    window.fill((0,0,0))
    #creating character
    pygame.draw.rect(window, (0,255,0),(x,y,width,height)) #we put our "character on surface (window) then add parameters
    pygame.display.update()



pygame.quit()
