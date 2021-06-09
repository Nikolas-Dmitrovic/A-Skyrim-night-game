# TODO create animatic modal and implement into stage modal
# TODO move all state changes into a single class
# TODO add basic config json file to change stuff like movement speed

# TODO imports all the scripts and code library's
import pygame
from main_menu import Gamestate_main_menu
from stageOne import stage_one

pygame.init()

# TODO screen constants and initialise screen
# TODO make changes to change scream size and resolution
# from timeings_classes import timing

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
    # main()

    def switch_demo(argument):

        def left():
            print("hello")

        switcher = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: left()
        }
        switcher.get(argument, "Invalid month")
    switch_demo(12)
