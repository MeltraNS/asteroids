import pygame  # import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):  # a class CircleShape is created inheriting everything from pygame.sprite (all circle shapes are sprites on the screen)
    def __init__(self, x, y, radius):  # a constructor is initialized taking x y coordinates as well as a radius
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)  # set a public variable position initialized as a vector to the coordinated (x,y)
        self.velocity = pygame.Vector2(0, 0)  # set a public variable velocity initialized as a vector.  We will assume that the object is not moving at first, and will move later
        self.radius = radius  # set a public variable radius to radius.  These values will be changed later by the subclasses

    def draw(self, screen):  # define a method draw which takes a screen argument. The subclasses will call this method and override with the functionality they need
        # sub-classes must override
        pass

    def update(self, dt):  # define a method update with takes a dt argument.  Each inheritor will update their methods differently
        # sub-classes must override
        pass

    def HasCollided(self, CircleShape):  # define a function Has Collided which takes a CircleShape argument
        return pygame.math.Vector2.distance_to(self.position, CircleShape.position) <= (self.radius + CircleShape.radius)
        #  if distance between the centers of both circles are greater than the added radius of both circles, return False
