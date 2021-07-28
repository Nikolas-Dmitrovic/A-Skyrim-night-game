#include "statemanager.h" 
#include<stdio.h>
#include<stdlib.h>
#include "pythondevfiles/include/python.h"

// TODO implement state index in stack 
//also implent int onstack check to see if it is on the stack(defult value of zero on build means it is not on the stack, when value is 1 it means it is on the stack)


unsigned returnNum(){
    return 1;
}

State buildC(FnPrt init, FnPrt update, FnPrt draw, FnPrt destroy){
    State name1;
    name1.init = init;
    name1.update = update;
    name1.draw = draw;
    name1.destroy = destroy;
    name1.onStack = 0;

    return name1;
}

void rebuildC(State state1, FnPrt init, FnPrt update, FnPrt draw, FnPrt destroy){
    state1 = buildC(init,update,draw,destroy);
}

int STATEMANAGER_initC(StateManager *statemanager) {
  statemanager -> capacity = 3;
  statemanager -> stack = malloc(statemanager -> capacity * sizeof(State*));
  statemanager -> top = -1;
  return 0;
}

int STATEMANAGER_freeC(StateManager *statemanager) {
  do {
    STATEMANAGER_pop(statemanager);
  } while (statemanager -> top > -1);
  free(statemanager -> stack);
  return 0;
}

int STATEMANAGER_scaleC(StateManager *statemanager){
    statemanager -> capacity *= 2;
    statemanager -> stack = realloc(statemanager ->stack, statemanager-> capacity * sizeof(State*));
    return statemanager -> capacity;
}

int STATEMANAGER_pushC(StateManager *statemanager, State *state){
    if(statemanager -> top + 1 == statemanager -> capacity) STATEMANAGER_scaleC(statemanager);
    statemanager -> top++;
    statemanager -> stack[statemanager ->top] = state;
    state ->onStack = 1;
    if (state -> init != NULL) state ->init;
    return statemanager->top;

}

int STATEMANAGER_popC(StateManager *statemanager){

    if(statemanager -> top == -1) return 0;
    State *top = STATEMANAGER_topC(statemanager);
    if(top -> destroy != NULL) top -> destroy();
    statemanager -> stack[statemanager -> top] = NULL;
    statemanager -> top--;
    return statemanager -> top;
}

State *STATEMANAGER_topC(StateManager *statemanager){
    return statemanager -> stack[statemanager ->top];
}

int STATEMANAGER_updateC(StateManager *statemanager, float deltatime) {
  State *state = STATEMANAGER_topC(statemanager);
  if (state -> update != NULL) return state -> update(deltatime);
  return 1;
}

int STATEMANAGER_drawC(StateManager *statemanager, float deltatime) {
  State *state = STATEMANAGER_topC(statemanager);
  if (state -> draw != NULL) return state -> draw(deltatime);
  return 1;
}


// create three base states that are automaticaly loaded into the stack
// base states should be used for temp reasons like pause menus


// create a function that takes a python object and create a state struct for it, and then push it onto the stack
// create a that allow a state to be pushed to a specific spot on the stack
int STATEMANAGER_pushtobottomC(StateManager *statemanager, State* state){
    if(state->onStack == 0) return 0;

    int bottomindex = 0;

    if(statemanager -> top + 1 == statemanager -> capacity) STATEMANAGER_scaleC(statemanager);
    statemanager -> top++;
    statemanager -> stack[bottomindex] = state;
    if (state -> init != NULL) state ->init;
    return bottomindex;
}

int STATEMANAGER_movetobottomC(StateManager *statemanager, State* state){
    if(state->onStack == 1) return 0;
    int bottomindex = 0;

    if(statemanager -> top + 1 == statemanager -> capacity) STATEMANAGER_scale(statemanager);
    statemanager -> top++;
    statemanager -> stack[bottomindex] = state;
    if (state -> init != NULL) state ->init;
    return bottomindex;

}

int STATEMANAGER_movetotopC(StateManager *statemanager, State* state){
    if(state->onStack == 1) return 0;
    if(statemanager -> top + 1 == statemanager -> capacity) STATEMANAGER_scale(statemanager);
    
    statemanager -> stack[statemanager -> top] = state;
    if (state -> init != NULL) state ->init;
    return statemanager -> top;

}

int STATEMANAGER_movetoposC(StateManager *statemanager, State* state, int indexpos){
    if(state->onStack == 1) return 0;

    if(statemanager -> top + 1 == statemanager -> capacity) STATEMANAGER_scale(statemanager);
    statemanager -> stack[indexpos] = state;
    if (state -> init != NULL) state ->init;
    return indexpos;
}

// create a function that pushs a state already on the stack to the top of the stack
// fix this shit lmao
int STATEMANAGER_swapstatesC(StateManager *statemanager, State* state){
    
    //figure out how to check if a state is on the stack
    if(state->onStack == 1) return 0;



    if(state == STATEMANAGER_topC(statemanager)) return 0;

    // get the top state with the STATEMANAGER_top function
    State top = *STATEMANAGER_topC(statemanager);

    // create two temp states and do not pushthem to the stack
    //ie
    State tempstate1 = top;
    State tempstate2 = state;

    // use indexs to switch states
    // ie

    state = tempstate1;
    top = tempstate2;

}


// create a function that can parse json files and make states
// do this in c or python
// python would be easyer to write it in

// create simple test funtions


// create a function that can convert a stuct into a python object and vise versa





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

static PyObject* STATEMANAGER_free(PyObject *self, PyObject* args){

}

static PyObject* STATEMANAGER_push(PyObject *self, PyObject* args){

}

static PyObject* STATEMANAGER_pop(PyObject *self, PyObject* args){

}

static PyObject* STATEMANAGER_scale(PyObject *self, PyObject* args){

}

static PyObject* STATEMANAGER_top(PyObject *self, PyObject* args){

}

static PyObject* STATEMANAGER_update(PyObject *self, PyObject* args){

}

static PyObject* STATEMANAGER_draw(PyObject *self, PyObject* args){

}

static PyObject* STATEMANAGER_pushtobottom(PyObject *self, PyObject* args){

}

static PyObject* STATEMANAGER_movetobottom(PyObject *self, PyObject* args){

}

static PyObject* STATEMANAGER_movetotop(PyObject *self, PyObject* args){

}

static PyObject* STATEMANAGER_movetopos(PyObject *self, PyObject* args){

}

static PyObject* STATEMANAGER_swapstates(PyObject *self, PyObject* args){

}
