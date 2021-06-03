import pygame
from GLOBAL_VARIABLES import VEL


class movement:

    def __init__(self, data, character, background, limits):
        self.data = data
        self.character = character
        self.background = background
        self.limits = limits  # list of hard limits which follows the format of (x left, x right, y up, y down)
        self.x_left = self.limits[0]
        self.x_right = self.limits[1]
        self.y_up = self.limits[2]
        self.y_down = self.limits[3]
        self.VEL = 5

    def handle_movment(self, keys_pressed):
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