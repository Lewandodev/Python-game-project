import pygame

pygame.init() #initialising pygame

window=pygame.display.set_mode((600,480)) #displaying the window

pygame.display.set_caption("Python Game Project") #displaying games title

#uploading all the sprites/images to python
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
background = pygame.image.load('bgr.jpg')
char = pygame.image.load('Standing.png')
score_of_player=0

clock=pygame.time.Clock()

#uploading music and sound effect
bullet_soundef=pygame.mixer.Sound('bullet_sound.wav')
hit_soundef=pygame.mixer.Sound('hiteffect.wav')
music_backgorund=pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1) #playing music in background

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
        self.hitbox=(self.x + 17, self.y, 28, 60) #defining rectangular hitbox 28 is width 60 is height x and and y are the coordinates which move whole rectangle up/down/left/right



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

        # we need to add hitbox to draw method since player can move
        self.hitbox = (self.x + 17, self.y, 28, 60)
        #every time player is moving the hitbox moves with him and changes
        #pygame.draw.rect(window,(255,0,0),self.hitbox,2)

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

class enemy(object):

    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                 pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                 pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),
                 pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),
                pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]  #This will define where our enemy starts and finishes their walking cycle/path.
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y+2, 31, 57)
        self.health=11 #to keep track of our enemy health
        self.visible=True #once our enemy has no more health left we will make him disappear

    #we will first move then draw enemy

    #enemy will move only on x axis from one point to another
    #essentially we will increase/substract x value
    def draw(self,window):
        self.move()
        if self.visible is True:

            #standard loop reseting to change images
            #if self.walkCount + 1 >= 33: #33 since we have 11 sprites
            #    self.walkCount=0

            # we can use the modulo in order to avoid resetting walkCount value every round of frames
            if self.vel>0: #we move right
                window.blit(self.walkRight[(self.walkCount//3)%11],(self.x,self.y))

            else: #we move left
                window.blit(self.walkLeft[(self.walkCount // 3)%11], (self.x, self.y))
            self.walkCount += 1

            pygame.draw.rect(window,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,50,10) ) #drawing our health bar -> damaged red colour hitbox[0,1] are coordinates
            pygame.draw.rect(window, (0, 150, 0), (self.hitbox[0], self.hitbox[1] - 20, 50-((50//11)*(11-self.health)), 10)) #full healthbar green colour which we will move via substraction
            #50 is width we substract our width by width // divided by the previously defined health multiplied by overall health we start with substracted by current amount of health
            self.hitbox = (self.x + 17, self.y+2, 31, 57)

            #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)




    def move(self):
        if self.vel>0:
            if self.x+self.vel<self.path[1]: #if our x coordinate is less than the coordinate we cant go pass we  will allow enemy to move
                self.x+=self.vel
            else: #changing direction enemy moves
                self.vel=self.vel*-1 #changing to opposite direction
                self.walkCount=0
        else:
            if self.x-self.vel>self.path[0]:
                self.x+=self.vel
            else:
                self.vel = self.vel * -1  # opposite direction
                self.walkCount = 0

    #this methods exectue whenever goblin gets hit
    def hit(self):
        print('target hit')
        if self.health>1: #once health is 0 enemy will die
            self.health-=1 #substracting health while enemy is hit
        else:
            self.visible=False
        pass



def redraw_game_window():

    window.blit(background,(0,0))
    text=scoreboard_font.render('Score:'+str(score_of_player),1,(0,0,0)) #rendering our scoreboard onto the screen
    window.blit(text,(390,10))
    character.draw(window)
    zombie.draw(window)
    for bullet in bullets:
        bullet.draw(window)
    pygame.display.update()

character=player(300,340,64,64)
zombie=enemy(100,340,64,64,500) #instance of our enemy
cooldown=0 #shooting cooldown
bullets=[]

#creating our scoreboard
scoreboard_font=pygame.font.SysFont('TTF',40,True)



run=True
while run is True:
    clock.tick(54) #changed delay according to our FPS

    #making a cooldown of the projectiles player is shooting
    if cooldown>0:
        cooldown+=1
    if cooldown>3:
        cooldown=0
    #we only allow palyer to shoot if the shooting cooldown is max it prevents player from spamming and making the the projectiles looks like a cluster

    for event in pygame.event.get(): #event is anything that happens "from the user" like using movement keys or clicking
        if event.type==pygame.QUIT:  #thanks to this function we wont get error after exiting game
            run=False
    #projectiles:
    for bullet in bullets:
        #if the bullet is inside the hitbox we match it as hit
        #specifically we will check the y coordinates of projectile and see if its between the y coordinates of our hitbox
        if bullet.y-bullet.radius<zombie.hitbox[1]+zombie.hitbox[3] and bullet.y+bullet.radius>zombie.hitbox[1]: #first part check if we are above the bottom of hitbox and second if we are below the top
            #then we need to check right side and left side
            if bullet.x + bullet.radius > zombie.hitbox[0] and bullet.x-bullet.radius<zombie.hitbox[0]+zombie.hitbox[2]: #hitbox[0] is x coordinate
                hit_soundef.play()
                zombie.hit()
                score_of_player+=1
                bullets.pop(bullets.index(bullet)) #remove projectile once it hit


        if bullet.x<500 and bullet.x>0:#checking if proejctile is on the screen
            bullet.x+=bullet.velocity#projectile will move in any direction (left/right) we want
        else:#projectile is not on the screen
            bullets.pop(bullets.index(bullet))

    #movement
    #coordinates of object are stored in top left of the character
    move_keys=pygame.key.get_pressed()

    #projectiles
    if move_keys[pygame.K_SPACE] and cooldown==0:
        bullet_soundef.play()
        if character.left:
            facing=-1 #moving negative direction in order to make the projectiole move left
        else:
            facing=1 #otherwise projectile will move right
        if len(bullets)<5:
            bullets.append(projectile(round(character.x + character.width // 2), round(character.y + character.height // 2), 6, (255, 0, 0), facing))
            #projectile will come from the "center" of player character
        cooldown=1

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
