import pygame
import random

pygame.init()

display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h
window = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
black = pygame.color.Color('#000000')


class Board:
    POSITIONS = [
        (screen_width * 0.5, screen_height * 0.5 - screen_width * 0.1),
        (screen_width * 0.4, screen_height * 0.5 - screen_width * 0.1),
        (screen_width * 0.5, screen_height * 0.5),
        (screen_width * 0.4, screen_height * 0.5),
        (screen_width * 0.5, screen_height * 0.5 + screen_width * 0.1),
        (screen_width * 0.4, screen_height * 0.5 + screen_width * 0.1)

    ]

    def create(self):
        self.dices = [Dice(x, y) for x, y in self.POSITIONS]
        for dice in self.dices:
            dice.draw(6)


class Dice:
    dice_imgs = {
        "locked_imgs": {
            1: pygame.transform.scale(pygame.image.load('foto/dice1X.png'), (0.08 * screen_width, 0.08 * screen_width)),
            2: pygame.transform.scale(pygame.image.load('foto/dice2X.png'), (0.08 * screen_width, 0.08 * screen_width)),
            3: pygame.transform.scale(pygame.image.load('foto/dice3X.png'), (0.08 * screen_width, 0.08 * screen_width)),
            4: pygame.transform.scale(pygame.image.load('foto/dice4X.png'), (0.08 * screen_width, 0.08 * screen_width)),
            5: pygame.transform.scale(pygame.image.load('foto/dice5X.png'), (0.08 * screen_width, 0.08 * screen_width)),
            6: pygame.transform.scale(pygame.image.load('foto/dice6X.png'), (0.08 * screen_width, 0.08 * screen_width))
        },
        "unlocked_imgs": {
            1: pygame.transform.scale(pygame.image.load('foto/dice1.png'), (0.08 * screen_width, 0.08 * screen_width)),
            2: pygame.transform.scale(pygame.image.load('foto/dice2.png'), (0.08 * screen_width, 0.08 * screen_width)),
            3: pygame.transform.scale(pygame.image.load('foto/dice3.png'), (0.08 * screen_width, 0.08 * screen_width)),
            4: pygame.transform.scale(pygame.image.load('foto/dice4.png'), (0.08 * screen_width, 0.08 * screen_width)),
            5: pygame.transform.scale(pygame.image.load('foto/dice5.png'), (0.08 * screen_width, 0.08 * screen_width)),
            6: pygame.transform.scale(pygame.image.load('foto/dice6.png'), (0.08 * screen_width, 0.08 * screen_width))
        }
    }

    def __init__(self, x, y, locked=False):
        self.x = x
        self.y = y
        self.locked = locked

    def draw(self, number):
        if self.locked != True:
            window.blit(self.dice_imgs["unlocked_imgs"][number], (self.x, self.y))
        else:
            window.blit(self.dice_imgs["locked_imgs"][number], (self.x, self.y))
        pygame.display.flip()

    def rolldice(self):
        if self.locked != True:
            self.animation()
            #
    def animation(self):
        for i in range(4):
            for l in range(6):
                random_number = random.randint(1, 6)
                self.draw(random_number)
            pygame.time.delay(2000)

board = Board()
board.create()
pygame.display.flip()

window.fill(black)
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for i in range(6):
                    board.dices[i].rolldice()
                # i = 0
                # while i < 100:
                #     # Your code here
                #     Dice.rolldice()
                #     i += 1
