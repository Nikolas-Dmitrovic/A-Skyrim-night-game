import pygame
from GLOBAL_VARIABLES import WIN, WHITE


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


class text_box:
    class decorators:

        # tract current text index to be able to pick next text file
        @classmethod
        def tract_index(cls, func):
            def wrapper():
                func()

            return wrapper

    text_box_rect = pygame.Rect(0, 0, 100, 100)

    def __init__(self, surface):
        self.surface = surface
        print(text_box.text_box_rect)

    def draw_textbox(self):
        pygame.draw.rect(self.surface, WHITE, text_box.text_box_rect)

    @decorators.tract_index
    def open_text(self):
        pass
        # open json index file

        # create function to track current index in index file

        # set variable to text file

        # text = open("filename","r")

        # return textvariable

    def text_display(self):
        font = pygame.font.Font('DarkXShadowSkyrim.ttf', 16)

        # place this in for loop and change y positon after every line
        # clear text area to black after it is filled with text
        '''text = font.render(self.text, True, WHITE)
        textRect = text.get_rect()
        textRect.center = (self.x, self.y)
        WIN.blit(text, textRect)'''

# print text to screen

# control text speed

# add skip forward stuff
