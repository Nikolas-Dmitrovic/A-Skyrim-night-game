import pygame
from pygame import image
from GLOBAL_VARIABLES import WIN
import os

# movement without any animations
class movement:

    def __init__(self, data, character, background, clock):
        self.data = data
        self.character = character
        self.background = background
        self.x_left = None
        self.x_right = None
        self.y_up = None
        self.y_down = None
        self.clock = clock


    def handle_movement(self, keys_pressed, limits):
        self.x_left = limits[0]
        self.x_right = limits[1]
        self.y_up = limits[2]
        self.y_down = limits[3]

        if not self.data["background"]["movable"]:
            self.handle_movement_background_static(keys_pressed)

        if self.data["background"]["movable"]:
            self.background_handle_movement(keys_pressed)

    def handle_movement_background_static(self, keys_pressed):
        if keys_pressed[pygame.K_a]:  # LEFT
            self.character.x -= self.VEL()
            if self.x_left:
                self.character.x += self.VEL()

        if keys_pressed[pygame.K_d]:  # Right
            self.character.x += self.VEL()
            if self.x_right:
                self.character.x -= self.VEL()

        if keys_pressed[pygame.K_w]:  # UP
            self.character.y -= self.VEL()
            if self.y_up:
                self.character.y += self.VEL()

        if keys_pressed[pygame.K_s]:  # DOWN
            self.character.y += self.VEL()
            if self.y_down:
                self.character.y -= self.VEL()

    def background_handle_movement(self, keys_pressed):
        # TODO create limits to read from json file
        # TODO rework limits
        if keys_pressed[pygame.K_a]:  # LEFT
            if self.x_left:
                self.background.x -= self.VEL() / 2
                self.character.x = 300

            if self.character.x > 300:
                self.character.x -= self.VEL()

        if keys_pressed[pygame.K_d]:  # Right
            if self.x_right:
                self.background.x += self.VEL() / 2
                self.character.x = 1620

            self.character.x += self.VEL()

        if keys_pressed[pygame.K_w]:  # UP
            if self.y_up:
                self.background.y -= self.VEL() / 2
                self.character.y = 300

            self.character.y -= self.VEL()

        if keys_pressed[pygame.K_s]:  # DOWN
            if self.y_down:
                self.background.y += self.VEL() / 2
                self.character.y = 780

            self.character.y += self.VEL()

    def stop_character(self, key_pressed):
        if key_pressed[pygame.K_a]:  # left
            self.character.x += self.VEL()
        if key_pressed[pygame.K_d]:  # left
            self.character.x -= self.VEL()
        if key_pressed[pygame.K_w]:  # left
            self.character.y += self.VEL()
        if key_pressed[pygame.K_s]:  # left
            self.character.y -= self.VEL()

    def VEL(self):
        return round((300)/self.clock.get_fps())


