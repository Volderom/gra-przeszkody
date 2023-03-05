import pygame
import random

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moja gra")

# Kolory
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Gracz
player_width = 50
player_height = 50
player_x = 375
player_y = 500
player_speed = 5

# Przeszkody
obstacle_width = 50
obstacle_height = 50
obstacle_x = random.randint(0, width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 5

# Punktacja
score = 0
font = pygame.font.Font(None, 36)

# Pętla gry
game_over = False
clock = pygame.time.Clock()

while not game_over:
    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Ruch gracza
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed

    # Ruch przeszkód
    obstacle_y += obstacle_speed
    if obstacle_y > height:
        obstacle_x = random.randint(0, width - obstacle_width)
        obstacle_y = -obstacle_height
        score += 1

    # Sprawdzenie kolizji
    if obstacle_y + obstacle_height > player_y and obstacle_y < player_y + player_height:
        if obstacle_x + obstacle_width > player_x and obstacle_x < player_x + player_width:
            game_over = True

    # Rysowanie
    screen.fill(white)
    pygame.draw.rect(screen, red, [obstacle_x, obstacle_y, obstacle_width, obstacle_height])
    pygame.draw.rect(screen, black, [player_x, player_y, player_width, player_height])
    text = font.render("Punkty: {}".format(score), True, black)
    screen.blit(text, [10, 10])

    pygame.display.update()

    # Ograniczenie liczby klatek na sekundę
    clock.tick(60)

# Zakończenie Pygame
pygame.quit()
