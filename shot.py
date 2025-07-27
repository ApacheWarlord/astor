import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)
    
    def update(self, dt):
        
        print(f"Shot update: position={self.position}, velocity={self.velocity}, dt={dt}")
        self.position += self.velocity * dt
        