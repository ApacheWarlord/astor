import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import * 
from shot import *

def main():
    print("Starting Asteroids!")
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()




    Player.containers =(updatable,drawable)
    Asteroid.containers = (asteroid,updatable,drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shot_group, updatable,drawable)


    asteroid_field = AsteroidField()






    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Astroids Game")
    clock = pygame.time.Clock()
    dt = 0
    running = True
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))

        

        for sprite in updatable:
            sprite.update(dt)

        for asteroid_obj in asteroid:
            if player.collision(asteroid_obj):
                print("Game Over!")
                sys.exit()

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000

        
        

    pygame.quit()

if __name__ == "__main__":
    main()