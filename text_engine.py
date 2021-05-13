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


class text_box:
    text_box_rect = pygame.Rect(0, 0, 1000, 100)

    def __init__(self, surface, text_file):
        self.surface = surface
        self.text = text_file

    def draw_textbox(self):
        pygame.draw.rect(self.surface, WHITE, text_box.text_box_rect)

    # add async timings and skip function for this lol
    def text_display(self):

        font = pygame.font.Font('DarkXShadowSkyrim.ttf', 16)
        textvar = open(self.text, "r")
        x = 0

        for i in textvar:
            text = font.render(i, True, WHITE)
            textRect = text.get_rect()

            time_delay = 500  # 0.5 seconds
            timer_event = pygame.USEREVENT + 1
            pygame.time.set_timer(timer_event, time_delay)

            for event in pygame.event.get():
                if event == timer_event:



                    # optimise if statements and create recursive function for it
                    if x == 0:
                        textRect.center = (800, 900)
                        WIN.blit(text, textRect)
                        x += 1

                    if x == 1:
                        textRect.center = (800, 1000)
                        WIN.blit(text, textRect)
                        x += 1

                    if x == 2:
                        x = 0
                        self.draw_textbox()
                        textRect.center = (800, 1000)
                        WIN.blit(text, textRect)
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        pygame.quit()
                        sys.exit()
