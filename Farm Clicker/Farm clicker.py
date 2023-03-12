import pygame
import random
from threading import Timer

pygame.init()

size = (800,560)

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

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 560
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Простой кликер")
bg = pygame.image.load("BG.png")
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
screen.blit(bg, (0, 0))

BUTTON_WIDTH = 300
BUTTON_HEIGHT = 100

UFO_POSITION = 400
UFO_MOVING_LEFT = False

earnings = house5_earnings + house2_earnings + house3_earnings + house4_earnings + house1_earnings
image1 = pygame.image.load("farm 1.png")
image2 = pygame.image.load("farm 2.png")
image3 = pygame.image.load("farm 3.png")
image4 = pygame.image.load("farm 4.png")
image5 = pygame.image.load("farm 5.png")
cow = pygame.image.load("corova.png")
ufo = pygame.image.load("UFO.png")
coin_image = pygame.image.load("Coin Image.png")

image1 = pygame.transform.scale(image1, (BUTTON_WIDTH, BUTTON_HEIGHT))
image2 = pygame.transform.scale(image2, (BUTTON_WIDTH, BUTTON_HEIGHT))
image3 = pygame.transform.scale(image3, (BUTTON_WIDTH, BUTTON_HEIGHT))
image4 = pygame.transform.scale(image4, (BUTTON_WIDTH, BUTTON_HEIGHT))
image5 = pygame.transform.scale(image5, (BUTTON_WIDTH, BUTTON_HEIGHT))
cow = pygame.transform.scale(cow, (BUTTON_WIDTH, 250))
ufo = pygame.transform.scale(ufo, (50, 50))
alpha = 255
coin_image = pygame.transform.scale(coin_image, (50, 50))

button_rect1 = pygame.Rect(10, 10, BUTTON_WIDTH, BUTTON_HEIGHT)
button_rect2 = pygame.Rect(10, 120, BUTTON_WIDTH, BUTTON_HEIGHT)
button_rect3 = pygame.Rect(10, 230, BUTTON_WIDTH, BUTTON_HEIGHT)
button_rect4 = pygame.Rect(10, 340, BUTTON_WIDTH, BUTTON_HEIGHT)
button_rect5 = pygame.Rect(10, 450, BUTTON_WIDTH, BUTTON_HEIGHT)
button_rect6 = pygame.Rect(460, 300, 25, 25)
button_rect7 = pygame.Rect(UFO_POSITION, 100, 25, 25)
font = pygame.font.Font("Minecraft.ttf", 18)
text = font.render(f"  = {money}", True, (255,255,255))

house1_label = font.render(f"Amount: {house1_count}", True, (255,255,255))
house1_cost = font.render(f"Price: {house1_curprice} ", True, (255,255,255))
house1_earn = font.render(f"Earnings: {house1_earnings}", True, (255,255,255))

house2_label = font.render(f"Amount: {house2_count}", True, (255,255,255))
house2_cost = font.render(f"Price: {house2_curprice} ", True, (255,255,255))
house2_earn = font.render(f"Earnings: {house2_earnings}", True, (255,255,255))

house3_label = font.render(f"Amount: {house3_count}", True, (255,255,255))

house3_cost = font.render(f"Price: {house3_curprice}", True, (255,255,255))
house3_earn = font.render(f"Earnings: {house3_earnings}", True, (255,255,255))

house4_label = font.render(f"Amount: {house4_count}", True, (255,255,255))

house4_cost = font.render(f"Price: {house4_curprice}", True,(255,255,255))

house4_earn = font.render(f"Earnings: {house4_earnings}", True, (255,255,255))


house5_label = font.render(f"Amount: {house5_count}", True, (255,255,255))

house5_cost = font.render(f"Price: {house5_curprice}", True,(255,255,255))

house5_earn = font.render(f"Earnings: {house5_earnings}", True, (255,255,255))



#update_all()
def autoclick ():
    global money
    global text
    money += house5_earnings + house2_earnings + house3_earnings + house4_earnings + house1_earnings
    text = font.render(f" = {money}", True, (200, 200, 200))
    #update_all()
    Timer(0.5, autoclick).start()

autoclick()
def UFO_Moving():
        global UFO_POSITION, UFO_MOVING_LEFT, button_rect7
        if UFO_POSITION <= 400:
            UFO_MOVING_LEFT = False
            print("134")
        elif UFO_POSITION >= 560:
            print("431")
            UFO_MOVING_LEFT = True
        if UFO_MOVING_LEFT:
            UFO_POSITION -= 1
        else:
            UFO_POSITION += 1
        button_rect7 = pygame.Rect(UFO_POSITION, 100, BUTTON_WIDTH, 250)
        Timer(0.1, UFO_Moving).start()


UFO_Moving()

def UFO_TRAN2():
    global alpha
    alpha = 255
    ufo.set_alpha(alpha)
