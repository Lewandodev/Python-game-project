import pygame

pygame.init() #initialising pygame

window=pygame.display.set_mode((600,480)) #displaying the window

pygame.display.set_caption("Python Game Project") #displaying games title

#uploading all the sprites/images to python
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
background = pygame.image.load('bgr.jpg')
char = pygame.image.load('Standing.png')

clock=pygame.time.Clock()

screen_border=600

#getting rid of globals by using classes
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
        self.right=True #which direction will our character face upon spawning if both are set to false we will see bug
        self.walking_count=0
        self.standing=True

    def draw(self,window):
        # creating character
        if self.walking_count + 1 >= 27:  # 9 sprites which I will display for 3 frames therefore 9*3. That's how many times we will go through the loop before it changes the image
            self.walking_count = 0  # In 27 FPS changing image every 3 loops makes the character look like its moving

        if not(self.standing):
            if self.left:
                window.blit(walkLeft[self.walking_count // 3], (self.x, self.y)) #self.x/y->position we use integer divison for frames
                self.walking_count += 1
            elif self.right:
                window.blit(walkRight[self.walking_count // 3], (self.x, self.y))
                self.walking_count += 1
        else:
            #window.blit(char, (self.x, self.y))
            #checking last frame/whether player is standing turned left or right, player character doesn't move
            if self.right:
                window.blit(walkRight[0],(self.x,self.y))
            else:
                window.blit(walkLeft[0],(self.x,self.y))

#projectile which our character will shoot
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.velocity=6*facing

    def draw(self,window):
        pygame.draw.circle(window,self.color,(self.x,self.y),self.radius)



def redraw_game_window():

    window.blit(background,(0,0))
    character.draw(window)
    for bullet in bullets:
        bullet.draw(window)
    pygame.display.update()

character=player(300,340,64,64)

bullets=[]

run=True
while run is True:
    clock.tick(54) #changed delay according to our FPS

    for event in pygame.event.get(): #event is anything that happens "from the user" like using movement keys or clicking
        if event.type==pygame.QUIT:  #thanks to this function we wont get error after exiting game
            run=False
    #projectiles:
    for bullet in bullets:
        if bullet.x<500 and bullet.x>0:#checking if proejctile is on the screen
            bullet.x+=bullet.velocity#projectile will move in any direction (left/right) we want
        else:#projectile is not on the screen
            bullets.pop(bullets.index(bullet))

    #movement
    #coordinates of object are stored in top left of the character
    move_keys=pygame.key.get_pressed()

    #projectiles
    if move_keys[pygame.K_SPACE]:
        if character.left:
            facing=-1 #moving negative direction in order to make the projectiole move left
        else:
            facing=1 #otherwise projectile will move right
        if len(bullets)<5:
            bullets.append(projectile(round(character.x + character.width // 2), round(character.y + character.height // 2), 6, (255, 0, 0), facing))
            #projectile will come from the "center" of player character

    if move_keys[pygame.K_LEFT] and character.x>character.velocity:
        character.x-=character.velocity
        character.left=True
        character.right=False
        #changing the stand
        character.standing=False
    elif move_keys[pygame.K_RIGHT] and character.x<screen_border-character.width-character.velocity: #substracting by width moves our border making the character crossing attempts impossible
        character.x+=character.velocity
        character.left = False
        character.right = True
        character.standing=False
    else:
        #we need to get rid of reseting rigt/left values because we wont know which way our character is looking
        #character.right=False
        #character.left=False
        character.standing=True
        character.walking_count=0

    if not(character.is_jump):
        '''if move_keys[pygame.K_UP] and y > velocity:
            y-=velocity                         #going up and down will be useless in a paltformer game
        elif move_keys[pygame.K_DOWN] and y < screen_border-height-velocity:
            y+=velocity'''
        if move_keys[pygame.K_UP]:
            character.is_jump = True
            #we don't set character booleans to true or false to avoid bugs

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
