import math

from pygame.math import Vector2

class Ball:
    """
    base class for bouncing objects
    """
    def __init__(self, bounds, position, velocity, color, radius):
        self.position = position
        self.velocity = velocity
        self.bounds = bounds
        self.color = color
        self.radius = radius

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius: # screen width
            self.velocity.x *= -1
        if self.position.y < 100 + self.radius or self.position.y > self.bounds[1] - self.radius: # screen height
            self.velocity.y *= -1
        self.position += self.velocity

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(self.position.x), int(self.position.y)], self.radius)

class BouncingBall(Ball):
    """
    ball effected by gravity
    """
   

    GRAVITY = .1

    def update(self):  # TODO: Rounding Error
        # print('called update')
        self.velocity.y += self.GRAVITY
        super().update()

class RainbowBall(Ball):
    """
    Ball that changes colors
    """
   # TODO:
    def update(self):
        r = (self.color[0] + 10) % 256
        g = (self.color[1] - 5) % 256
        b = (self.color[2] + 5) % 256
        self.color = [r, g, b]
        super().update()

class BouncingRainbow(RainbowBall, BouncingBall):
    """
    Ball that changes color and is affected by gravity
    """
    # TODO:
    pass

# class KineticBall(BouncingRainbow):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     """
#     # TODO:
#     def update(self):
#         p1 = self.position
#         p2 = self.position
#         v1 = self.velocity
#         v2 = self.velocity
#         b1 = self.bounds
#         b2 = self.bounds

#         if p1.x == p2.x or p1.y == p2.y:
#             v1.x += 5
#             v1.y += 5
#             v2.x += 3
#             v2.y += 3
#             super().update()

# class KineticBouncing(???):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     And is affected by gravity
#     """
    

# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """