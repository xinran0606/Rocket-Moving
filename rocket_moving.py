import sys
import pygame
from rocket import Rocket

class RocketMoving:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Rocket Moving")

        self.rocket = Rocket(self)

    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.rocket.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.rocket.moving_left = True
                elif event.key == pygame.K_UP:
                    self.rocket.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.rocket.moving_down = True
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.rocket.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.rocket.moving_left = False
                if event.key == pygame.K_UP:
                    self.rocket.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.rocket.moving_down = False

    def _update_screen(self):
        self.screen.fill((230,230,230))
        self.rocket.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    rm = RocketMoving()
    rm.run_game()