from constants import *
from circleshape import CircleShape
import pygame
import math
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cool = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points, LINE_WIDTH)


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
        if keys[pygame.K_SPACE]:
            self.shoot()

        if self.shot_cool > 0:
            self.shot_cool -= dt
        if self.shot_cool < 0:
            self.shot_cool = 0

    def move(self, dt):
        angle = math.radians(self.rotation)

        move_x = -math.sin(angle)
        move_y = math.cos(angle)

        move_x *= PLAYER_SPEED * dt
        move_y *= PLAYER_SPEED * dt

        self.position.x += move_x
        self.position.y += move_y

    def shoot(self):
        if self.shot_cool > 0:
            return
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        direction = pygame.Vector2(0, 1)
        direction = direction.rotate(self.rotation)
        direction *= PLAYER_SHOOT_SPEED
        shot.velocity = direction
        self.shot_cool = PLAYER_SHOOT_COOLDOWN_SECONDS
