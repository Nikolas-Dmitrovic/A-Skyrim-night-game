import pygame
from GLOBAL_VARIABLES import WIN


class triggers:
    def __init__(self, character, data, movementObject):
        self.character = character
        self.data = data
        self.movementObject = movementObject
        self.detectionList = list()
        self.unpacker()

    def unpacker(self):
        # TODO add type recognition

        for i in self.data["triggers"]["triggers_info"]:
            self.detectionList.append(pygame.Rect(self.data["triggers"]["triggers_info"][i]["cords"][0],
                                                  self.data["triggers"]["triggers_info"][i]["cords"][1],
                                                  self.data["triggers"]["triggers_info"][i]["dims"][0],
                                                  self.data["triggers"]["triggers_info"][i]["dims"][1]))

    def detection(self, test=False, surface=WIN):
        for i in self.detectionList:
            if test:
                self.drawBoxes(i,surface)
            if self.character.colliderect(i):
                keys_pressed = pygame.key.get_pressed()
                self.movementObject.stop_character(keys_pressed)

    @staticmethod
    def drawBoxes(rect, surface):
        pygame.draw.rect(surface, (0, 0, 0), rect)
