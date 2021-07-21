#include "statemanager.h" 
#include<stdio.h>
#include<stdlib.h>
#include "pythondevfiles/include/python.h"

// TODO implement state index in stack


unsigned returnNum(){
    return 1;
}

State build(FnPrt init, FnPrt update, FnPrt draw, FnPrt destroy){
    State name1;
    name1.init = init;
    name1.update = update;
    name1.draw = draw;
    name1.destroy = destroy;

    return name1;
}

void rebuild(State state1, FnPrt init, FnPrt update, FnPrt draw, FnPrt destroy){
    state1 = build(init,update,draw,destroy);
}

int STATEMANAGER_init(StateManager *statemanager) {
  statemanager -> capacity = 3;
  statemanager -> stack = malloc(statemanager -> capacity * sizeof(State*));
  statemanager -> top = -1;
  return 0;
}

int STATEMANAGER_free(StateManager *statemanager) {
  do {
    STATEMANAGER_pop(statemanager);
  } while (statemanager -> top > -1);
  free(statemanager -> stack);
  return 0;
}

int STATEMANAGER_scale(StateManager *statemanager){
    statemanager -> capacity *= 2;
    statemanager -> stack = realloc(statemanager ->stack, statemanager-> capacity * sizeof(State*));
    return statemanager -> capacity;
}

int STATEMANAGER_push(StateManager *statemanager, State *state){
    if(statemanager -> top + 1 == statemanager -> capacity) STATEMANAGER_scale(statemanager);
    statemanager -> top++;
    statemanager -> stack[statemanager ->top] = state;
    if (state -> init != NULL) state ->init;
    return statemanager->top;

}

int STATEMANAGER_pop(StateManager *statemanager){

    if(statemanager -> top == -1) return 0;
    State *top = STATEMANAGER_top(statemanager);
    if(top -> destroy != NULL) top -> destroy();
    statemanager -> stack[statemanager -> top] = NULL;
    statemanager -> top--;
    return statemanager -> top;
}

int *STATEMANAGER_top(StateManager *statemanager){
    return statemanager -> stack[statemanager ->top];
}

int STATEMANAGER_update(StateManager *statemanager, float deltatime) {
  State *state = STATEMANAGER_top(statemanager);
  if (state -> update != NULL) return state -> update(deltatime);
  return 1;
}

int STATEMANAGER_draw(StateManager *statemanager, float deltatime) {
  State *state = STATEMANAGER_top(statemanager);
  if (state -> draw != NULL) return state -> draw(deltatime);
  return 1;
}


// create three base states that are automaticaly loaded into the stack


// create a function that takes a python object and create a state struct for it, and then push it onto the stack
// create a that allow a state to be pushed to a specific spot on the stack
int STATEMANAGER_pushtobottom(StateManager *statemanager, State* state){

    // calculate the bottom index
    int bottomindex;

    if(statemanager -> top + 1 == statemanager -> capacity) STATEMANAGER_scale(statemanager);
    statemanager -> top++;
    statemanager -> stack[bottomindex] = state;
    if (state -> init != NULL) state ->init;
    return bottomindex;
}

// create a function that pushs a state already on the stack to the top of the stack

int STATEMANAGER_swapstates(StateManager *statemanager, State* state){
    
    //



    if(state == STATEMANAGER_top(statemanager)) return 0;

    // get the top state with the STATEMANAGER_top function

    // create two temp states and do not pushthem to the stack
    //ie
    //State tempstate1 = topstate
    //State tempstate2 = state

    // use indexs to sitch states
    // ie
    //state = tempsate1
    //topstate = tempstate2

    return 0;
}










// functions for states

// take python object and do stuff i guess
int stateInit();

// takes python object and calls destroy function
int stateDestroy();

// takes python object and calls draw function
int stateDraw();

// create wrapper functions for state manager

static PyObject* STATEMANAGER_init(PyObject* self, PyObject* args){

}


