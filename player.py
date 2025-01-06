import pygame
from circleshape import *
from constants import *

class Player(CircleShape):  # create a class named Player that inherits from CircleShape
    def __init__(self, x, y):  # define a constructor that takes x and y coordinates as inputs
        super().__init__(x, y, PLAYER_RADIUS)  # call theparent class' constructor, run PLAYER_RADIUS as the input, which is 20
        self.rotation = 0  # set the rotation field as 0

    def triangle(self):  # define a function that draws our player
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):  # define a function draw, accepts the screen object as an agruments, also overrides the CircleShape draw method
        pygame.draw.polygon(screen, "white", self.triangle() , 2)  # on the screen, draw a white triangle with a line width of 2

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)           
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
