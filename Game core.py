import pygame

pygame.init() #initialising pygame

window=pygame.display.set_mode((600,480)) #displaying the window

pygame.display.set_caption("Python Game Project")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
background = pygame.image.load('bgr.jpg')
char = pygame.image.load('Standing.png')

clock=pygame.time.Clock()

screen_border=600

#getting rid of globals
class player(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.velocity=5 #speed of our character
        self.is_jump=False
        self.jump_count=10
        self.left=False #which direction character is moving
        self.rigt=False
        self.walking_count=0
    def draw(window):
        # creating character
        if walking_count + 1 >= 27:  # 9 sprites which I will display for 3 frames therefore 9*3. That's how many times we will go through the loop before it changes the image
            walking_count = 0  # In 27 FPS changing image every 3 loops makes the character look like its moving
        if left:
            window.blit(walkLeft[walking_count // 3], (x, y))
            walking_count += 1
        elif right:
            window.blit(walkRight[walking_count // 3], (x, y))
            walking_count += 1
        else:
            window.blit(char, (x, y))



def redraw_game_window():
    global walking_count
    window.blit(background,(0,0))

    pygame.display.update()

character=player(300,410,64,64)
run=True
while run is True:
    clock.tick(54) #changed delay according to our FPS

    for event in pygame.event.get(): #event is anything that happens "from the user" like using movement keys or clicking
        if event.type==pygame.QUIT:  #thanks to this function we wont get error after exiting game
            run=False

    #movement
    #coordinates of object are stored in top left of the character
    move_keys=pygame.key.get_pressed()
    if move_keys[pygame.K_LEFT] and character.x>character.velocity:
        character.x-=character.velocity
        character.left=True
        character.right=False

    elif move_keys[pygame.K_RIGHT] and character.x<screen_border-character.width-character.velocity: #substracting by width moves our border making the character crossing attempts impossible
        character.x+=character.velocity
        left = False
        right = True
    else:
        character.right=False
        character.left=False
        character.walking_count=0

    if not(character.is_jump):
        '''if move_keys[pygame.K_UP] and y > velocity:
            y-=velocity                         #going up and down will be useless in a paltformer game
        elif move_keys[pygame.K_DOWN] and y < screen_border-height-velocity:
            y+=velocity'''
        if move_keys[pygame.K_SPACE]:
            character.is_jump = True
            character.left = False
            character.right = False
            character.walking_count=0
    else:
        if character.jump_count>=-10: #jumping is moving character by ceratin amount of pixels
            neg=1   #negative value is used in order for function to follow the quadratic formula
            if character.jump_count<0:
                neg=-1
            character.y-=(character.jump_count**2)/2*neg #how many pxiels will our character move
            character.jump_count-=1

        else:
            character.is_jump = False
            character.jump_count=10
    redraw_game_window()




pygame.quit()
