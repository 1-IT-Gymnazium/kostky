import pygame
import random

from load import rules

pygame.init()
sound1 = pygame.mixer.Sound('music/rolling_dice.mp3')
sound2 = pygame.mixer.Sound('music/rolling_dice2.mp3')
sound3 = pygame.mixer.Sound('music/rolling_dice3.mp3')
victory_sound = pygame.mixer.Sound('music/victory_sound.mp3')
sounds = [sound1, sound2, sound3]
display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h
window = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
black = pygame.color.Color('#000000')
white = pygame.color.Color('#FFFFFF')
blue = pygame.color.Color('#6c8cbf')
grey = pygame.color.Color('#928383')
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 74)
fontdsd = pygame.font.Font('font/SEASRN__.ttf', 36)
number_of_players = 2
menu = True


class Board:
    POSITIONS = [
        (screen_width * 0.5, screen_height * 0.5 - screen_width * 0.1),
        (screen_width * 0.4, screen_height * 0.5 - screen_width * 0.1),
        (screen_width * 0.5, screen_height * 0.5),
        (screen_width * 0.4, screen_height * 0.5),
        (screen_width * 0.5, screen_height * 0.5 + screen_width * 0.1),
        (screen_width * 0.4, screen_height * 0.5 + screen_width * 0.1)

    ]
    DIFFPOSS = [
        (screen_width * 0.01, screen_height * 0.13,"Player 1 - 0"),
        (screen_width * 0.01, screen_height * 0.20,"Player 2 - 0"),
        (screen_width * 0.01, screen_height * 0.27,"Player 3 - 0"),
        (screen_width * 0.01, screen_height * 0.34,"Player 4 - 0"),
        (screen_width * 0.01, screen_height * 0.41,"Player 5 - 0"),
        (screen_width * 0.01, screen_height * 0.48,"Player 6 - 0"),
        (screen_width * 0.01, screen_height * 0.55,"Player 7 - 0"),
        (screen_width * 0.01, screen_height * 0.62,"Player 8 - 0"),
        (screen_width * 0.01, screen_height * 0.69, "Player 9 - 0"),
        (screen_width * 0.01, screen_height * 0.76, "Player 10 - 0")

    ]
    def create(self):
        '''
            Creates all the objects
            :example: create()
        '''
        self.dices = [Dice(x, y, 6) for x, y in self.POSITIONS]
        for dice in self.dices:
            dice.draw()
        self.buttons = [ThrowButton("Throw"),
                        NextPlayerButton("Next player", y=screen_height * 0.5 + screen_width * 0.015),
                        KeepDiceButton("Keep dice", x=screen_width * 0.6 + screen_width * 0.175, y=screen_height * 0.5 - screen_width * 0.05, visible=False, back_color=black),
                        ResetDiceButton("Reset dice", x=screen_width * 0.6 + screen_width * 0.175, y=screen_height * 0.5 + screen_width * 0.015,
                                        visible=False, back_color=black),
                        PlayAgainButton("Play Again", x=screen_width * 0.4 + screen_width * 0.25, y=screen_height * 0.5 + screen_width * 0.015*5.3,
                                        visible=False, back_color=black)
                        ]
        for button in self.buttons:
            button.draw()
        self.player = 0
        self.temp_score_holder = 0
        self.players = [Player("Player 1"),Player("Player 2")]
        self.score_rec = ScoreDisplay("Temp score - 0")
        self.score_rec.draw()
        self.victory_screen = VictoryScreen()
        self.player_rec = PlayerDisplay(f"{self.players[self.player].name} is now playing")
        self.player_rec.draw()
        self.player_name_score = [ScoreAndPlayers(x, y, text) for x, y, text in self.DIFFPOSS]
        board.draw_names()
        self.drawable_objects = [*self.dices, *self.buttons, self.score_rec, self.player_rec]
        self.throw_unselected_dices()

    def draw(self):
        '''
        Draws all the objects in the drawable_objects list
        :example: draw()
        '''
        for object in self.drawable_objects:
            object.draw()
    def create_menu(self):
        '''
        Creates the menu
        :example: create_menu
        '''
        self.menu = Menu()
    def draw_names(self):
        '''
        Draws all the players
        :example: draw_names
        '''
        for x in range(0, number_of_players):
            board.player_name_score[x].draw()
    def create_players(self):
        '''
        Creates the rest of the players(the first two are hardcoded in)
        :example: create_players
        '''
        for x in range(2, number_of_players):
            self.players.append(Player(f"Player {x+1}"))
        #for x in range(0,number_of_players):
            #print(self.players[x])
    def get_position(self):
        '''
        Gets the position of the mouse
        :return: int,int
        :example: get_position() return 150,150
        '''
        return pygame.mouse.get_pos()

    def get_dice(self, x, y):
        '''
        Gets coordinates of the click of the mouse and checks if the
        click is on a dice. If it is it returns what dice it is on.
        :param x(int),y(int):
        :return: int
        :example: get_dice(200,200) return 2
        '''
        for dice in self.dices:
            if (x >= dice.x and x <= dice.x_end) and (y >= dice.y and y <= dice.y_end):
                return dice

    def get_button(self, x, y):
        '''
        Gets coordinates of the click of the mouse and checks if the
        click is on a button. If it is it returns what button it is on.
        :param x(int),y(int):
        :return: int
        :example: get_button(200,200) return 1
        '''
        for button in self.buttons:
            if (x >= button.x and x <= button.x_end) and (y >= button.y and y <= button.y_end):
                return button

    def check_all_dices_locked(self):
        '''
        checks if all the dices are locked, if they are it returns True
        :return: Bool
        :example: gcheck_all_dices_locked() return True
        '''
        for dice in self.dices:
            if not dice.selected:
                return False
        return True

    def unlock_all_dices(self):
        '''
        unlocks and uncounts all the dices
        :example: unlock_all_dices()
        '''
        for dice in self.dices:
            dice.selected = False
            dice.counted = False
            dice.locked = False

    def lock_dices(self):
        '''
        locks all the dices
        :example: lock_dices()
        '''
        for dice in self.dices:
            dice.locked = True

    def unlock_dices(self):
        '''
        unlocks all the dices
        :example: unlock_dices()
        '''
        for dice in self.dices:
            dice.locked = False

    def throw_unselected_dices(self):
        '''
        Throws all the unlocked(unselected) dices
        :example: throw_unselected_dices()
        '''
        ThrowButton.sound(self)
        for l in range(6):
            for i in range(6):
                self.dices[i].rolldice()
                if self.dices[i].selected:
                    self.dices[i].counted = True
            pygame.time.delay(200)

    def show_next_player_buttons(self):
        '''
        Shows the keep dices and reset dices buttons
        :example: show_next_player_buttons()
        '''
        self.buttons[2].show()
        self.buttons[3].show()
        self.buttons[2].back_color = blue
        self.buttons[3].back_color = blue

    def show_play_again_button(self):
        self.buttons[4].show()
        self.buttons[4].back_color = blue
    def hide_next_player_buttons(self):
        '''
        Hides the keep dices and reset dices buttons
        :example: hide_next_player_buttons()
        '''
        self.buttons[2].hide()
        self.buttons[3].hide()
        self.buttons[2].back_color = black
        self.buttons[3].back_color = black

    def next_player(self):
        '''
        Switches players, if the player is the last one on the list, it starts from the start of the list
        :example: next_player()
        '''
        if len(self.players) - 1 == self.player:
            self.player_name_score[
                self.player].text = str(f"{self.players[self.player].name} - {self.players[self.player].score}")
            self.player = 0
            self.player_rec.text = str(f"{self.players[self.player].name} is now playing")
        else:
            self.player_name_score[
                self.player].text = str(f"{self.players[self.player].name} - {self.players[self.player].score}")
            self.player += 1
            self.player_rec.text = str(f"{self.players[self.player].name} is now playing")
        self.draw_names()
    pygame.display.update()


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

    def __init__(self, x, y, value, selected=False, counted=False, locked=False):
        self.x = x
        self.y = y
        self.selected = selected
        self.value = value
        self.x_end = x + (self.SIZE * screen_width)
        self.y_end = y + (self.SIZE * screen_width)
        self.counted = counted
        self.locked = locked

    def draw(self):
        '''
        If the dice you clicked on is not selected, it changes the img to be the
        selected one and vice versa
        :example: draw()
        '''
        if self.selected != True:
            window.blit(self.dice_imgs["unlocked_imgs"][self.value], (self.x, self.y))
        else:
            window.blit(self.dice_imgs["locked_imgs"][self.value], (self.x, self.y))
        pygame.display.flip()

    def rolldice(self):
        '''
        checks if the dice is locked or not, if not it calls animation to roll the dice.
        :example: rolldice()
        '''
        if self.selected != True:
            self.animation()

    def animation(self):
        '''
        gives the dice a random number and draws them.
        :example: animation()
        '''
        random_number = random.randint(1, 6)
        self.value = random_number
        self.draw()

