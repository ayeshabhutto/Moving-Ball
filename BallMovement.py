import pygame
import random
import math

init()
size = width, height = 800, 800 
screen = display.set_mode(size)

#Setting up colour
BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)



FONT = font.SysFont("Times New Roman",30) # done once	
FONT2 = font.SysFont("comicsansms",100) # done once	


# setting up constants to help with the parts of the list
BALLX = 0
BALLY = 1
BALLSPEEDX = 2
BALLSPEEDY = 3
COLOUR = 4

radiusOFball = 10

# function to set up a ball with random attributes
def initBall():
    ballx = random.randint(0, 800) # randomly setting the x position
    bally = random.randint(0, 800) # randomly setting the y position
    dirx = random.randint(-5,5) # randomly setting the x speed
    diry = random.randint(-5,5) # randomly setting the y speed
    COLOUR = random.choice([BLUE, GREEN, RED, WHITE])
    info = [ballx, bally, dirx, diry, COLOUR] # returning a list with all the info the ball needs
    return info # returning the list



def drawScreen(ClicksonBall):
    draw.rect(screen, BLACK, (0, 0, 800, 800))
    text = FONT.render(str(ClicksonBall), 1, (255,255, 255))	
    screen.blit(text, Rect(750,10,200,100))
    
    
def moveBall(info): # takes in the list of the ball
    info[BALLX] += info[BALLSPEEDX] # increases the position of the ball
    info[BALLY] += info[BALLSPEEDY]

# checks to see if the ball is hitting the walls in the x direction
    if info[BALLX] > 800:
        info[BALLX] = 800
        info[BALLSPEEDX] *= -1
    elif info[BALLX] < 0:
        info[BALLX] = 0
        info[BALLSPEEDX] *= -1
    
    # checks to see if the ball is hitting the walls in the y direction
    if info[BALLY] < 0:
        info[BALLY] = 0
        info[BALLSPEEDY] *= -1 
    elif info[BALLY] > 800:
        info[BALLY] = 800
        info[BALLSPEEDY] *= -1
    
    return info # returning the updated list





def ballIsClicked(info, mx, my):
    print(mx >= info[BALLX])
    if mx >= info[BALLX] - radiusOFball and mx <= info[BALLX] + radiusOFball:
        if my >= info[BALLY] - radiusOFball and my <= info[BALLY] + radiusOFball:
            return True
    
    return False 

def BallCollision(info1, info2):

    distance = ((info2[BALLX] - info1[BALLX])**2 + (info2[BALLY] - info1[BALLY])**2)
    if distance < 0: #so we can still get the distance if the number is negative
        distance *= -1
    distance = sqrt(distance)

    if distance <= radiusOFball:
        return True
        
    return False




def drawBall(info): # sends a ball to be displayed

    draw.circle(screen, info[COLOUR], (info[BALLX], info[BALLY]), radiusOFball)
    
    
    
    
running = True # variable that controls the main loop
myClock = time.Clock() # for controlling the frames per second

balls = []
ClicksonBall = 0
win = False
redLeft = False

for i in range(0,10): 
    balls.append(initBall()) # initializing the ball
# Game Loop
while running == True: # do this loop as long as running is True
    redLeft = False
# events all ready
    for evnt in event.get(): # checks all events that happen
        if evnt.type == QUIT:
            running = False
    if evnt.type == MOUSEBUTTONDOWN:
        print('click')
        mx, my = evnt.pos 
        button = evnt.button 
        for ball1 in balls:
            if ballIsClicked(ball1, mx, my) and ball1[COLOUR] == RED:
                balls[balls.index(ball1)] = initBall()
                ClicksonBall += 1
                break


#draw the black background
    drawScreen(ClicksonBall)
    # moving each ball and drawing it
    for i in range(0,len(balls)):
    # calling the draw ball function and sending the ball information
        drawBall(balls[i])
        balls[i] = moveBall(balls[i])
    
        for ball2 in balls:
            if ball2 is not balls[i] and BallCollision(balls[i], ball2):
                c1 = balls[i][COLOUR]
                c2 = ball2[COLOUR]
        
                if c1 == GREEN or c2 == GREEN:
                    balls[i][COLOUR] = GREEN
                    ball2[COLOUR] = GREEN
        
                elif (c1 == WHITE and c2 == BLUE) or (c1 == BLUE and c2 == WHITE):
                    balls[i][COLOUR] = WHITE
                    ball2[COLOUR] = WHITE 
        
                elif (c1 == RED and c2 is not GREEN) or (c2 == RED and c1 is not GREEN):
                    balls[i][COLOUR] = RED
                    ball2[COLOUR] = RED 
        
        if balls[i][COLOUR] == RED:
            redLeft = True
    
    display.flip()

    myClock.tick(60) # waits long enough to have 60 frames per second

    if not redLeft:
        running = False

        if ClicksonBall >= 5:
            win = True
            running = False



if win:
    drawScreen('')
    text = FONT2.render('You Win!', 1, (75,255, 241))	
    screen.blit(text, Rect(200,200,25,25)) 
    display.flip()
    time.wait(3000)
else:
    drawScreen('')
    text = FONT2.render('You lost.', 1, (75,255, 241))	
    screen.blit(text, Rect(200,200,25,25)) 
    display.flip()
    time.wait(3000) 




quit()
