import pygame
from GLOBAL_VARIABLES import VEL, WIN
import os


# movemnet without any animations
class movement:

    def __init__(self, data, character, background):
        self.data = data
        self.character = character
        self.background = background
        self.x_left = None
        self.x_right = None
        self.y_up = None
        self.y_down = None
        self.VEL = 5

    def handle_movment(self, keys_pressed, limits):
        self.x_left = limits[0]
        self.x_right = limits[1]
        self.y_up = limits[2]
        self.y_down = limits[3]

        if not self.data["background"]["movable"]:
            self.handle_movment_background_static(keys_pressed)

        if self.data["background"]["movable"]:
            self.background_handle_movement(keys_pressed)

    def handle_movment_background_static(self, keys_pressed):
        if keys_pressed[pygame.K_a]:  # LEFT
            self.character.x -= VEL
            if self.x_left:
                self.character.x += VEL

        if keys_pressed[pygame.K_d]:  # Right
            self.character.x += VEL
            if self.x_right:
                self.character.x -= VEL

        if keys_pressed[pygame.K_w]:  # UP
            self.character.y -= VEL
            if self.y_up:
                self.character.y += VEL

        if keys_pressed[pygame.K_s]:  # DOWN
            self.character.y += VEL
            if self.y_down:
                self.character.y -= VEL

    def background_handle_movement(self, keys_pressed):
        # TODO create limits to read from json file
        # TODO rework limits
        if keys_pressed[pygame.K_a]:  # LEFT
            if self.x_left:
                self.background.x -= VEL / 2
                self.character.x = 300

            if self.character.x > 300:
                self.character.x -= VEL

        if keys_pressed[pygame.K_d]:  # Right
            if self.x_right:
                self.background.x += VEL / 2
                self.character.x = 1620

            self.character.x += VEL

        if keys_pressed[pygame.K_w]:  # UP
            if self.y_up:
                self.background.y -= VEL / 2
                self.character.y = 300

            self.character.y -= VEL

        if keys_pressed[pygame.K_s]:  # DOWN
            if self.y_down:
                self.background.y += VEL / 2
                self.character.y = 780

            self.character.y += VEL

    def stop_character(self, key_pressed):
        if key_pressed[pygame.K_a]:  # left
            self.character.x += VEL
        if key_pressed[pygame.K_d]:  # left
            self.character.x -= VEL
        if key_pressed[pygame.K_w]:  # left
            self.character.y += VEL
        if key_pressed[pygame.K_s]:  # left
            self.character.y -= VEL


class animated_movment:

    def __init__(self, data, character, background):
        self.data = data
        self.character = character
        self.background = background
        self.x_left = None
        self.x_right = None
        self.y_up = None
        self.y_down = None
        self.VEL = 5

        # animation data

        # gives number of animations per movement direction
        self.numberOfanimations = data["main_character"]["number of animations"]
        self.animationIndexer = 0  # set the max to numberOfAnimations
        self.animationImagesLeft = list()
        self.animationIndexLeft = 0
        for i in range(self.numberOfanimations):
            self.animationImagesLeft.append(self.data["main_character"]["animation images left"][i])

        self.animationImagesRight = list()
        self.animationIndexRight = 0
        '''
        for i in range(self.numberOfanimations):
            self.animationImagesRight.append(self.data["main_character"]["animation images right"][i])
            

        self.animationImagesForward = list()
        self.animationIndexForward = 0
        for i in range(self.numberOfanimations):
            self.animationImagesForward.append(self.data["main_character"]["animation images forward"][i])

        self.animationImagesBack = list()
        self.animationIndexBack = 0
        for i in range(self.numberOfanimations):
            self.animationImagesBack.append(self.data["main_character"]["animation images back"][i])'''

    # create standing resent function

    def animation_handler(self, direction):

        # figure out timings
        def left():
            # image = self.animationImagesLeft[self.animationIndexLeft]
            image = pygame.transform.rotate(
                pygame.transform.scale(
                    pygame.image.load(
                        os.path.join(self.data["main_character"]["file_location"],
                                     self.data["main_character"]["animation images left"])), (192, 108)), 0)
            if self.animationIndexLeft < self.numberOfanimations:
                WIN.blit(image, (self.character.x, self.character.y))
                print(1)
                self.animationIndexLeft += 1
            if self.animationIndexLeft >= self.numberOfanimations:
                print(2)
                WIN.blit(image, (self.character.x, self.character.y))
                self.animationIndexLeft = 0

        def right():
            pass

        def forward():
            pass

        def back():
            pass

        def getDirection(argument):
            switcher = {
                "left": left(),
                "right": right(),
                "forward": forward(),
                "back": back(),
            }
            switcher.get(argument, "Invalid month")

        getDirection(direction)

    def handle_movment(self, keys_pressed, limits):
        self.x_left = limits[0]
        self.x_right = limits[1]
        self.y_up = limits[2]
        self.y_down = limits[3]

        if not self.data["background"]["movable"]:
            self.handle_movment_background_static(keys_pressed)

        if self.data["background"]["movable"]:
            self.background_handle_movement(keys_pressed)

    def handle_movment_background_static(self, keys_pressed):
        if keys_pressed[pygame.K_a]:  # LEFT
            self.character.x -= VEL
            self.animation_handler("left")
            if self.x_left:
                self.character.x += VEL

        if keys_pressed[pygame.K_d]:  # Right
            self.character.x += VEL
            if self.x_right:
                self.character.x -= VEL

        if keys_pressed[pygame.K_w]:  # UP
            self.character.y -= VEL
            if self.y_up:
                self.character.y += VEL

        if keys_pressed[pygame.K_s]:  # DOWN
            self.character.y += VEL
            if self.y_down:
                self.character.y -= VEL

    def background_handle_movement(self, keys_pressed):
        # TODO create limits to read from json file
        # TODO rework limits
        if keys_pressed[pygame.K_a]:  # LEFT
            if self.x_left:
                self.background.x -= VEL / 2
                self.character.x = 300

            if self.character.x > 300:
                self.character.x -= VEL

        if keys_pressed[pygame.K_d]:  # Right
            if self.x_right:
                self.background.x += VEL / 2
                self.character.x = 1620

            self.character.x += VEL

        if keys_pressed[pygame.K_w]:  # UP
            if self.y_up:
                self.background.y -= VEL / 2
                self.character.y = 300

            self.character.y -= VEL

        if keys_pressed[pygame.K_s]:  # DOWN
            if self.y_down:
                self.background.y += VEL / 2
                self.character.y = 780

            self.character.y += VEL

    def stop_character(self, key_pressed):
        if key_pressed[pygame.K_a]:  # left
            self.character.x += VEL
        if key_pressed[pygame.K_d]:  # left
            self.character.x -= VEL
        if key_pressed[pygame.K_w]:  # left
            self.character.y += VEL
        if key_pressed[pygame.K_s]:  # left
            self.character.y -= VEL