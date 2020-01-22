from PIL import Image,ImageDraw
import pygame
from pygame.locals import *
from random import randint

SCREEN_RECT = pygame.Rect(0,0,1000,800)
SCREEN_CLOOR = (200,200,200)
SURFACE_RECT = pygame.Rect(0,0,700,700)
SURFACE_CLOOR = (180,180,180)
SPLIT_NUMBER = 3
RECTLET_SIZE = (SURFACE_RECT.width // SPLIT_NUMBER,
                SURFACE_RECT.height // SPLIT_NUMBER)



class Rectlet(pygame.sprite.Sprite):



    @staticmethod
    def image_no_fame():
        img = Image.new('RGB',RECTLET_SIZE)
        draw = ImageDraw.Draw(img)
        draw.rectangle((1,1,RECTLET_SIZE[0]-2,RECTLET_SIZE[1]-2),(255,248,220))
        img.save("let.png")

        # return img


    # __image = image_no_fame()

    def __init__(self,index,image = None):
        pygame.init()
        super().__init__()
        if image == None:
            self.image = pygame.image.load("let.png")
            my_font = pygame.font.SysFont("SimHei", RECTLET_SIZE[1] * 70 //100)
            text_surface = my_font.render(str(index), True, (0, 0, 0))
            self.image.blit(text_surface, (RECTLET_SIZE[1] * 30 //100,
                                           RECTLET_SIZE[1] * 12 //100))
        self.rect = self.image.get_rect()
        self.imdex = index


class MoBan():

    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__sprite_init()

    def __sprite_init(self):
        self.group = pygame.sprite.Group()

        for i in range(SPLIT_NUMBER ** 2 - 1):
            rectlet = Rectlet(i+1)
            rectlet.rect.x = i % SPLIT_NUMBER * RECTLET_SIZE[0]
            rectlet.rect.y = i // SPLIT_NUMBER * RECTLET_SIZE[1]

            self.group.add(rectlet)

    def __sprite_update(self):
        self.group.update()
        self.group.draw(self.screen)

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

    def start(self):
        self.screen.fill(SCREEN_CLOOR)

        while True:

            # 设置FPS
            self.clock.tick(30)
            # 精灵组更新
            self.__sprite_update()
            # 监控事件
            self.__event_handler()
            # 更新屏幕
            pygame.display.update()


if __name__ == '__main__':
    game = MoBan()
    game.start()
    # Rectlet.image_no_fame()