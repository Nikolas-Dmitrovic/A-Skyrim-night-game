# TODO create animatic modal and implement into stage modal
# TODO move all state changes into a single class
# TODO add basic config json file to change stuff like movement speed

# TODO imports all the scripts and code library's
import pygame
from pygame.time import Clock
from main_menu import Gamestate_main_menu
from state import stage_one
from statemanager.statemanagerexample import statemanager as statemanagerclass
import os
import json
# import time

pygame.init()
# pygame.display.set_caption("12")
# from timings_classes import timing


file = open(os.path.join('statemanager', 'statemanager.json'))
data = json.load(file)

clock =  pygame.time.Clock()


# time_start = time.time()
game_state = Gamestate_main_menu()
mainMenu = True

firstStateName = "stageone"
cuurentStateIndex = "stageone"

statemanager = statemanagerclass()


""" before while loop push basic states like menus and shit"""
state = stage_one(data["stageone"]["json_file"], data["stageone"]["json_file_location"], exit_data= data, clock= clock)
statemanager.push(state)

# TODO add defult menu states at common indexs ex) [0] to [5]            

"""
if preformace degrades too much or fps drops below 50
TODO create regions for the state manager to load
TODO create pop calls before entering new reigion to reduce memory usage

"""

"""

TODO clip character images better lmao 


"""


def main(counter = 0, exitstate = None):
    run = True
    while run:

        state = statemanager.stack[statemanager.top]
        exitstate = state.state
        if exitstate != None:
            newstate = stage_one(data[exitstate]["json_file"], data[exitstate]["json_file_location"], exit_data= data, clock = clock)
            statemanager.push(newstate)
            exitstate = None

        # statemanager.update()
        statemanager.draw()
        # pygame.display.update()
        # counter += 1
        # print(clock.get_fps())
        # print(dounter)
        #if counter >= 600:
        #    statemanager.pop()

        clock.tick(144)



    pygame.quit()


if __name__ == "__main__":
    main()
