import pygame
from GLOBAL_VARIABLES import WIN


class triggers:
    def __init__(self, character, data, movementObject = None):

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


class state_triggers:
    def __init__(self, data, character = None) -> None:

        self.data = data
        self.character = character

        #[rect, nextstage]
        self.onRectCollison = list()
        self.onPassingLimit = list()
        self.onRectColliosnAndUserInput = list()

        self.exitUnpacker()


    def exitUnpacker(self):
        exits = self.data["stageone"]["stage exits"]

        for i in exits:
            
            if i[1] == "collison":
                self.onRectCollison.append(pygame.Rect(i[2][0],i[2][1],i[2][2],i[2][3]),i[0])

            elif i[1] == "collisonKeydown":
                self.onRectColliosnAndUserInput.append(pygame.Rect(i[2][0],i[2][1],i[2][2],i[2][3]), i[0])

            elif i[1] == "limit":
                self.onPassingLimit.append(pygame.Rect(i[2][0],i[2][1],i[2][2],i[2][3]),i[0])


    def detection(self):
        for i in self.onRectCollison:
            if self.character.colliderect(i[0]):
                return i[1]

        for i in self.onPassingLimit:
            if self.character.colliderect(i[0]):
                return i[1]

        for i in self.onRectColliosnAndUserInput:
            if self.character.colliderect(i[0]):
                for event in pygame.event.get():
                    # TODO modify to get key down from datapack
                    if event.key == pygame.K_RETURN:
                        return i[1]
                        



