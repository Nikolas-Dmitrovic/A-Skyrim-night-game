'''
creates a event object for custom level scrips and npc moves or something lmao
create triggers first to see if this is needed

'''
# TODO create events format in json file
import pygame
import timeings_classes as time


class events:
    def __init__(self, character, npcObject, data=None):

        self.character = character

        if data is None:
            self.data = list()

        if data is not None:
            self.data = data

        self.npcObject = npcObject
        self.triggersList = list()
        self.onStartMovement = list()

    def stage_events_JsonUnpacker(self):

        if self.data is not None:

            for i in self.data["events"]:

                if self.data["events"][i]["type"] == "trigger":

                    event = self.data["events"][i]["reckt"]
                    self.triggersList.append(pygame.Rect(event[0], event[1], event[2], event[3]))

                if self.data["events"][i]["type"] == "onLevelStart":
                    self.onStartMovement.append(self.data["events"[i]["path"]])

        if self.data is None:
            pass
            # enter code here lol

    def addEvent(self, rect, func):
        pass

    def event_trigger_check(self, func):
        for i in self.triggersList:
            
            if self.character.colliderect(i):
                func()

    def event_onStart_check(self, wait, func):
        if time.waitFor(wait):
            func(self.onStartMovement)