class Button:
    def __init__(self, text, color=black, back_color=blue, width=150, height=75,
                 x=screen_width * 0.4 + screen_width * 0.25,
                 y=screen_height * 0.5 - screen_width * 0.05,
                 visible=True, unlocked=True):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.x_end = x + width
        self.y_end = y + height
        self.text = text
        self.color = color
        self.back_color = back_color
        self.visible = visible
        self.unlocked = unlocked

    def draw(self):
        '''
        draws all the visible buttons
        :example: draw()
        '''
        pygame.draw.rect(window, self.back_color, (self.x, self.y, self.width, self.height), border_radius=15)
        text = font.render(self.text, True, self.color)
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        window.blit(text, text_rect)

    def hide(self):
        '''
        hides the next player buttons
        :example: hide()
        '''
        self.visible = False

    def show(self):
        '''
        shows the next player buttons
        :example: show()
        '''
        self.visible = True


class ThrowButton(Button):

    def action(self):
        '''
        If the selected dices are allowed by the rules it throws all te unselected dices
        :example: action()
        '''
        if rules(dice_values):
            self.write_dice_to_score()
            self.sound()
            board.throw_unselected_dices()

    def sound(self):
        '''
        plays a random sound
        :example: hide()
        '''
        random_sound = random.choice(sounds)
        random_sound.play()

    def write_dice_to_score(self):
        '''
        Takes the score from the value of the dices and adds it to the temporary score.
        :example: write_dice_to_score()
        '''
        board.players[board.player].temp_score = rules(dice_values)
        board.score_rec.text = f"Temp score - {str(board.players[board.player].temp_score)}"
        board.score_rec.draw()
        dice_values.clear()


