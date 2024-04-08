import pygame

class Rocket:

    def __init__(self, rm_game):
        self.screen = rm_game.screen
        self.screen_rect = rm_game.screen.get_rect()
        self.image = pygame.image.load('image/rocket.bmp')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.x = self.rect.x
        self.y = self.rect.y
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1
        if self.moving_left and self.rect.left > 0:
            self.x -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1
        if self.moving_up and self.rect.top > 0:
            self.y -= 1
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)