import sys  # import sys to activate sys.ext upon game over
import pygame  # import pygame to run the game, draw polygons, etc.
from constants import *  # import everything from the constants.py to establish non changing values
from player import Player  # import the Player class from player.py to establish player attributes
from asteroid import Asteroid  # import the Asteroid class from asteroid.py to make asteroids
from asteroidfield import AsteroidField  # import the AsteroidField class from asteroidfield.py to define where and when asteroids spawn
from shot import Shot # import the Shot class from shot.py to handle what happens when we shoot

def main():  # a main function is defined to run as soon as the program is run in Python
    pygame.init()  # initiate a pygame instance
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # initialize variable screen to a 1280/720
    clock = pygame.time.Clock()  # initiate a clock instance to keep track of time
    
    updatable = pygame.sprite.Group()  # create a group to house all of our updatables
    drawable = pygame.sprite.Group()  # create a group to house all of our drawables
    asteroids = pygame.sprite.Group()  # create a group to house all of our asteroids
    shots = pygame.sprite.Group()  # create a group to house all of our shots
    
    Asteroid.containers = (asteroids, updatable, drawable)  # create an asteroids containers which houses all asteroids is updatable and drawable
    Player.containers = (updatable, drawable)  # create a player container that is updatable and drawable
    AsteroidField.containers = updatable  # create an asteroid field container which is updatable
    Shot.containers = (shots, updatable, drawable)  # create a shot container whose objects are shots, updatable, and drawable

    x = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # create a variable where the player will spawn
    y = AsteroidField()  # create the asteroid field
    
    dt = 0  # set the change in time to zero
    
    while True:  # create the infinite loop for the game engine
        for event in pygame.event.get():  # check events every refresh
            if event.type == pygame.QUIT:  # if the x button is closed on the pygame game window:
                return  # close the program and return to the command line

        for obj in updatable:  # update each object in the object container every time the screen refreshes
            obj.update(dt)
                
        for asteroid in asteroids:  # if the player collided with an asteroid, end  the game
            if asteroid.HasCollided(x) == True:
                sys.exit("Game over!")
                
        for asteroid in asteroids:
            for shot in shots:  # Nested loop to check all shot-asteroid combinations
                if asteroid.HasCollided(shot):  # Ensure collision check happens properly
                    shot.kill()
                    asteroid.split()
            
        screen.fill("black")  # flash the screen, ergo fill the screen with black every update call
        
        for obj in drawable:  # once the screen fills with black, update the positions of every drawable object to simulate movement
            obj.draw(screen)
            
        pygame.display.flip()  # refresh the screen
        dt = clock.tick(60) / 1000  # update the refresh rate
        
if __name__ == "__main__":  #  call the main function if this program is run in the command line
    main()
