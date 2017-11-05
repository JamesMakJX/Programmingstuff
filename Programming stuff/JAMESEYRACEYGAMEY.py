import pygame
import time
import random


pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
rimbrown = (139,69,19)
innerbrown = (160,82,45)


car_width = 145

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Jamesey Racey")
clock = pygame.time.Clock()
roadpict = pygame.image.load('jamesey_road.png')
carmodel = pygame.image.load('jamesey_car.png')


def things(thingx, thingy, thingw, thingh):
    pygame.draw.rect(gameDisplay, rimbrown, [thingx, thingy, thingw, thingh])
    pygame.draw.rect(gameDisplay, innerbrown, [thingx + 5, thingy + 5, thingw - 10, thingh - 10])
    pygame.draw.rect(gameDisplay, rimbrown, [thingx + thingw/2 -2.5, thingy, 5, thingh])
    pygame.draw.rect(gameDisplay, rimbrown, [thingx, thingy + thingh/2 -2.5, thingw, 5])


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text, (0,0))

def road(rx, ry):
    gameDisplay.blit(roadpict, (rx, ry))

def car(x, y):
    gameDisplay.blit(carmodel, (x, y))

def text_objects(text, font):
    textsurf = font.render(text, True, black)
    return textsurf, textsurf.get_rect()

def message(text, ypos):
    t = pygame.font.Font('freesansbold.ttf', 70)
    tsurf, trect = text_objects(text, t)
    trect.center = ((display_width/2), ypos)
    gameDisplay.blit(tsurf, trect)

    pygame.display.update()
    time.sleep(2)

    game_loop()

def crash():
    message('You Crashed!', (display_height/2))
    
    
def speed(carspeed):
    t2 = pygame.font.Font('freesansbold.ttf', 50)
    t2surf, t2rect = text_objects(carspeed, t2)
    t2rect.center = ((display_width/2), (display_height * 0.1))
    gameDisplay.blit(t2surf, t2rect)

    pygame.display.update()


def game_loop():

    x = (display_width * 0.4)
    y = (display_height * 0.6)

    rx = 0
    ry = 0
    ry2 = -600
    x_change = 0
    y_change = 0
    thing_startx = random.randrange(0, display_width)
    thing_starty = -100
    thing_speed = 10
    thing_width = random.randrange(50, 100)
    thing_height = random.randrange(50, 100)
    thing2_startx = random.randrange(0, display_width)
    thing2_starty = -400
    thing2_speed = 10
    thing2_width = random.randrange(50, 100)
    thing2_height = random.randrange(50, 100)
    carspeedno = 50
    global dodged
    dodged = 0
    
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -20
                elif event.key == pygame.K_RIGHT:
                    x_change = 20

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -20
                elif event.key == pygame.K_DOWN:
                    y_change = 20

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        x += x_change                  
        y += y_change   
        gameDisplay.fill(white)

        road(rx, ry)
        road(rx, ry2)
        car(x, y)
        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height)
        things(thing2_startx, thing2_starty, thing2_width, thing2_height)
        thing2_starty += thing2_speed
        thing_starty += thing_speed
        ry += thing_speed
        ry2 += thing_speed
        
        
        things_dodged(dodged)
        carspeed = "{0:.1f}km/hr".format(carspeedno)
        speed(carspeed)
        carspeedno += 0.05
        if x > display_width - car_width + 100 or x < -120:
            crash()

        if y < 0 or y > display_height:
            crash()

        if ry > display_height:
            ry = -600

        if ry2 > display_height:
            ry2 = -600
            
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width-thing_width)
            thing_width = random.randrange(50, 100)
            thing_height = random.randrange(50, 100)
            thing_speed += 0.5
            dodged += 1

        if thing2_starty > display_height:
            thing2_starty = 0 - thing2_height
            thing2_startx = random.randrange(0, display_width-thing2_width)
            thing2_width = random.randrange(50, 100)
            thing2_height = random.randrange(50, 100)
            thing2_speed += 0.5
            dodged += 1
            

        if (y + 10 < thing_starty + thing_height and y + 222 > thing_starty) and (x + 30 < thing_startx + thing_width and x + 135 > thing_startx):
            crash()

        if (y + 10 < thing2_starty + thing2_height and y + 222 > thing2_starty) and (x + 30 < thing2_startx + thing2_width and x + 135 > thing2_startx):
            crash()
            
        pygame.display.update()
        clock.tick(300)



game_loop()
pygame.quit()
quit()
