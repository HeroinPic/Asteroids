import pygame
import sys
from player import *
from constants import *
from asteroids import *
from asteroidfield import *
from shoot import *


def main ():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable, )
    Shot.containers = (updatable, drawable, shots)

    player1 = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color = (0,0,0))
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = fps.tick(60) / 1000
        for object in updatable:
            object.update(dt)
        for asteroid in asteroids:
            if asteroid.collide(player1):
               print ("GAME OVER!")
               sys.exit()
            for shot in shots:
                if asteroid.collide(shot):
                    shot.kill()
                    asteroid.split()

 
if __name__ == "__main__":
    main()
