# TODO create trigger event
# TODO optimise code
# TODO add code to close opened files and shit
# TODO resize character box to make collisions more effective


import sys
import pygame
from GLOBAL_VARIABLES import WIN, WHITE, VEL
import os
import json
from text_engine import text_box
from NPC_handler import NPC
from movement import movement, animated_movement
from triggers import triggers

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
def draw_window_stage1(backgroundimage, characterimage):
    WIN.fill(WHITE)
    WIN.blit(STAGE, (backgroundimage.x, backgroundimage.y))
    WIN.blit(MAIN_CHARACTER, (characterimage.x, characterimage.y))


def getPos() -> tuple:
    return character.x, character.y


class stage_one:
    def __init__(self, datas=None):

        """
        f = open(os.path.join('level data', 'level_one.json'))
        data = json.load(f)

        character = pygame.Rect(data["main_character"]["starting_positionx"],
                                data["main_character"]["starting_positiony"],
                                data["main_character"]["rect_dim_x"], data["main_character"]["rect_dim_y"])
        background = pygame.Rect(0, 0, data["background"]["level_x_dim"], data["background"]["level_y_dim"])

        MAIN_CHARACTER = pygame.transform.rotate(
            pygame.transform.scale(
                pygame.image.load(
                    os.path.join(data["main_character"]["file_location"], data["main_character"]["file_name"])),
                (192, 108)), 0)
        STAGE = pygame.transform.rotate(
            pygame.transform.scale(
                pygame.image.load(
                    os.path.join(data["background"]["base_level_location"], data["background"]["file_name"])),
                (1920, 1080)), 0)


        """

        self.state = 'stage'
        self.background = background
        self.character = character
        # self.npcOne = NPC(data, "npc1", movement=False)
        self.play_movement = movement(data, self.character, self.background)
        self.text = text_box(STAGE, "sample text file")
        self.triggers = triggers(character, data, self.play_movement)

    def load_stage(self):

        self.quit_check()
        WIN.fill(WHITE)
        keys_pressed = pygame.key.get_pressed()
        self.play_movement.handle_movement(keys_pressed, (
            (self.character.x <= 190), (self.character.x >= 1500), (self.character.y <= 100),
            (self.character.y >= 980)))
        draw_window_stage1(background, character)
        # print(getPos())
        self.triggers.detection(test=True, surface=STAGE)
        # WIN.blit(STAGE, (self.background.x, self.background.y))

        # self.npcOne.draw_npc()

        # self.text.draw_textbox()
        # self.text.text_animation()

        pygame.display.update()

    def drawWindowStage(self, backgroundimage, characterimage):
        WIN.fill(WHITE)
        WIN.blit(STAGE, (backgroundimage.x, backgroundimage.y))
        WIN.blit(MAIN_CHARACTER, (characterimage.x, characterimage.y))

    @staticmethod
    def quit_check():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(1)
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print(2)
                    run = False
                    pygame.quit()
                    sys.exit()

    def closeStage(self) -> None:
        """
        close text and json files
        """

        pass

    def state_manager(self):
        if self.state == 'stage':
            self.load_stage()
