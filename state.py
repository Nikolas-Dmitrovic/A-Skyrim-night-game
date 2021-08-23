# TODO create trigger event
# TODO optimise code
# TODO add code to close opened files and shit
# TODO resize character box to make collisions more effective

"""

TODO add end of level function that detects player position and triggers the statemanager to do something

"""


import sys
import pygame
from GLOBAL_VARIABLES import WIN, WHITE, VEL
import os
import json
from text_engine import text_box
from NPC_handler import NPC
from movement import movement, animated_movement
from triggers import triggers, state_triggers


class stage_one:
    def __init__(self, jsonfile=None, jsonfileloc = None, exit_data = None):

        
        self.file = open(os.path.join(jsonfileloc, jsonfile))
        data = json.load(self.file)

        self.character = pygame.Rect(data["main_character"]["starting_positionx"],
                                data["main_character"]["starting_positiony"],
                                data["main_character"]["rect_dim_x"], data["main_character"]["rect_dim_y"])
        self.background = pygame.Rect(0, 0, data["background"]["level_x_dim"], data["background"]["level_y_dim"])

        self.MAIN_CHARACTER = pygame.transform.rotate(
            pygame.transform.scale(
                pygame.image.load(
                    os.path.join(data["main_character"]["file_location"], data["main_character"]["file_name"])).convert(),
                (192, 108)), 0)

        """ figure out how to make.covert() work with the background image for preformace increase"""
        self.STAGE = pygame.transform.rotate(
            pygame.transform.scale(
                pygame.image.load(
                    os.path.join(data["background"]["base_level_location"], data["background"]["file_name"])).convert(),
                (1920, 1080)), 0)



        

        self.state = 'stage'
        # self.npcOne = NPC(data, "npc1", movement=False)
        self.play_movement = movement(data, self.character, self.background)
        self.text = text_box(self.STAGE, "sample text file")
        self.triggers = triggers(self.character, data, self.play_movement)
        self.exits = state_triggers(exit_data,self.character)

        self.nextState = False
        self.exit_data = exit_data
        self.state = None

    def playerRect(self):
        return self.character

    def backgroundRect(self):
        return self.background

    def npcRects(self):
        "return npc objects to check shit with this lmao"
        pass

    def destroy(self):
        # unloads stage
        # removes all data like sub objects
        # closes json and text files
        self.file.close()
        self.text.text.close()
        # close text file in texthandler object


    def update(self):

        self.quit_check()
        keys_pressed = pygame.key.get_pressed()
        self.play_movement.handle_movement(keys_pressed, (
            (self.character.x <= 190), (self.character.x >= 1500), (self.character.y <= 100),
            (self.character.y >= 980)))
        # print(self.getPos())
        self.triggers.detection(test=False, surface=self.STAGE)

        # self.npcOne.draw_npc()

        # self.text.draw_textbox()
        # self.text.text_animation()



    def draw(self):
            WIN.fill(WHITE)
            WIN.blit(self.STAGE, (self.background.x, self.background.y))
            WIN.blit(self.MAIN_CHARACTER, (self.character.x, self.character.y))
            pygame.display.update()

    def getPos(self) -> tuple:
        return self.character.x, self.character.y


    
    def quit_check(self):
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

            for i in self.exits.onRectCollison:
                if self.exits.character.colliderect(i[0]):
                    self.state =  i[1]

            for i in self.exits.onPassingLimit:
                if self.exits.character.colliderect(i[0]):
                    self.state =  i[1]


            for i in self.exits.onRectColliosnAndUserInput:
                #triggers.drawBoxes(i[0], WIN)
                pygame.draw.rect(WIN, (0, 0, 0), i[0])
                pygame.display.flip()

                if self.exits.character.colliderect(i[0]):
                    # TODO modify to get key down from datapack
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            print("i have no clue lmao")
                            self.state =  i[1]

    #figures out what conditon was met and returns the next state
    def nextstate(self):
        if self.nextState == True:
            return self.state
