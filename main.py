# TODO create animatic modal and implement into stage modal
# TODO move all state changes into a single class
# TODO add basic config json file to change stuff like movement speed

# TODO imports all the scripts and code library's
import pygame
from main_menu import Gamestate_main_menu
from stageOne import stage_one

pygame.init()
pygame.display.set_caption("12")
# from timings_classes import timing

game_state = Gamestate_main_menu()
mainMenu = True
stage = stage_one()


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        if not mainMenu:
            check = game_state.state_manager()

        if mainMenu:
            stage.state_manager()

    pygame.quit()


if __name__ == "__main__":
    main()
