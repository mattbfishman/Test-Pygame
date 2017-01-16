from pygame import *
import sys, pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,image, x, y, height, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


