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

#time for the event loop!

def main():
    run = True
    clock = pygame.time.Clock()
    #we need a clock is gonna regulate the framerate of our game so it runs at the same pace on every computer
    FPS = 60

    WHITE = (255,255,255)
    BLACK = (0,0,0)

    def draw(win):
        win.fill(WHITE)
        pygame.display.update()
        #whenever we do a drawing application we need the display 
        # to update and perform any of the drawing operations that we've done.


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