class animated_movement:

    def __init__(self, data, character, background, clock):
        self.data = data
        self.character = character
        self.background = background
        self.x_left = None
        self.x_right = None
        self.y_up = None
        self.y_down = None
        # self.VEL = 5
        self.clock = clock

        # animation data

        # gives number of animations per movement direction
        self.numberOfanimations = data["main_character"]["number of animations"]
        self.animationIndexer = 0  # set the max to numberOfAnimations
        self.animationImagesLeft = list()
        self.animationIndexLeft = 0
        for i in range(self.numberOfanimations):
            image = pygame.transform.rotate(
                pygame.transform.scale(
                    pygame.image.load(
                        os.path.join(self.data["main_character"]["file_location"],
                                     self.data["main_character"]["animation images left"][0])).convert_alpha(), (192, 108)), 0)
            self.animationImagesLeft.append(image)

        self.animationImagesRight = list()
        self.animationIndexRight = 0
        for i in range(self.numberOfanimations):
            image = pygame.transform.rotate(
                pygame.transform.scale(
                    pygame.image.load(
                        os.path.join(self.data["main_character"]["file_location"],
                                     self.data["main_character"]["animation images right"][0])).convert_alpha(), (192, 108)), 0)
            self.animationImagesRight.append(image)
            

        self.animationImagesForward = list()
        self.animationIndexForward = 0
        for i in range(self.numberOfanimations):
            image = pygame.transform.rotate(
                pygame.transform.scale(
                    pygame.image.load(
                        os.path.join(self.data["main_character"]["file_location"],
                                     self.data["main_character"]["animation images forword"][0])).convert_alpha(), (192, 108)), 0)
            self.animationImagesForward.append(image)
        self.animationImagesBack = list()
        self.animationIndexBack = 0
        for i in range(self.numberOfanimations):
            image = pygame.transform.rotate(
                pygame.transform.scale(
                    pygame.image.load(
                        os.path.join(self.data["main_character"]["file_location"],
                                     self.data["main_character"]["animation images back"][0])).convert_alpha(), (192, 108)), 0)
            self.animationImagesBack.append(image)

    # create standing resent function

    def animation_handler(self, direction):
        def draw(image):
            WIN.blit(image, (self.character.x,self.character.y))
        # figure out timings
        def left():
            draw(self.animationImagesLeft[0])
            '''if self.animationIndexLeft < self.numberOfanimations:
                draw(image)
                self.animationIndexLeft += 1
            if self.animationIndexLeft >= self.numberOfanimations:
                draw(image)
                self.animationIndexLeft = 0'''

        def right():
            draw(self.animationImagesRight[0])
            '''if self.animationIndexRight < self.numberOfanimations:
                draw(image)
                self.animationIndexRight += 1
            if self.animationIndexRight >= self.numberOfanimations:
                draw(image)
                self.animationIndexRight = 0'''

        def forword():
            draw(self.animationImagesForward[0])
            '''if self.animationIndexForward < self.numberOfanimations:
                draw(image)
                self.animationIndexForward += 1
            if self.animationIndexForward <= self.numberOfanimations:
                draw(image)
                self.animationIndexForward = 0'''

        def back():
            draw(self.animationImagesBack[0])

            '''if self.animationIndexBack < self.numberOfanimations:
                draw(image)
                self.animationIndexBack += 1
            if self.animationIndexBack <= self.numberOfanimations:
                draw(image)
                self.animationIndexBack = 0'''

        def getDirection(argument):
            if argument == "left":
                left()
            elif argument == "right":
                right()

            elif argument == "forword":
                forword()
            elif argument == "back":
                back()

            

        getDirection(direction)

    def handle_movement(self, keys_pressed, limits):
        self.x_left = limits[0]
        self.x_right = limits[1]
        self.y_up = limits[2]
        self.y_down = limits[3]

        if not self.data["background"]["movable"]:
            self.handle_movement_background_static(keys_pressed)

        if self.data["background"]["movable"]:
            self.background_handle_movement(keys_pressed)

    def handle_movement_background_static(self, keys_pressed):
        if keys_pressed[pygame.K_a]:  # LEFT
            self.character.x -= self.VEL()
            self.animation_handler("left")
            if self.x_left:
                self.character.x += self.VEL()

        elif keys_pressed[pygame.K_d]:  # Right
            self.character.x += self.VEL()
            self.animation_handler("right")
            if self.x_right:
                self.character.x -= self.VEL()

        elif keys_pressed[pygame.K_w]:  # UP
            self.character.y -= self.VEL()
            self.animation_handler("forword")
            if self.y_up:
                self.character.y += self.VEL()

        elif keys_pressed[pygame.K_s]:  # DOWN
            self.character.y += self.VEL()
            self.animation_handler("back")
            if self.y_down:
                self.character.y -= self.VEL()

        else:
            image = pygame.transform.rotate(
                pygame.transform.scale(
                    pygame.image.load(
                        os.path.join(self.data["main_character"]["file_location"],
                                     self.data["main_character"]["file_name"])).convert_alpha(), (192, 108)), 0)
            WIN.blit(image, (self.character.x, self.character.y))
            # pygame.display.flip()

    def background_handle_movement(self, keys_pressed):
        # TODO create limits to read from json file
        # TODO rework limits
        if keys_pressed[pygame.K_a]:  # LEFT
            if self.x_left:
                self.background.x -= self.VEL() / 2
                self.character.x = 300

            if self.character.x > 300:
                self.character.x -= self.VEL()

        if keys_pressed[pygame.K_d]:  # Right
            if self.x_right:
                self.background.x += self.VEL() / 2
                self.character.x = 1620

            self.character.x += self.VEL()

        if keys_pressed[pygame.K_w]:  # UP
            if self.y_up:
                self.background.y -= self.VEL() / 2
                self.character.y = 300

            self.character.y -= self.VEL()

        if keys_pressed[pygame.K_s]:  # DOWN
            if self.y_down:
                self.background.y += self.VEL() / 2
                self.character.y = 780

            self.character.y += self.VEL()

    def stop_character(self, key_pressed):
        if key_pressed[pygame.K_a]:  # left
            self.character.x += self.VEL()
        if key_pressed[pygame.K_d]:  # left
            self.character.x -= self.VEL()
        if key_pressed[pygame.K_w]:  # left
            self.character.y += self.VEL()
        if key_pressed[pygame.K_s]:  # left
            self.character.y -= self.VEL()


    def VEL(self):
        return round((300)/self.clock.get_fps())