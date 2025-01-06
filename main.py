import pygame
from constants import *
from circleshape import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    x = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #  x.update(dt)
        for obj in updatable:
            obj.update(dt)
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        # x.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
