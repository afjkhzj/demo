import random
import pygame
from pygame.locals import *
import numpy as np


SCREEN_RECT = pygame.Rect(0, 0, 900, 700)
SURFACE_RECT = pygame.Rect(0, 0, 700, 700)
SPLIT_NUMBER = 5


class ImageSprite(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        # self.rect.x = x
        # self.rect.y = y
        self.rect.width += 2
        self.rect.height += 2

    def update(self, *key):
        if key == K_UP:
            if self.rect.y > 0:
                self.rect.y -= self.rect.height
        if key == K_DOWN:
            if self.rect.bottom < SURFACE_RECT.height:
                self.rect.y += self.rect.height
        if key == K_LEFT:
            if self.rect.x > 0:
                self.rect.x -= self.rect.width
        if key == K_RIGHT:
            if self.rect.right < SURFACE_RECT.right:
                self.rect.y += self.rect.height


class MoFang:

    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.surface = pygame.Surface(SURFACE_RECT.size)
        self.clock = pygame.time.Clock()
        self.array = np.arange(SPLIT_NUMBER ** 2).reshape((5,5))

        # np.random.shuffle(self.array)
        # self.array.reshape((5,5))
        print(self.array)

        self.sprite_init()

    @staticmethod
    def image_slice():
        img = pygame.image.load('image.jpeg')
        imgs = []
        for i in range(5):
            for j in range(5):
                imgs.append(img.subsurface((i * 140 + 1, j * 140 + 1, 138, 138)))
        return imgs

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                ImageSprite.update(event.key)

    def sprite_init(self):
        imagelet_width = SURFACE_RECT.width // SPLIT_NUMBER
        imagelet_height = SURFACE_RECT.height // SPLIT_NUMBER

        img = pygame.image.load('image.jpeg')
        self.group = pygame.sprite.Group()
        for i in range(SPLIT_NUMBER):
            for j in range(SPLIT_NUMBER):
                imglet = img.subsurface((i * imagelet_width + 1, j * imagelet_height + 1,
                                         imagelet_width - 2, imagelet_height - 2))
                # if i== 4 and j == 4:
                #     break
                imglet_sprite = ImageSprite(imglet)
                imglet_sprite.rect.x = self.array[i][j] // SPLIT_NUMBER * imagelet_width
                imglet_sprite.rect.y = self.array[i][j] % SPLIT_NUMBER * imagelet_height
                self.group.add(imglet_sprite)

    def sprite_update(self):

        self.screen.fill((200, 200, 200))
        self.surface.fill((200, 200, 200))

        self.group.update()
        self.group.draw(self.surface)
        self.screen.blit(self.surface, (0, 0))

    def start(self):
        while True:
            # 设置刷新率
            self.clock.tick(30)
            # 事件监控
            self.event_handler()
            # 精灵组更新
            self.sprite_update()
            #
            pygame.display.update()


if __name__ == '__main__':
    game = MoFang()
    game.start()