class NextPlayerButton(Button):

    def action(self):
        '''
        Checks if the button is unlocked, if yes it checks the combination of the dices with the rules. If it returns
        a value it adds the value to the temporary score and adds the temporary score to the players score,
        switches to the next player and displays the next player buttons.If the player has achieved 10000 points it
        will end the game. If the rules don't return a value it resets.
        :example: action()
        '''
        if self.unlocked:
            if rules(dice_values):
                    self.unlocked = False
                    board.players[board.player].temp_score = rules(dice_values)
                    board.temp_score_holder = board.players[board.player].temp_score
                    board.players[board.player].set_score()
                    board.score_rec.text = f"Temp score - {str(board.temp_score_holder)}"
                    board.score_rec.draw()
                    if board.players[board.player].score >= 10000:
                        board.victory_screen.draw(f"Winner is - {str(board.players[board.player])}")
                        board.show_play_again_button()
                        victory_sound.play()
                    else:
                        board.show_next_player_buttons()
                    board.next_player()
                    dice_values.clear()
                    board.lock_dices()
            else:
                dice_values.clear()
                board.players[board.player].reset_temp_score()
                board.temp_score_holder = 0
                board.next_player()
                board.score_rec.text = f"Temp score - {str(board.players[board.player].temp_score)}"
                board.unlock_all_dices()
                board.throw_unselected_dices()
                self.unlocked = True


class KeepDiceButton(Button):
    def action(self):
        '''
        If the button is visible, switches to the next player and doesn't reset the dices. Keep the temporary score.
        :example: action()
        '''
        if self.visible:
            board.players[board.player].temp_score = board.temp_score_holder
            board.hide_next_player_buttons()
            board.throw_unselected_dices()
            board.unlock_dices()
            board.buttons[1].unlocked = True

class ResetDiceButton(Button):
    def action(self):
        '''
        If the button is visible, switches to the next player and resets the dices. Resets the temporary score.
        :example: action()
        '''
        if self.visible:
            board.hide_next_player_buttons()
            board.score_rec.text = f"Temp score - {str(board.players[board.player].temp_score)}"
            board.unlock_all_dices()
            board.throw_unselected_dices()
            # NextPlayerButton.unlocked = True
            board.buttons[1].unlocked = True

class PlayAgainButton(Button):
    def action(self):
        '''
        If the button is visible, switches to the next player and doesn't reset the dices. Keep the temporary score.
        :example: action()
        '''
        if self.visible:
            global menu
            menu = True


class Player:
    def __init__(self, name):
        self.__score = 0
        self.__temp_score = 0
        self.name = name
    def __repr__(self):
        '''
        Returns players name
        :example: action()
        '''
        return f"{self.name}"

    @property
    def temp_score(self):
        '''
        Returns the temporary score
        :return: int
        :example: temp_score(), return 150
        '''
        return self.__temp_score

    @temp_score.setter
    def temp_score(self, value):
        '''
        Adds the temporary score to the player score
        :param: value(int)
        :example: temp_score(), return 150
        '''
        self.__temp_score += value

    @property
    def score(self):
        '''
        Returns the player score
        :return: int
        :example: score(), return 1500
        '''
        return self.__score

    def set_score(self):
        '''
        Adds the temporary score to the players score and resets the temporary score
        :example: set_score()
        '''
        self.__score += self.__temp_score
        self.__temp_score = 0

    def reset_temp_score(self):
        '''
        Resets the temporary score
        :example: reset_temp_score()
        '''
        self.__temp_score = 0


