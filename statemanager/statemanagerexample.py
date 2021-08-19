# python version of statemanager to firgure out alorithmic aspects 
# and quick proplem solving
import sys

# rebuilt stage one to conform to this shit lmao

class teststate:
    def __init__(self) -> None:
        pass 

    def __repr__(self):
        return "state"        

    def draw(self):
        pass
    def update(self):
        pass
    def destroy(self):
        pass


class statemanager:
    def __init__(self) -> None:
        self.stack = list()
        self.top = -1

    # statemanager functions
    """top function does not work and i have no clue why"""
    def top(self):
        return self.stack[self.top]

    def pop(self):
        if (self.top == -1): return 0
        self.stack[self.top].destory()
        del self.stack[self.top]
        self.top -= 1
        return self.top


    def free(self):
        self.pop()
        while(self.top > -1):
            self.pop()
        return 0

    def push(self, state):
        self.top += 1;
        self.stack.append(state)
        

    # note scale is not needed thanks to pythons dynamic memory allocation

    def update(self):
        self.stack[self.top].update()

    def draw(self):
        self.stack[self.top].draw()

    # stack manaipulation shit lol
    """def pushtobottom(self, bottomstate):
        bottomindex = 0
        tempstate = None

        tempstate = self.stack[bottomindex]"""