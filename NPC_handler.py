#  done - def draw npc
# def npc movement handler
# def npc events- includes movement activation and text triggers
import pygame
import os
from GLOBAL_VARIABLES import WIN, WHITE


# temp test path add this to json file afterwords
# path = ((1,1),(2,2))6

class NPC:
    def __init__(self, data):
        self.data = data
        # TODO add these fields to level one json and modify indexes here
        self.character = pygame.Rect(data["main_character"]["starting_positionx"],
                                     data["main_character"]["starting_positiony"],
                                     data["main_character"]["rect_dim_x"], data["main_character"]["rect_dim_y"])
        self.npc = pygame.transform.rotate(
            pygame.transform.scale(
                pygame.image.load(
                    os.path.join(data["main_character"]["file_location"], data["main_character"]["file_name"])),
                (192, 108)), 0)

    def draw_npc(self):
        WIN.blit(self.npc, (self.character.x, self.character.y))

    def npc_handel_movements(self, path):
        # create path list where each index is two cords(pos 1 and pos 2) where path is from pos 1 to pos 2
        z = 0
        q = z + 1
        moving_x = True

        pos1_x = path[z][0]
        pos1_y = path[z][1]
        pos2_x = path[q][0]
        pos2_y = path[q][1]

        #  - done - find distance from point a to b for each x and y
        # - done - idenitfy if the change is for x or y
        # - done - calculate how many frames it will take to get to second point
        # use counter to run segment of code for that period of time
        # create switcher function to switch to new path ...
        # add movement stuff

        difx = pos2_x - pos1_x
        dify = pos2_y - pos1_y

        if difx != 0 and dify != 0:
            frames = difx / 60
            if difx > 0:
                self.character.x += 5
                return
            if difx < 0:
                self.character.x -= 5
                return

        if dify != 0 and difx != 0:
            frames = dify / 60
            if dify > 0:
                self.character.y += 5
                return
            if dify < 0:
                self.character.y -= 5
                return

        # diagonal movemnet handler
        if difx != 0 and dify != 0:
            pass

        '''if self.character.x <= 1900-192:

            if moving_x:
                self.character.x += 5

        # z = z + 1

        pass'''
