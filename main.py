import pygame

# Инициализация Pygame
pygame.init()

# Размеры окна
screen_width = 400
screen_height = 400

# Создание окна
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Передвигаемый квадрат")

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)

# Размеры и положение квадрата
square_size = 50
square_x = (screen_width - square_size) // 2
square_y = (screen_height - square_size) // 2

# Главный цикл программы
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получение координат мыши и перемещение квадрата
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:

        # Проверяем, находится ли курсор внутри квадрата
        if square_x <= mouse_x <= square_x + square_size and \
                square_y <= mouse_y <= square_y + square_size:
            square_x = mouse_x - square_size // 2
            square_y = mouse_y - square_size // 2
            # Проверка, не касается ли квадрат края экрана
    if square_x < 0 or square_x + square_size > screen_width or \
                    square_y < 0 or square_y + square_size > screen_height:
                square_x = -square_size
                square_y = -square_size
                time_since_disappearance = pygame.time.get_ticks()

            # Проверка, прошло ли уже 10 секунд с момента исчезновения квадрата
    if square_x == -square_size and square_y == -square_size:
        time_elapsed = pygame.time.get_ticks() - time_since_disappearance
        if time_elapsed >= 100:
                    square_x = screen_width // 2 - square_size // 2
                    square_y = screen_height // 2 - square_size // 2

    # Отрисовка фона и квадрата
    screen.fill(white)
    pygame.draw.rect(screen, black, (square_x, square_y, square_size, square_size))

    # Обновление экрана
    pygame.display.update()

# Завершение работы Pygame
pygame.quit()
