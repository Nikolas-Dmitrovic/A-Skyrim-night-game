import sys
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


# draw text box
# take text file and split into lines
# print text per screen and print a large black block over text
# move block to expose text one letter at a time


class text_box:
    text_box_rect = pygame.Rect(0, 780, 1920, 300)

    def __init__(self, surface, text_file):
        self.surface = surface
        self.text = open(text_file, "r")
        self.text_lines = list()
        self.textSize = 64
        self.font = pygame.font.Font('DarkXShadowSkyrim.ttf', self.textSize)

        # text lines rect parameters
        self.lineOneX = 200  # all x and y cords for top left corner of box
        self.lineOney = 900
        self.lineTwoX = 200
        self.lineTWOY = 1000
        self.indexLineOne = 0
        self.indexLineTwo = 1

        # text hiding block
        # TODO change dims to make then all fit and work nicely
        self.block = pygame.Rect(0, 780, 1920, 1000)
        self.moveDownAmount = 200  # number in pixels
        self.moveCounter = 0

        self.text_unpacker()

    def draw_textbox(self):
        pygame.draw.rect(self.surface, WHITE, text_box.text_box_rect)

    def text_unpacker(self):
        for lines in self.text:
            self.text_lines.append(lines)
            print(lines)

    def text_writer(self):
        text1 = self.font.render(self.text_lines[0], True, (0, 0, 0))
        textRect1 = text1.get_rect()
        textRect1.topleft = (self.lineOneX, self.lineOney)

        text2 = self.font.render(self.text_lines[1], True, (0, 0, 0))
        textRect2 = text2.get_rect()
        textRect2.topleft = (self.lineTwoX, self.lineTWOY)

        WIN.blit(text1, textRect1)
        WIN.blit(text2, textRect2)

    def text_cover(self):
        return pygame.draw.rect(self.surface, (0,0,0), self.block)

    def text_animation(self):

        self.text_writer()
        self.text_cover()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.moveCounter < 3:
                        self.block.y += self.moveDownAmount
                        self.moveCounter += 1
                    if self.moveCounter == 3:
                        self.block.y -= 3*self.moveDownAmount
                        self.moveCounter = 0
                        self.indexLineTwo += 2
                        self.indexLineTwo += 2

                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()
