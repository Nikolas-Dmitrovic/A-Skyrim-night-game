#  done - def draw npc
# def npc movement handler
# def npc events- includes movement activation and text triggers
import pygame
import os
from GLOBAL_VARIABLES import WIN, WHITE




# temp test path add this to json file afterwords
path = ((1,1),(2,2))

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
        WIN.fill(WHITE)
        WIN.blit(self.npc, (self.character.x, self.character.y))

    def npc_handel_movements(self, path):
        # create path list where each index is two cords(pos 1 and pos 2) where path is from pos 1 to pos 2
        for i in path:

        pass
