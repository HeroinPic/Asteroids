from circleshape import *
from constants import *
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        self.kill()
        blue_angle = random.uniform(20, 50)
        nv1 = self.velocity.rotate(blue_angle)
        nv2 = self.velocity.rotate(-blue_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        ast1.velocity = nv1 * 1.2
        ast2.velocity = nv2 * 1.2
        for group in self.groups():
            group.add(ast1)
            group.add(ast2)