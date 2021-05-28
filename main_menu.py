# TODO play music in main menu
# TODO make text pulse when hovering over instead of being static

import pygame
import time
import os
import sys
from text_engine import menu_text

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)

MAIN_MENU = pygame.image.load(os.path.join('Main_menu.jpg'))

# blank image
select_image_raw = pygame.image.load(os.path.join('select_image.png'))
select_image = pygame.transform.rotate(pygame.transform.scale(select_image_raw, (55, 40)), 0)




# cursor rectangle
select = pygame.Rect(1000, 250, 10, 10)

t1 = menu_text('New Game', 900, 250, 72)
t2 = menu_text('Continue', 900, 400, 72)
t3 = menu_text('Settings', 900, 550, 72)


def draw_window_menu(pos):
    WIN.fill(WHITE)
    WIN.blit(MAIN_MENU, (0, 0))
    WIN.blit(select_image, pos)
    menu_text.display_text(t1)
    menu_text.display_text(t2)
    menu_text.display_text(t3)
    # draws in text
    font = pygame.font.Font('DarkXShadowSkyrim.ttf', 72)

    pygame.display.update()


def menu_selection(key_pressed, select):
    # detects which option is curently being hovered over
    if select.y == 250:
        menu_text.text_size(t1, 100)
        menu_text.text_size(t2, 72)
        menu_text.text_size(t3, 72)

    if select.y == 400:
        menu_text.text_size(t1, 72)
        menu_text.text_size(t2, 100)
        menu_text.text_size(t3, 72)

    if select.y == 550:
        menu_text.text_size(t1, 72)
        menu_text.text_size(t2, 72)
        menu_text.text_size(t3, 100)


# into images or gif imported and set as class variables

# find better image that is 1920 by 1080
art_image_0 = pygame.image.load(os.path.join('introArt', 'skyrimart.jpg'))
# art_image_0 = pygame.transform.rotate(pygame.transform.scale(art_image_raw0,()), 0)
art_image_raw1 = pygame.image.load(os.path.join('introArt', 'skyrimart1.jpg'))
art_image_raw2 = pygame.image.load(os.path.join('introArt', 'skyrimart2.jpg'))
art_image_raw3 = pygame.image.load(os.path.join('introArt', 'skyrimart3.jpg'))


# loads sound for into section
# intro_sound = pygame.mixer.Sound('intro_song.mp3')


class Gamestate_main_menu:
    def __init__(self):
        self.state = 'main_menu'

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_DOWN:
                    select.y += 150

                if event.key == pygame.K_UP:
                    select.y -= 150

                if event.key == pygame.K_DOWN and select.y > 550:
                    select.y = 250

                if event.key == pygame.K_UP and select.y < 250:
                    select.y = 550

                # detects if selection object is over the new game menu and enter is pressed
                if event.key == pygame.K_RETURN and select.y == 250:
                    self.state = 'intro_screen'

        draw_window_menu(select)
        key_pressed = pygame.key.get_pressed()
        menu_selection(key_pressed, select)

    def intro_sceen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()

        WIN.blit(art_image_0, (0, 0))
        intro_sound = pygame.mixer.Sound(os.path.join('Music', 'intro_song.mp3'))
        intro_sound.play()
        pygame.display.update()
        time.sleep(3)
        WIN.blit(art_image_raw1, (0, 0))
        pygame.display.update()
        time.sleep(3)
        WIN.blit(art_image_raw2, (0, 0))
        pygame.display.update()
        time.sleep(3)
        WIN.blit(art_image_raw3, (0, 0))
        pygame.display.update()
        time.sleep(3)
        intro_sound.stop()
        self.state = 'stop'

    def state_manager(self):
        if self.state == 'main_menu':
            self.main_game()
        if self.state == 'intro_screen':
            self.intro_sceen()
        if self.state == 'stop':
            return False
