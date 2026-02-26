from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from circleshape import CircleShape
import random
from logger import log_state, log_event

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, 'white', (self.position.x, self.position.y), self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, asteroids):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        for _ in range(2):
            new_asteroid = Asteroid(
                self.position.x,
                self.position.y,
                new_radius
            )

            angle = random.uniform(20, 50)
            direction = pygame.Vector2(1, 0).rotate(angle)
            new_asteroid.velocity = direction * self.velocity.length()*1.2

            asteroids.add(new_asteroid)
        log_event("asteroid_split")
        self.kill()
