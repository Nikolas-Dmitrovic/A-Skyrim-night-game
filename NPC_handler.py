# def npc events- includes movement activation and text triggers
import pygame
import os
from GLOBAL_VARIABLES import WIN, WHITE
import timeings_classes as time


# temp test path add this to json file afterwords
# path = ((1,1),(2,2))
VEL = 5

class NPC:
    def __init__(self, data, npcDataIndex, movement = False, poggers = False):
        self.data = data
        # TODO add these fields to level one json and modify indexes here
        self.character = pygame.Rect(data["npc"]["npcStartPosition"][0],
                                     data["npc"]["npcStartPosition"][1],
                                     data["main_character"]["rect_dim_x"], data["main_character"]["rect_dim_y"])
        self.npc = pygame.transform.rotate(
            pygame.transform.scale(
                pygame.image.load(
                    os.path.join(data["main_character"]["file_location"], data["main_character"]["file_name"])),
                (192, 108)), 0)
        if movement:
            self.path = data["npc"]["npc_info"][npcDataIndex]["npc_movement_path"]
            self.movement_setup_token = 0
            self.movementObjs = list()
            self.currentMoveObjectIndex = 0
            self.currentMoveObjectTick = 1
            self.path_unpacker()

        self.npc_text = data["npc"]["npc_info"][npcDataIndex]["npc_dialog_file_location"]
        if poggers:
            print('hello')

    def draw_npc(self):
        WIN.blit(self.npc, (self.character.x, self.character.y))

    # create a counter system that ticks up once a full movement is complete to then select the next object in a list

    def path_unpacker(self):
        if self.movement_setup_token == 0:
            for i in range(len(self.path) - 1):
                self.movementObjs.append(paths(self.path[i], self.path[i + 1]))
                self.movement_setup_token = 1
        if self.movement_setup_token != 0:
            pass

    def move(self):
        obj = self.movementObjs[self.currentMoveObjectIndex]
        if obj.movementTicks >= self.currentMoveObjectTick:
            if obj.path.slope.horizontal:
                if obj.effectic_distance > 0:
                    self.character.x += VEL
                if obj.effectic_distance < 0:
                    self.character.x -= VEL

            if obj.path.slope.vertical:
                if obj.effectic_distance > 0:
                    self.character.y += VEL
                if obj.effectic_distance < 0:
                    self.character.y -= VEL

            # finish not horizontal or vertical movements
            if not obj.path.slope.horizontal and not obj.path.slope.vertical:
                pass
        if obj.movementTicks < self.currentMoveObjectTick:
            if self.currentMoveObjectIndex <= len(self.movementObjs):
                self.currentMoveObjectIndex += 1
                self.currentMoveObjectTick = 1


# make objects for individual objects
class paths:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        self.p1.x = self.p1[0]
        self.p1.y = self.p1[1]
        self.p2.x = self.p2[0]
        self.p2.y = self.p2[1]

        self.path = (p1, p2)
        self.path.distance = (self.p2.x - self.p1.x), (self.p2.y - self.p1.y)
        self.path.distance.x = self.p2.x - self.p1.x
        self.path.distance.y = self.p2.y - self.p1.y

        self.path.slope = self.slope()
        self.path.slope.horizontal = None
        self.path.slope.vertical = None

        self.effectic_distance = self.dis()
        self.movementTicks = self.getTicks()

    def __repr__(self) -> str:
        pass

    def __add__(self):
        pass

    def slope(self):

        if self.path.distance.x > 0 and self.path.distance.y > 0:
            slope = self.path.distance.x / self.path.distance.y
            return slope

        if self.path.distance.x == 0:
            self.path.slope.horizontal = False
            self.path.slope.vertical = True

        if self.path.distance.y == 0:
            self.path.slope.horizontal = True
            self.path.slope.vertical = False

    def dis(self):
        if self.path.slope.horizontal:
            return self.path.distance.x

        if self.path.slope.vertical:
            return self.path.distance.y

        if not self.path.slope.horizontal and not self.path.slope.vertical:
            dist = ((self.path.distance.x ^ 2) + (self.path.distance.x ^ 2)) ^ (1 / 2)

            return dist

    def getTicks(self):
        ticks = self.effectic_distance / VEL
        return int(ticks)
