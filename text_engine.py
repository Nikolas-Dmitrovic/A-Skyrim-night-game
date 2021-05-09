import pygame
from GLOBAL_VARIABLES import WIN


class menu_text:
    def __init__(self, text, x, y, size):
        self.text = text
        self.x = x
        self.y = y
        self.size = size


    def display_text(self):
        font = pygame.font.Font('DarkXShadowSkyrim.ttf', self.size)
        text = font.render(self.text, True, WHITE)
        textRect = text.get_rect()
        textRect.center = (self.x, self.y)
        WIN.blit(text, textRect)

    def text_size(self, size):
        self.size = size


# TODO fill in code and fit it all into a class

# draw text box
text_box = pygame.Rect(0, 0, 100, 100)

# create a text box image style shit you know
# text_box_image = # make and load in a image lol

'''def draw_window_stage1(textbox):
    WIN.blit(STAGE, (backgroundimage.x, backgroundimage.y))
    pygame.display.update()'''


# open file

'''
text = open("filename","r")
'''

# print text to screen

# control text speed

# add skip forward stuff
