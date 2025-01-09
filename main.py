import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
