import pygame
pygame.init

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
#whenever using a pygame you need a MAIN LOOP.  
# A main loop is a loop that is constantly running and 
# is handling everything related to the game, i.e: collision, moving the paddle
    while run:
        #the following gets the events like clicking the mouse, keyboard, closing the window.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


    pygame.quit()