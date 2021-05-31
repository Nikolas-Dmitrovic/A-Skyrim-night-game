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
    text_box_rect = pygame.Rect(0, 0, 1000, 100)

    def __init__(self, surface, text_file):
        self.surface = surface
        self.text = text_file
        self.text.lines = list()
        self.textSize = 24
        self.font = pygame.font.Font('DarkXShadowSkyrim.ttf', self.textSize)

        # text lines rect peramiters
        self.lineOneX = None  # all x and y cords for top left corner of box
        self.lineOney = None
        self.lineTwoX = None
        self.lineTWOY = None
        self.indexLineOne = 0
        self.indexLineTwo = 1

        # text hiding block
        # TODO change dims to make then all fit and work nicely
        self.block = pygame.Rect(0, 0, 1000, 100)
        self.moveDownAmount = 120  # number in pixels
        self.moveCounter = 0

    def draw_textbox(self):
        pygame.draw.rect(self.surface, WHITE, text_box.text_box_rect)

    def text_unpacker(self):
        for lines in self.text:
            self.text.lines.append(lines)

    def text_writer(self):
        text1 = self.font.render(self.text.lines[0], True, WHITE)
        textRect1 = text1.get_rect()
        textRect1.topleft = (self.lineOneX, self.lineOney)

        text2 = self.font.render(self.text.lines[1], True, WHITE)
        textRect2 = text2.get_rect()
        textRect2.topleft = (self.lineTwoX, self.lineTWOY)

        WIN.blit(text1, textRect1)
        WIN.blit(text2, textRect2)

    def text_cover(self):
        pygame.draw.rect(self.surface, WHITE, self.block)
        pass

    def text_animation(self):

        self.text_writer()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.moveCounter > 2:
                        self.block.x -= self.moveDownAmount
                        self.moveCounter += 1
                    if self.moveCounter == 2:
                        self.block.x += 2 * self.moveDownAmount
                        self.moveCounter = 0
                        self.indexLineTwo += 2
                        self.indexLineTwo += 2

                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()

        pass

    # def text_display(self):
