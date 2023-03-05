import pygame
import random
from threading import Timer

# Инициализация Pygame
pygame.init()



money = 50
house1_count = 0
house1_earnings = 0
house1_curprice = 10

house2_count = 0
house2_earnings = 0
house2_curprice = 50

house3_count = 0
house3_earnings = 0
house3_curprice = 250

house4_count = 0
house4_earnings = 0
house4_curprice = 500

house5_count = 0
house5_earnings = 0
house5_curprice = 1000

# Определение констант
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 560
FPS = 60

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Простой кликер")
bg = pygame.image.load("BG.png")
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
screen.blit(bg, (0, 0))

# Определение параметров кнопки
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 100

earnings = house5_earnings + house2_earnings + house3_earnings + house4_earnings + house1_earnings

# Загрузка изображения
image1 = pygame.image.load("farm 1.png")
image2 = pygame.image.load("farm 2.png")
image3 = pygame.image.load("farm 3.png")
image4 = pygame.image.load("farm 4.png")
image5 = pygame.image.load("farm 5.png")
coin_image = pygame.image.load("Coin Image.png")

# Изменение размера изображения
image1 = pygame.transform.scale(image1, (BUTTON_WIDTH, BUTTON_HEIGHT))
image2 = pygame.transform.scale(image2, (BUTTON_WIDTH, BUTTON_HEIGHT))
image3 = pygame.transform.scale(image3, (BUTTON_WIDTH, BUTTON_HEIGHT))
image4 = pygame.transform.scale(image4, (BUTTON_WIDTH, BUTTON_HEIGHT))
image5 = pygame.transform.scale(image5, (BUTTON_WIDTH, BUTTON_HEIGHT))
coin_image = pygame.transform.scale(coin_image, (50, 50))

# Создание кнопки
button_rect1 = pygame.Rect(10, 10, BUTTON_WIDTH, BUTTON_HEIGHT)
button_rect2 = pygame.Rect(10, 120, BUTTON_WIDTH, BUTTON_HEIGHT)
button_rect3 = pygame.Rect(10, 230, BUTTON_WIDTH, BUTTON_HEIGHT)
button_rect4 = pygame.Rect(10, 340, BUTTON_WIDTH, BUTTON_HEIGHT)
button_rect5 = pygame.Rect(10, 450, BUTTON_WIDTH, BUTTON_HEIGHT)



font = pygame.font.Font(None, 24)
text = font.render(f"  = {money}", True, (30,30,30))

house1_label = font.render(f"Кол-во: {house1_count}", True, (30,30,30))
house1_cost = font.render(f"Стоимость: {house1_curprice} ", True, (30,30,30))
house1_earn = font.render(f"Сумма добычи: {house1_earnings}", True, (30,30,30))

house2_label = font.render(f"Кол-во: {house2_count}", True, (30,30,30))
house2_cost = font.render(f"Стоимость: {house2_curprice} ", True, (30,30,30))
house2_earn = font.render(f"Сумма добычи: {house2_earnings}", True, (30,30,30))

house3_label = font.render(f"Кол-во: {house3_count}", True, (30,30,30))

house3_cost = font.render(f"Стоимость: {house3_curprice}", True, (30,30,30))
house3_earn = font.render(f"Сумма добычи: {house3_earnings}", True, (30,30,30))

house4_label = font.render(f"Кол-во: {house4_count}", True, (30,30,30))

house4_cost = font.render(f"Стоимость: {house4_curprice}", True, (30,30,30))

house4_earn = font.render(f"Сумма добычи: {house4_earnings}", True, (30,30,30))


house5_label = font.render(f"Кол-во: {house5_count}", True, (30,30,30))

house5_cost = font.render(f"Стоимость: {house5_curprice}", True, (30,30,30))

house5_earn = font.render(f"Сумма добычи: {house5_earnings}", True, (30,30,30))

def update_all():
    screen.blit(bg, (0, 0))
    screen.blit(image1, button_rect1)
    screen.blit(image2, button_rect2)
    screen.blit(image3, button_rect3)
    screen.blit(image4, button_rect4)
    screen.blit(image5, button_rect5)
    screen.blit(house1_cost, (button_rect5.x + 110, button_rect1.y + 35))
    screen.blit(house1_label, (button_rect5.x + 110, button_rect1.y+15))
    screen.blit(house1_earn, (button_rect5.x + 110, button_rect1.y + 55))
    screen.blit(house2_label, (button_rect2.x + 110, button_rect2.y+15))
    screen.blit(house2_cost, (button_rect2.x + 110, button_rect2.y + 35))
    screen.blit(house2_earn, (button_rect2.x + 110, button_rect2.y + 55))
    screen.blit(house3_label, (button_rect3.x + 110, button_rect3.y+15))
    screen.blit(house3_cost, (button_rect3.x + 110, button_rect3.y + 35))
    screen.blit(house3_earn, (button_rect3.x + 110, button_rect3.y + 55))
    screen.blit(house4_label, (button_rect4.x + 110, button_rect4.y+15))
    screen.blit(house4_cost, (button_rect4.x + 110, button_rect4.y + 35))
    screen.blit(house4_earn, (button_rect4.x + 110, button_rect4.y + 55))
    screen.blit(house5_label, (button_rect5.x + 110, button_rect5.y+15))
    screen.blit(house5_cost, (button_rect5.x + 110, button_rect5.y + 35))
    screen.blit(house5_earn, (button_rect5.x + 110, button_rect5.y + 55))
    screen.blit(coin_image, (SCREEN_WIDTH-150, 10))
    screen.blit(text, (SCREEN_WIDTH-150 + 50, 25))


