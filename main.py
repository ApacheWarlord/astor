import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import * 

def main():
    print("Starting Asteroids!")
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    Player.containers =(updatable,drawable)
    asteroid.containers = (asteroid,updatable,drawable)
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
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)
        
        

    pygame.quit()

if __name__ == "__main__":
    main()