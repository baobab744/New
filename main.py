import pygame
import random
import sys
import os
import time

os.environ['SDL_VIDEO_WINDOW_POS'] = '0, 0'

pygame.init()
FPS = 60
clock = pygame.time.Clock()

Info = pygame.display.Info()
W, H = Info.current_w, Info.current_h

MAX_SNOW = 150
BG_COLOR = (25, 25, 25)


class Snow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.speed = random.randint(1, 3)
        self.img_num = random.randint(1, 2)
        self.snow_size = random.randint(32, 64)
        self.image_filename = f'snowflake{self.img_num}.png'
        self.image_orig = pygame.image.load(self.image_filename)
        self.image_orig = pygame.transform.scale(self.image_orig, (self.snow_size, self.snow_size))
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.rot = 0
        self.angle = random.randint(-1, 1)


    def update(self):
        self.rect.y += self.speed
        if self.rect.top > H:
            self.rect.bottom = 0

        n = random.randint(1, 3)
        if n == 1:
            self.rect.x += 1
            if self.rect.left > W:
                self.rect.right = 0
        elif n == 2:
            self.rect.x -= 1
            if self.rect.right < 0:
                self.rect.left = W
        else:
            self.rect.x += 0

        self.rot = (self.rot + self.angle) % 360
        self.image = pygame.transform.rotate(self.image_orig, self.rot)
        self.rect = self.image.get_rect(center=self.rect.center)


def init_snow(max_snow):
    for _ in range(max_snow):
        snow = Snow(random.randint(0, W), random.randint(0, H))
        all_snow.add(snow)



def check_for_exit():
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            sys.exit(0)



'_________________________________ MAIN __________________________________'


pygame.display.set_icon(pygame.image.load('snow.ico'))
pygame.display.set_caption('SNOW')
screen = pygame.display.set_mode((W, H))

all_snow = pygame.sprite.Group()
init_snow(MAX_SNOW)


while True:
    check_for_exit()
    all_snow.update()
    screen.fill(BG_COLOR)
    all_snow.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
