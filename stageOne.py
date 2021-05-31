# TODO create trigger event
# TODO optimise code
# TODO create json level data
# TODO finish character movement and import and implement into this module


import sys
import pygame
from GLOBAL_VARIABLES import WIN, WHITE, VEL
import os
import json
from text_engine import text_box
from NPC_handler import NPC

# imports and sets variable for stage
# TODO change this to take json variables based on level data
# TODO set up movement limit data

# opens json file
f = open(os.path.join('level data', 'level_one.json'))
data = json.load(f)

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
        (1920, 1080)), 0)


# draws screen
def draw_window_stage1(backgroundimage,characterimage):
    WIN.fill(WHITE)
    WIN.blit(STAGE, (backgroundimage.x, backgroundimage.y))
    WIN.blit(MAIN_CHARACTER, (characterimage.x, characterimage.y))




class stage_one:
    def __init__(self):
        self.state = 'stage'
        self.background = background
        self.character = character
        self.textbox = text_box(STAGE, "pog")
        self.npcOne = NPC(data,False)

    def load_stage(self):
        self.quit_check()

        keys_pressed = pygame.key.get_pressed()
        self.handle_movment(keys_pressed)
        draw_window_stage1(background,character)
        self.textbox.draw_textbox()
        self.npcOne.draw_npc()
        # self.npcone.npc_handel_movements(((1, 2), (3, 4)))
        pygame.display.update()

    def handle_movment(self,keys_pressed):
        if not data["background"]["movable"]:
            self.handle_movment_background_static(keys_pressed)

        if data["background"]["movable"]:
            self.background_handle_movement(keys_pressed)

    def handle_movment_background_static(self,keys_pressed):
        if keys_pressed[pygame.K_a]:  # LEFT
            self.character.x -= VEL
            if self.character.x <= 300:
                self.character.x += VEL

        if keys_pressed[pygame.K_d]:  # Right
            self.character.x += VEL
            if self.character.x >= 1620:
                self.character.x -= VEL

        if keys_pressed[pygame.K_w]:  # UP
            self.character.y -= VEL
            if self.character.y <= 300:
                self.character.y += VEL

        if keys_pressed[pygame.K_s]:  # DOWN
            self.character.y += VEL
            if self.character.y >= 780:
                self.character.y -= VEL

    def background_handle_movement(self,keys_pressed):
        # TODO create limits to read from json file
        # TODO rework limits
        if keys_pressed[pygame.K_a]:  # LEFT
            if self.character.x <= 300:
                self.character.x -= VEL / 2
                self.character.x = 300

            if self.character.x > 300:
                self.character.x -= VEL

        if keys_pressed[pygame.K_d]:  # Right
            if self.character.x >= 1620:
                self.character.x += VEL / 2
                self.character.x = 1620

            if self.character.x < 1620:
                self.character.x += VEL

        if keys_pressed[pygame.K_w]:  # UP
            if self.character.y <= 300:
                self.background.y -= VEL / 2
                self.character.y = 300

            if self.character.y > 300:
                self.character.y -= VEL

        if keys_pressed[pygame.K_s]:  # DOWN
            if self.character.y >= 780:
                self.background.y += VEL / 2
                self.character.y = 780

            if self.character.y < 780:
                self.character.y += VEL

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
