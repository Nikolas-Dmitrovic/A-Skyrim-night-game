# TODO create
# TODO create stage class takes the stage, and triggering points as input
# TODO create animatic modal and implement into stage modal
# TODO create level loader modal
# TODO create movement logic modal
# TODO create character class
# TODO move all state changes into a single class
# TODO make a scene changer modual
# TODO add basic config json file to change stuff like movement speed

# TODO imports all the scripts and code library's
import pygame
from main_menu import Gamestate_main_menu
from stageOne import stage_one

# pygame.init()

# TODO screen constants and initialise screen
# TODO make changes to change scream size and resolution
from timeings_classes import timing


@timing(60)
def prints():
    print("hello")


'''run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    prints()'''

path = ((1, 2), (3, 4))

print(path[0][1])
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
