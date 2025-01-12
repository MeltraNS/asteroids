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
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    x = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    y = AsteroidField()
    
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)
                
        for asteroid in asteroids:
            if asteroid.HasCollided(x) == True:
                sys.exit("Game over!")
                
        for asteroid in asteroids:
            for shot in shots:  # Nested loop to check all shot-asteroid combinations
                if asteroid.HasCollided(shot):  # Ensure collision check happens properly
                    shot.kill()
                    asteroid.split()
            
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
