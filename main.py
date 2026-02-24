from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
import pygame
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
import sys
from shot import *

def main():
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event('player_hit')
                print("Game Over!")
                sys.exit()
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
