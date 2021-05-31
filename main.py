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
'''import pygame
from main_menu import Gamestate_main_menu
from stageOne import stage_one'''

# pygame.init()

# TODO screen constants and initialise screen
# TODO make changes to change scream size and resolution
# from timeings_classes import timing



def switch_demo(argument):
    switcher = {
        "a": "January",
        "b": "February",
        "c": "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print(switcher.get(argument, "Invalid month"))

switch_demo("f")


'''
# @timing(60)
def prints():
    print("hello")


class hi():
    def __init__(self,hello):
        self.hi = hello

    def swag(self):
        return self.hi

hello = ("hi","fuck","off","dude","i","sweare","t0","god","9","10","11","12")
objs = list()
for i in range(10):
    objs.append(hi(hello[i]))








run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    prints()

path = ((1, 2), (3, 4))

print(len(path))'''
'''game_state = Gamestate_main_menu()
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
    main()'''