class ScoreDisplay:
    def __init__(self, text, color=blue, text_color=black, width=screen_width / 4.2, height=screen_height / 9.6,
                 x=screen_width * 0.01,
                 y=screen_height * 0.01):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.x_end = x + width
        self.y_end = y + height
        self.text = text
        self.color = color
        self.text_color = text_color

    def draw(self):
        '''
        Draws the score display rectangle
        :example: draw()
        '''
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), border_radius=15)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        window.blit(text, text_rect)


class PlayerDisplay:
    def __init__(self, text, color=blue, text_color=black, width=screen_width / 3, height=screen_width / 10,
                 x=screen_width * 0.5 - (screen_width / 3)/2,
                 y=screen_height * 0.01):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.x_end = x + width
        self.y_end = y + height
        self.text = text
        self.color = color
        self.text_color = text_color

    def draw(self):
        '''
        Draws the player display rectangle
        :example: draw()
        '''
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), border_radius=15)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        window.blit(text, text_rect)




class ScoreAndPlayers:
    def __init__(self, x, y, text, width=screen_width / 4.2, height=screen_height / 9.6, color = black):
        self.x = x
        self.y = y
        self.text = text
        self.width = width
        self.height = height
        self.text_color = color

    def draw(self):
        '''
        Draws the current players score rectangle
        :example: draw()
        '''
        pygame.draw.rect(window, blue, (self.x, self.y, self.width, self.height), border_radius=15)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        window.blit(text, text_rect)
class Menu:
    def __init__(self, color=blue, text_color=black, width=screen_width / 4.2, height=screen_height / 9.6,
                 x=screen_width * 0.33,
                 y=screen_height * 0.38):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.x_end = x + width
        self.y_end = y + height
        self.color = color
        self.text_color = text_color
        self.menu_run = True

    def draw_text(self, text, font, color, x, y):
        '''
        Draws the menu screen
        :param: text(string)
        font(font),color(color),x(int),y(int)
        :example: draw_text('Pub Dice', font2, white, screen_width * 0.4, screen_height * 0.2)
        '''
        pygame.draw.rect(window, blue, (self.x, self.y, self.width, self.height), border_radius=15)
        textobj = font.render(text, 2, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        window.blit(textobj, textrect)

    def get_start(self, x, y):
        '''
        Gets coordinates of the click of the mouse and checks if the
        click is on a button. If it is it returns what button it is on.
        :param: x(int),y(int)
        :return: Bool
        :example: get_start(200,200) return True
        '''
        if (x >= self.x and x <= self.x + self.width) and (y >= self.y and y <= self.y + self.height):
            return True
class VictoryScreen:
    def __init__(self, color=blue, text_color=black, width=screen_width / 3, height=screen_width / 12,
                 x=screen_width * 0.5 - (screen_width / 3) / 2,
                 y=screen_height * 0.85):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.x_end = x + width
        self.y_end = y + height
        self.color = color
        self.text_color = text_color

    def draw(self,  text):
        '''
        Draws the player display rectangle
        :example: draw()
        '''
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), border_radius=15)
        text = font.render(text, True, self.text_color)
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        window.blit(text, text_rect)

board = Board()
board.create_menu()
pygame.display.flip()
dice_values = []
FirstDiceCounter = 0
end = False
createnumber = 0

running = True
while running:
    if menu:
        createnumber = 0
        window.fill(black)
        board.menu.draw_text('Pub Dice', font2, white, screen_width * 0.4, screen_height * 0.2)
        board.menu.draw_text(f'Number of Players: {number_of_players}', font2, white, screen_width * 0.4,
                       screen_height * 0.6)
        board.menu.draw_text('Start', font2, white, screen_width * 0.4, screen_height * 0.4)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_UP or event.key == pygame.K_RIGHT:
                    number_of_players = min(number_of_players + 1, 10)
                if event.key == pygame.K_DOWN or event.key == pygame.K_LEFT:
                    number_of_players = max(number_of_players - 1, 2)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if board.menu.get_start(*board.get_position()):
                    menu = False
                    break
            pygame.display.update()
    else:
        for event in pygame.event.get():
            if createnumber == 0:
                window.fill(black)
                board.create()
                board.create_players()
                createnumber += 1
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                dice = board.get_dice(*board.get_position())
                button = board.get_button(*board.get_position())
                if dice and not dice.counted and not dice.locked:
                    dice.selected = not dice.selected
                    # print(dice.value)
                    if dice.selected == True:
                        dice_values.append(dice.value)
                    else:
                        dice_values.remove(dice.value)
                    for dice in board.dices:
                        pass
                        # dice.draw()S
                elif button:
                    if board.check_all_dices_locked():
                        if rules(dice_values):
                            board.unlock_all_dices()
                    button.action()
            board.draw()
            pygame.display.flip()
        # i = 0
        # while i < 100:
        #     # Your code here
        #     Dice.rolldice()
        #     i += 1
