import pygame
import random
import sys
import os
import time

os.environ['SDL_VIDEO_WINDOW_POS'] = '0, 30'

pygame.init()
FPS = 60
clock = pygame.time.Clock()

Info = pygame.display.Info()
W, H = Info.current_w, Info.current_h

MAX_SHOW = 150
SNOW_SIZE = 64
BG_COLOR = (25, 25, 25)


class Snow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.speed = random.randint(1,3)
        self.img_num = random.randint(1, 2)
        self.snow_SIZE = random.randint(32,64)
        self.image_filename = f'snowflake{self.img_num}.png'
        self.image_orig = pygame.image.load(self.image_filename)
        self.image_orig = pygame.transform.scale(self.image_orig, (self.SNOW_SIZE, self.SNOW_SIZE))
        self.image = self.image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.rot = 0
        self.angle = random.randint(-1, 1)


def check_for_exit():
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            sys.exit(0)



'_________________________________ MAIN __________________________________'


pygame.display.set_icon(pygame.image.load('snow.ico'))
pygame.display.set_caption('SNOW')
screen = pygame.display.set_mode((W, H))

while True:
    check_for_exit()
    pygame.display.update()
    clock.tick(FPS)