update_all()

def autoclick ():
    global money
    global text
    money += house5_earnings + house2_earnings + house3_earnings + house4_earnings + house1_earnings
    text = font.render(f" = {money}", True, (30, 30, 30))
    update_all()
    Timer(0.5, autoclick).start()

autoclick()

# Бесконечный цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Обработка события нажатия кнопки
            if button_rect1.collidepoint(event.pos):
                print("Кнопка 1 нажата!")
                if money >= house1_curprice:
                    money -= house1_curprice
                    house1_count += 1
                    house1_earnings += 1
                    house1_curprice += 10
                    screen.fill((30, 30, 30))
                    house1_label = font.render(f"Кол-во: {house1_count}", True, (30,30,30))
                    house1_cost = font.render(f"Стоимость: {house1_curprice} ", True, (30, 30, 30))
                    house1_earn = font.render(f"Сумма добычи: {house1_earnings}", True, (30, 30, 30))
                    text = font.render(f" = {money}", True, (30,30,30))
                    update_all()
            elif button_rect2.collidepoint(event.pos):
                print("Кнопка 2 нажата!")
                if money >= house2_curprice:
                    money -= house2_curprice
                    house2_count += 1
                    house2_earnings += 5
                    house2_curprice += 50
                    screen.fill((30, 30, 30))
                    house2_label = font.render(f"Кол-во: {house2_count}", True, (30, 30, 30))
                    house2_cost = font.render(f"Стоимость: {house2_curprice} ", True, (30, 30, 30))
                    house2_earn = font.render(f"Сумма добычи: {house2_earnings}", True, (30, 30, 30))
                    text = font.render(f" = {money}", True, (30,30,30))
                    update_all()
            elif button_rect3.collidepoint(event.pos):
                print("Кнопка 3 нажата!")
                if money >= house3_curprice:
                    money -= house3_curprice
                    house3_count += 1
                    house3_earnings += 15
                    house3_curprice += 250
                    screen.fill((30, 30, 30))
                    house3_label = font.render(f"Кол-во: {house3_count}", True, (30, 30, 30))
                    house3_cost = font.render(f"Стоимость: {house3_curprice} ", True, (30, 30, 30))
                    house3_earn = font.render(f"Сумма добычи: {house3_earnings}", True, (30, 30, 30))
                    text = font.render(f" = {money}", True, (30,30,30))
                    update_all()
            elif button_rect4.collidepoint(event.pos):
                print("Кнопка 4 нажата!")
                if money >= house4_curprice:
                    money -= house4_curprice
                    house4_count += 1
                    house4_earnings += 50
                    house4_curprice += 500
                    screen.fill((30, 30, 30))
                    house4_label = font.render(f"Кол-во: {house4_count}", True, (30, 30, 30))
                    house4_cost = font.render(f"Стоимость: {house4_curprice} ", True, (30, 30, 30))
                    house4_earn = font.render(f"Сумма добычи: {house4_earnings}", True, (30, 30, 30))
                    text = font.render(f" = {money}", True, (30,30,30))
                    update_all()
            elif button_rect5.collidepoint(event.pos):
                print("Кнопка 5 нажата!")
                if money >= house5_curprice:
                    money -= house5_curprice
                    house5_count += 1
                    house5_earnings += 100
                    house5_curprice += 1000
                    screen.fill((30, 30, 30))
                    house5_label = font.render(f"Кол-во: {house5_count}", True, (30, 30, 30))
                    house5_cost = font.render(f"Стоимость: {house5_curprice} ", True, (30, 30, 30))
                    house5_earn = font.render(f"Сумма добычи: {house5_earnings}", True, (30, 30, 30))
                    text = font.render(f" = {money}", True, (30,30,30))
                    update_all()

    # Отрисовка экрана
    pygame.display.update()

    # Ограничение частоты обновления экрана
    pygame.time.Clock().tick(FPS)

# Завершение Pygame
pygame.quit()
