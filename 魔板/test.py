import pygame
from PIL import ImageDraw,Image
RECTLET_SIZE = (50,50)
# # pygame.init()
# img = Image.new('RGBA', RECTLET_SIZE)
# draw = ImageDraw.Draw(img)
# draw.rectangle((1, 1, RECTLET_SIZE[0] - 2, RECTLET_SIZE[1] - 2), (255, 248, 220))
# print(pygame.font.get_fonts())
# img.save("let.png")

pygame.init()
img = pygame.image.load("let.png")
rect = img.get_rect()

my_font = pygame.font.SysFont("SimHei", 183)
text_surface = my_font.render("5", True, (0,0,0))
img.blit(text_surface,(50,0))

screen = pygame.display.set_mode(rect.size)
screen.blit(img,(0,0))
pygame.display.update()
while True:
    pass