# TODO create animatic modal and implement into stage modal
# TODO move all state changes into a single class
# TODO add basic config json file to change stuff like movement speed

# TODO imports all the scripts and code library's
import pygame
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




# time_start = time.time()
game_state = Gamestate_main_menu()
mainMenu = True

"""
TODO create events that trigger the event manager to progress
ie go though door and enter a new stage

make statemanager check var in state to see if actions are needed


make a text file to figure out algorithm step by step for this

"""
firstStateName = "stageone"
cuurentStateIndex = "stageone"

statemanager = statemanagerclass()


""" before while loop push basic states like menus and shit"""
state = stage_one(data["stageone"]["json_file"], data["stageone"]["json_file_location"], exit_data= data)
statemanager.push(state)


if state.nextState == True:
    """ add exit condions to the statemanager.json"""
    "create temp triggers based on the exit conditions"
    """ check if the condions are archived with the events module"""
    """ return the name of the next state to add to the stack"""
    """ do something"""


    """
    create defult exit triggers; builders and checkers for each trigger
    on collison
    on passing limit
    on colliosn and user input/keydown

    TODO finish exit upacker in the tiggers.py module
    
    
    """
    pass


def main(counter = 0):
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        statemanager.update()
        statemanager.draw()
        counter += 1
        print(counter)
        if counter >= 600:
            statemanager.pop()



    pygame.quit()


if __name__ == "__main__":
    main()
