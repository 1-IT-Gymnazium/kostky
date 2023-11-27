import pygame
import random

pygame.init()
sound1 = pygame.mixer.Sound('music/rolling_dice.mp3')
sound2 = pygame.mixer.Sound('music/rolling_dice2.mp3')
sound3 = pygame.mixer.Sound('music/rolling_dice3.mp3')
sounds = [sound1, sound2, sound3]
display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h
window = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
black = pygame.color.Color('#000000')
white = pygame.color.Color('#FFFFFF')
blue = pygame.color.Color('#6c8cbf')
font = pygame.font.Font(None, 36)


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
        self.dices = [Dice(x, y, 6) for x, y in self.POSITIONS]
        for dice in self.dices:
            dice.draw(6)
        self.buttons = [Button("Throw"),Button("Next player",y = screen_height * 0.5 + screen_width * 0.05)]
        for button in self.buttons:
            button.draw()

    def get_position(self):
        return pygame.mouse.get_pos()

    def get_dice(self, x, y):
        for dice in self.dices:
            if (x >= dice.x and x <= dice.x_end) and (y >= dice.y and y <= dice.y_end):
                return dice


class Dice:
    SIZE = 0.08
    dice_imgs = {
        "locked_imgs": {
            1: pygame.transform.scale(pygame.image.load('foto/dice1X.png'), (SIZE * screen_width, SIZE * screen_width)),
            2: pygame.transform.scale(pygame.image.load('foto/dice2X.png'), (SIZE * screen_width, SIZE * screen_width)),
            3: pygame.transform.scale(pygame.image.load('foto/dice3X.png'), (SIZE * screen_width, SIZE * screen_width)),
            4: pygame.transform.scale(pygame.image.load('foto/dice4X.png'), (SIZE * screen_width, SIZE * screen_width)),
            5: pygame.transform.scale(pygame.image.load('foto/dice5X.png'), (SIZE * screen_width, SIZE * screen_width)),
            6: pygame.transform.scale(pygame.image.load('foto/dice6X.png'), (SIZE * screen_width, SIZE * screen_width))
        },
        "unlocked_imgs": {
            1: pygame.transform.scale(pygame.image.load('foto/dice1.png'), (SIZE * screen_width, SIZE * screen_width)),
            2: pygame.transform.scale(pygame.image.load('foto/dice2.png'), (SIZE * screen_width, SIZE * screen_width)),
            3: pygame.transform.scale(pygame.image.load('foto/dice3.png'), (SIZE * screen_width, SIZE * screen_width)),
            4: pygame.transform.scale(pygame.image.load('foto/dice4.png'), (SIZE * screen_width, SIZE * screen_width)),
            5: pygame.transform.scale(pygame.image.load('foto/dice5.png'), (SIZE * screen_width, SIZE * screen_width)),
            6: pygame.transform.scale(pygame.image.load('foto/dice6.png'), (SIZE * screen_width, SIZE * screen_width))
        }
    }

    def __init__(self, x, y, value, locked=False, counted=False):
        self.x = x
        self.y = y
        self.locked = locked
        self.value = value
        self.x_end = x + (self.SIZE * screen_width)
        self.y_end = y + (self.SIZE * screen_width)
        self.counted = counted

    def draw(self, number):
        if self.locked != True:
            window.blit(self.dice_imgs["unlocked_imgs"][number], (self.x, self.y))
        else:
            window.blit(self.dice_imgs["locked_imgs"][number], (self.x, self.y))
        pygame.display.flip()

    def rolldice(self):
        if self.locked != True:
            self.animation()

    def animation(self):
        random_number = random.randint(1, 6)
        self.value = random_number
        self.draw(random_number)


class Button:
    def __init__(self, text, color=black, width=150, height=75, x=screen_width * 0.5 + screen_width * 0.25,
                 y=screen_height * 0.5 - screen_width * 0.05):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text
        self.color = color

    def draw(self):
        pygame.draw.rect(window, blue, (self.x, self.y, self.width, self.height))
        text = font.render(self.text, True, self.color)
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        window.blit(text, text_rect)


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
                random_sound = random.choice(sounds)
                random_sound.play()
                for l in range(6):
                    for i in range(6):
                        board.dices[i].rolldice()
                        if board.dices[i].locked:
                            board.dices[i].counted = True
                    pygame.time.delay(200)

                print(board.dices[0].value)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            dice = board.get_dice(*board.get_position())
            if dice and not dice.counted:
                dice.locked = not dice.locked
                for dice in board.dices:
                    dice.draw(dice.value)
                    pygame.display.flip()
            # i = 0
            # while i < 100:
            #     # Your code here
            #     Dice.rolldice()
            #     i += 1
