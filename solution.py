import pygame
pygame.init()

#the following syntax is how you declare 
# TWO VARIABLES on the same line in python
#this is for our window
WIDTH, HEIGHT = 700, 500
#using all caps on your variable names, 
# in this case, WIN and WIDTH and HEIGHT, makes them a constant

#the following is how you would set up your window in python
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#this will be the caption at the top of the game that says "Pong"
pygame.display.set_caption("Pong")


FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

##################### P A D D L E   C L A S S ########################


class Paddle:
    COLOR = WHITE
    #we are making a class because we are going to have multiple paddles 
    # and we want their properties to be store as an object as to avoid hard coding.

    #initializing a new paddle uses __init__ for this one we will take in x y width and height.  
    # both paddles need to have different movements to move we want them to move based on where the user moves it with the key
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


        #a method on the paddles is the following:


    #draw method is going to literally draw the paddle
    def draw(self, win):
        #how to draw a rectangle in python
        #passing through it where I want to draw it, the window, then the color, 
        # then the rectangle which is an x y width and height.  we draw from the left hand corner in python.
        pygame.draw.rectangle(win, self.COLOR, (self.x, self.y, self,width, self.height))

    def draw(win):
        win.fill(BLACK)
        pygame.display.update()
        #whenever we do a drawing application we need the display 
        # to update and perform any of the drawing operations that we've done.

def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    # whenever using a pygame you need a MAIN LOOP.  
    # A main loop is a loop that is constantly running and 
    # is handling everything related to the game, i.e: collision, moving the paddle
    while run:
        clock.tick(FPS)
        draw(WIN)
            #the following gets the events like clicking the mouse, keyboard, closing the window.
        for event in pygame.event.get():
                #first event we want to check is if we are quitting the window. 
                # it checks on if we hit the close button, so the main loop stops and breaks.
            if event.type == pygame.QUIT:
                run = False
                break


    pygame.quit()

#this ensures we are running this module to call the function
if __name__ == '__main__':
    main()