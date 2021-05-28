#  done - def draw npc
# - done - def npc movement handler
# def npc events- includes movement activation and text triggers
import pygame
import os
from GLOBAL_VARIABLES import WIN, WHITE, VEL
import timeings_classes as time


# temp test path add this to json file afterwords
# path = ((1,1),(2,2))6


class NPC:
    def __init__(self, data, movement, path=((0, 0), (0, 0))):
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
        if movement:
            self.path = path
            self.movement_setup_token = 0
            self.movementObjs = list()
            self.currentMoveObjectIndex = 0
            self.currentMoveObjectTick = 1
            self.path_unpacker()

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

    '''def npc_handel_movements(self, path):
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

        count =

        if difx != 0 and dify != 0:
            frames = difx / 60
            if difx > 0:
                self.character.x += 5

            if difx < 0:
                self.character.x -= 5

        if dify != 0 and difx != 0:
            frames = dify / 60
            if dify > 0:
                self.character.y += 5

            if dify < 0:
                self.character.y -= 5

        # diagonal movemnet handler
        if difx != 0 and dify != 0:
            pass

        if self.character.x <= 1900-192:

            if moving_x:
                self.character.x += 5

        # z = z + 1

        pass

    # figure out movement count variables
    @time.do_for(5)
    def movement_statments(self):
        if difx != 0 and dify != 0:
            frames = difx / 60
            if difx > 0:
                self.character.x += 5

            if difx < 0:
                self.character.x -= 5

        if dify != 0 and difx != 0:
            frames = dify / 60
            if dify > 0:
                self.character.y += 5

            if dify < 0:
                self.character.y -= 5

        # diagonal movemnet handler
        if difx != 0 and dify != 0:
            pass

        if self.character.x <= 1900-192:

            if moving_x:
                self.character.x += 5

        # z = z + 1
'''