def UFO_TRAN():
    global alpha
    alpha = 0
    ufo.set_alpha(alpha)
    Timer(10, UFO_TRAN2).start()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect1.collidepoint(event.pos):
                print("Кнопка 1 нажата!")
                if money >= house1_curprice:
                    money -= house1_curprice
                    house1_count += 1
                    house1_earnings += 1
                    house1_curprice += 10
                    house1_label = font.render(f"Кол-во: {house1_count}", True, (255,255,255))
                    house1_cost = font.render(f"Стоимость: {house1_curprice} ", True, (255, 255, 255))
                    house1_earn = font.render(f"Сумма добычи: {house1_earnings}", True, (255, 255, 255))
                    text = font.render(f" = {money}", True, (255,255,255))
                    #update_all()
            elif button_rect2.collidepoint(event.pos):
                print("Кнопка 2 нажата!")
                if money >= house2_curprice:
                    money -= house2_curprice
                    house2_count += 1
                    house2_earnings += 5
                    house2_curprice += 50
                    house2_label = font.render(f"Кол-во: {house2_count}", True, (255, 255, 255))
                    house2_cost = font.render(f"Стоимость: {house2_curprice} ", True, (255, 255, 255))
                    house2_earn = font.render(f"Сумма добычи: {house2_earnings}", True, (255, 255, 255))
                    text = font.render(f" = {money}", True, (255,255,255))
                    #update_all()
            elif button_rect3.collidepoint(event.pos):
                print("Кнопка 3 нажата!")
                if money >= house3_curprice:
                    money -= house3_curprice
                    house3_count += 1
                    house3_earnings += 15
                    house3_curprice += 250
                    house3_label = font.render(f"Кол-во: {house3_count}", True, (255, 255, 255))
                    house3_cost = font.render(f"Стоимость: {house3_curprice} ", True, (255, 255, 255))
                    house3_earn = font.render(f"Сумма добычи: {house3_earnings}", True, (255, 255, 255))
                    text = font.render(f" = {money}", True, (255,255,255))
                    #update_all()
            elif button_rect4.collidepoint(event.pos):
                print("Кнопка 4 нажата!")
                if money >= house4_curprice:
                    money -= house4_curprice
                    house4_count += 1
                    house4_earnings += 50
                    house4_curprice += 500
                    house4_label = font.render(f"Кол-во: {house4_count}", True, (255, 255, 255))
                    house4_cost = font.render(f"Стоимость: {house4_curprice} ", True, (255, 255, 255))
                    house4_earn = font.render(f"Сумма добычи: {house4_earnings}", True, (255, 255, 255))
                    text = font.render(f" = {money}", True, (255,255,255))
                    #update_all()
            elif button_rect5.collidepoint(event.pos):
                print("Кнопка 5 нажата!")
                if money >= house5_curprice:
                    money -= house5_curprice
                    house5_count += 1
                    house5_earnings += 100
                    house5_curprice += 1000
                    house5_label = font.render(f"Кол-во: {house5_count}", True, (255, 255, 255))
                    house5_cost = font.render(f"Стоимость: {house5_curprice} ", True, (255, 255, 255))
                    house5_earn = font.render(f"Сумма добычи: {house5_earnings}", True, (255, 255, 255))
                    text = font.render(f" = {money}", True, (255,255,255))
                    #update_all()
            elif button_rect6.collidepoint(event.pos):
                print("Корова нажата!")
                money += 3
                #update_all()
            elif button_rect7.collidepoint(event.pos) and alpha == 255:
                print("Нло нажат!")
                UFO_TRAN()
                money += 10
                #update_all()

    screen.blit(bg, (0, 0))
    screen.blit(image1, button_rect1)
    screen.blit(image2, button_rect2)
    screen.blit(image3, button_rect3)
    screen.blit(image4, button_rect4)
    screen.blit(image5, button_rect5)
    screen.blit(cow, button_rect6)
    screen.blit(ufo, button_rect7)
    screen.blit(house1_cost, (button_rect5.x + 110, button_rect1.y + 35))
    screen.blit(house1_label, (button_rect5.x + 110, button_rect1.y + 15))
    screen.blit(house1_earn, (button_rect5.x + 110, button_rect1.y + 55))
    screen.blit(house2_label, (button_rect2.x + 110, button_rect2.y + 15))
    screen.blit(house2_cost, (button_rect2.x + 110, button_rect2.y + 35))
    screen.blit(house2_earn, (button_rect2.x + 110, button_rect2.y + 55))
    screen.blit(house3_label, (button_rect3.x + 110, button_rect3.y + 15))
    screen.blit(house3_cost, (button_rect3.x + 110, button_rect3.y + 35))
    screen.blit(house3_earn, (button_rect3.x + 110, button_rect3.y + 55))
    screen.blit(house4_label, (button_rect4.x + 110, button_rect4.y + 15))
    screen.blit(house4_cost, (button_rect4.x + 110, button_rect4.y + 35))
    screen.blit(house4_earn, (button_rect4.x + 110, button_rect4.y + 55))
    screen.blit(house5_label, (button_rect5.x + 110, button_rect5.y + 15))
    screen.blit(house5_cost, (button_rect5.x + 110, button_rect5.y + 35))
    screen.blit(house5_earn, (button_rect5.x + 110, button_rect5.y + 55))
    screen.blit(coin_image, (SCREEN_WIDTH - 150, 10))
    screen.blit(text, (SCREEN_WIDTH - 150 + 50, 25))

    pygame.display.flip()

    pygame.time.Clock().tick(FPS)

pygame.quit()
