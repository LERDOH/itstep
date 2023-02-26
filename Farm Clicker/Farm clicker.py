import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

Money = 10
house1_count = 0
house1_earnings = 0
house1_price = 10

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Простой кликер")
screen.fill((70, 70, 70))

# параметры кнопки
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 100
BUTTON_TEXT = " "
coins_text = f" = {Money}"
BUTTON_COLOR = (0, 255, 0)
BUTTON_TEXT_COLOR = (0, 0, 0)
BUTTON_TEXT_SIZE = 24

image1 = pygame.image.load("farm 1.png")
image2 = pygame.image.load("farm 2.png")
image3 = pygame.image.load("farm 3.png")
image4 = pygame.image.load("farm 4.png")
image5 = pygame.image.load("farm 5.png")

coin_image = pygame.image.load("Coin Image.png")

image1 = pygame.transform.scale(image1, (BUTTON_WIDTH, BUTTON_HEIGHT))
image2 = pygame.transform.scale(image2, (BUTTON_WIDTH, BUTTON_HEIGHT))
image3 = pygame.transform.scale(image3, (BUTTON_WIDTH, BUTTON_HEIGHT))
image4 = pygame.transform.scale(image4, (BUTTON_WIDTH, BUTTON_HEIGHT))
image5 = pygame.transform.scale(image5, (BUTTON_WIDTH, BUTTON_HEIGHT))
coin_image = pygame.transform.scale(coin_image, (50, 50))

# Создание кнопки
button_rect1 = pygame.Rect(10, 10, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image1, button_rect1)
button_rect2 = pygame.Rect(10, 120, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image2, button_rect2)
button_rect3 = pygame.Rect(10, 230, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image3, button_rect3)
button_rect4 = pygame.Rect(10, 340, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image4, button_rect4)
button_rect5 = pygame.Rect(10, 450, BUTTON_WIDTH, BUTTON_HEIGHT)
screen.blit(image5, button_rect5)

screen.blit(coin_image, (SCREEN_WIDTH//2, 10))

# Создание текстовой надписи на кнопке
font = pygame.font.Font(None, 24)
text = font.render(coins_text, True, (255,255,255))
screen.blit(text, (SCREEN_WIDTH//2+50, 25))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame .MOUSEBUTTONDOWN and event.button == 1:
            if button_rect1.collidepoint(event.pos):
                print("Кнопка1 нажата!")
            if button_rect2.collidepoint(event.pos):
                print("Кнопка2 нажата!")
            if button_rect3.collidepoint(event.pos):
                print("Кнопка3 нажата!")
            if button_rect4.collidepoint(event.pos):
                print("Кнопка4 нажата!")
            if button_rect5.collidepoint(event.pos):
                print("Кнопка5 нажата!")

    pygame.display.update()

    pygame.time.Clock().tick(FPS)

pygame.quit()
