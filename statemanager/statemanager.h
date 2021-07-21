#ifndef ENGINE_STATEMANAGER_H
#define ENGINE_STATEMANAGER_H

typedef unsigned int (*FnPrt)();
// typedef unsigned int (*FnPrt)(float);


typedef struct{
    FnPrt init;
    FnPrt update;
    FnPrt draw;
    FnPrt destroy;
    int stackIndex;
    int onStack;


} State;

typedef struct{
    int capacity;
    State **stack;
    int top;
} StateManager;



// defines

// returns a state struct
State build(FnPrt init);

// rebuilds and changes the values of a State struct
void Statestruct_rebuild();


// inits the stack, sets the capacity, allocates memory, and indexs the top value

// destroys each state untill stack is empty
int STATEMANAGER_init(StateManager *statemanager);
int STATEMANAGER_free(StateManager *statemanager);
int STATEMANAGER_push(StateManager *statemanager, State *state);
int STATEMANAGER_pop(StateManager *statemanager);
int STATEMANAGER_scale(Statemanager *statemanager);
State *STATEMANAGER_top(StateManager *statemanager);
int STATEMANAGER_update(StateManager *statemanager, float deltatime);
int STATEMANAGER_draw(StateManager *statemanager, float deltatime);



// create a function that can make states like xxxx(struct name, func1, func two func three) insed of struct state statename; statename.func1 = fun1; statename.func2 = fun2;


#endif