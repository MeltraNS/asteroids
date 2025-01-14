import pygame  # import pygame
import random  # import random module to simulate random behavior
from circleshape import CircleShape  # import the CircleShape method from circleshape to help shape the asteroid

class Asteroid(CircleShape):  # initiate the class Asteroid inheriting everything from the CircleShaple class
    def __init__(self, x, y, radius):  # a constructor is created taking an x, y coordinate and a radius
        super().__init__(x, y, radius)  # each value given in the construcor is fed into the parent's constructor

    def draw(self, screen):  # 
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            
