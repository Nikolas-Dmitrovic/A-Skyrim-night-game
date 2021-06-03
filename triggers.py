import pygame


class triggers:
    def __init__(self, character, data, movementObject):
        self.character = character
        self.data = data
        self.movementObject = movementObject
        self.list = list()
        self.unpacker()

    def unpacker(self):
        for i in self.data["triggers"]["triggers_info"]:
            self.list.append(pygame.Rect(self.data["triggers"]["triggers_info"][i]["cords"][0],
                                         self.data["triggers"]["triggers_info"][i]["cords"][1],
                                         self.data["triggers"]["triggers_info"][i]["dims"][0],
                                         self.data["triggers"]["triggers_info"][i]["dims"][1]))

    def detection(self):
        for i in self.list:
            if self.character.colliderect(i):
                # self.movement_object.do something lmao()
                keys_pressed = pygame.key.get_pressed()
                self.movementObject.stop_character()
