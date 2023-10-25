import time

import pygame

pygame.init()
display_info = pygame.display.Info()
print(display_info)
screen_width = display_info.current_w
screen_height = display_info.current_h
window = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
red = pygame.color.Color('#FF0000')
orange = pygame.color.Color('#FF9000')
white = pygame.color.Color('#FFFFFF')
black = pygame.color.Color('#000000')
kostkaIMG = pygame.image.load('foto/dice6.png')
kostka6 = pygame.transform.scale(kostkaIMG, (0.08 * screen_width, 0.08 * screen_width))
kostkaIMG = pygame.image.load('foto/dice6X.png')
kostka6X = pygame.transform.scale(kostkaIMG, (0.08 * screen_width, 0.08 * screen_width))


class dice:
    def __init__(self, x, y, size, number, color):
        self.number = number
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def drawrec(self):
        # pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))
        window.blit(kostka6, (self.x, self.y))
        pygame.display.flip()

    def drawrecP(self):
        window.blit(kostka6X, (self.x, self.y))
        pygame.display.flip()


dice1 = dice(screen_width * 0.5, screen_height * 0.5 - screen_width * 0.1, 0.08 * screen_width, 1, orange)
dice2 = dice(screen_width * 0.4, screen_height * 0.5 - screen_width * 0.1, 0.08 * screen_width, 2, red)
dice3 = dice(screen_width * 0.5, screen_height * 0.5, 0.08 * screen_width, 3, orange)
dice4 = dice(screen_width * 0.4, screen_height * 0.5, 0.08 * screen_width, 4, red)
dice5 = dice(screen_width * 0.5, screen_height * 0.5 + screen_width * 0.1, 0.08 * screen_width, 5, orange)
dice6 = dice(screen_width * 0.4, screen_height * 0.5 + screen_width * 0.1, 0.08 * screen_width, 6, red)
dice1.drawrec()
dice2.drawrecP()
dice3.drawrec()
dice4.drawrecP()
dice5.drawrec()
dice6.drawrecP()
pygame.display.flip()

window.fill(black)
running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
