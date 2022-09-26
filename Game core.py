import pygame

pygame.init() #initialising pygame

window=pygame.display.set_mode((600,480)) #displaying the window

pygame.display.set_caption("Python Game Project")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png')]
background = pygame.image.load('bgr.jpg')
char = pygame.image.load('Standing.png')

clock=pygame.time.Clock()

screen_border=600
x=50
y=340
width=64
height=64
velocity=3 #speed of our character

is_jump=False
jump_count=10

#which direction character is moving
left=False
right=False
walking_count=0


def redraw_game_window():
    global walking_count
    window.blit(background,(0,0))
    # creating character
    if walking_count+1>=9: #3 sprites which I will display for 3 frames therefore 3*3. That's how many times we will go through the loop before it changes the image
        walking_count=0 # In 9 FPS changing image every 3 loops makes the character look like its moving
    if left:
        window.blit(walkLeft[walking_count//3],(x,y))
        walking_count+=1
    elif right:
        window.blit(walkRight[walking_count//3],(x,y))
        walking_count+=1
    else:
        window.blit(char,(x,y))

    pygame.display.update()

run=True
while run is True:
    clock.tick(27) #changed delay according to our FPS

    for event in pygame.event.get(): #event is anything that happens "from the user" like using movement keys or clicking
        if event.type==pygame.QUIT:  #thanks to this function we wont get error after exiting game
            run=False

    #movement
    #coordinates of object are stored in top left of the character
    move_keys=pygame.key.get_pressed()
    if move_keys[pygame.K_LEFT] and x>velocity:
        x-=velocity
        left=True
        right=False

    elif move_keys[pygame.K_RIGHT] and x<screen_border-width-velocity: #substracting by width moves our border making the character crossing attempts impossible
        x+=velocity
        left = False
        right = True
    else:
        right=False
        left=False
        walking_count=0

    if not(is_jump):
        '''if move_keys[pygame.K_UP] and y > velocity:
            y-=velocity                         #going up and down will be useless in a paltformer game
        elif move_keys[pygame.K_DOWN] and y < screen_border-height-velocity:
            y+=velocity'''
        if move_keys[pygame.K_SPACE]:
            is_jump = True
            left = False
            right = False
            walking_count=0
    else:
        if jump_count>=-10: #jumping is moving character by ceratin amount of pixels
            neg=1
            if jump_count<0:
                neg=-1
            y-=(jump_count**2)/2*neg #how many pxiels will our character move
            jump_count-=1
            #aaa
        else:
            is_jump = False
            jump_count=10
    redraw_game_window()




pygame.quit()
