import pygame
import sys

# Inicializace Pygame
pygame.init()

# Nastavení obrazovky
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()

# Barvy
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Počet hráčů
number_of_players = 2

# Nastavení fontu
font = pygame.font.Font(None, 74)


# Funkce pro vykreslení textu
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 2, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Hlavní smyčka
running = True
while running:
    screen.fill(BLACK)

    # Vykreslení položek menu
    draw_text('Pub Dice', font, WHITE, screen, screen_width*0.4, screen_height*0.2)
    draw_text('Start', font, WHITE, screen, screen_width*0.4, screen_height*0.4)
    draw_text(f'Number of Players: {number_of_players}', font, WHITE, screen, screen_width*0.4, screen_height*0.6)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP or event.key == pygame.K_RIGHT:
                number_of_players = min(number_of_players + 1, 8)
            if event.key == pygame.K_DOWN or event.key == pygame.K_LEFT:
                number_of_players = max(number_of_players - 1, 2)

    pygame.display.update()

pygame.quit()
sys.exit()