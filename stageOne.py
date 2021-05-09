# TODO create trigger event
# TODO optimise code
# TODO create json level data
# TODO finish character movement and import and implement into this module


import sys
import pygame
from GLOBAL_VARIABLES import WIN, WHITE
import os
import json
from text_engine import text_box

# imports and sets variable for stage
# TODO change this to take json variables based on level data
# TODO set up movement limit data

# opens json file
f = open(os.path.join('level data', 'level_one.json'))
data = json.load(f)
VEL = 5

character = pygame.Rect(data["main_character"]["starting_positionx"], data["main_character"]["starting_positiony"],
                        data["main_character"]["rect_dim_x"], data["main_character"]["rect_dim_y"])
background = pygame.Rect(0, 0, data["background"]["level_x_dim"], data["background"]["level_y_dim"])

MAIN_CHARACTER = pygame.transform.rotate(
    pygame.transform.scale(
        pygame.image.load(os.path.join(data["main_character"]["file_location"], data["main_character"]["file_name"])),
        (192, 108)), 0)
STAGE = pygame.transform.rotate(
    pygame.transform.scale(
        pygame.image.load(os.path.join(data["background"]["base_level_location"], data["background"]["file_name"])),
        (2920, 2080)), 0)


# draws screen
def draw_window_stage1(backgroundimage):
    WIN.fill(WHITE)
    WIN.blit(STAGE, (backgroundimage.x, backgroundimage.y))
    draw_characters(character)
    pygame.display.update()


def draw_characters(characterimage):
    WIN.blit(MAIN_CHARACTER, (characterimage.x, characterimage.y))




class stage_one:
    def __init__(self):
        self.state = 'stage'
        self.background = background
        self.character = character
        textbox = text_box(self.background)

    def load_stage(self):
        self.quit_check()

        keys_pressed = pygame.key.get_pressed()
        self.background_handle_movement(keys_pressed, character, background)
        draw_window_stage1(background)

    def background_handle_movement(self, keys_pressed, yellow, background):
        if keys_pressed[pygame.K_a]:  # LEFT
            yellow.x -= VEL
            # temporary limits
            # TODO create limits to read from json file
            # set limits to be based off of the position of the background
            if yellow.x <= background.x + 300:
                background.x -= VEL / 2
                yellow.x = background.x + 300

        if keys_pressed[pygame.K_d]:  # Right
            yellow.x += VEL
            # temporary limits
            # TODO create limits to read from json file
            if yellow.x >= background.x + 1620:
                background.x += VEL / 2
                # yellow.x = background.x + 1620

        if keys_pressed[pygame.K_w]:  # UP
            yellow.y -= VEL
            # temporary limits
            # TODO create limits to read from json file
            if yellow.y <= background.y + 300:
                background.y -= VEL / 2
                # yellow.y = background.y + 300

        if keys_pressed[pygame.K_s]:  # UP
            yellow.y += VEL
            # temporary limits
            # TODO create limits to read from json file
            if yellow.y >= background.y + 780:
                background.y += VEL / 2
                # yellow.y = background.y + 780

    def player_movement(self):
        # draw character and its rect
        pass

    @staticmethod
    def quit_check():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()

    def state_manager(self):
        if self.state == 'stage':
            self.load_stage()
