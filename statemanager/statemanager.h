#ifndef ENGINE_STATEMANAGER_H
#define ENGINE_STATEMANAGER_H

//add c suffix to all functions written in to distigusih the diffrence between the python wrappers and c funcs

typedef unsigned int (*FnPrt)();
typedef unsigned int (*FnPrt)(float);


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
int STATEMANAGER_initC(StateManager *statemanager);
int STATEMANAGER_freeC(StateManager *statemanager);
int STATEMANAGER_pushC(StateManager *statemanager, State *state);
int STATEMANAGER_popC(StateManager *statemanager);
int STATEMANAGER_scaleC(Statemanager *statemanager);
State *STATEMANAGER_topC(StateManager *statemanager);
int STATEMANAGER_updateC(StateManager *statemanager, float deltatime);
int STATEMANAGER_drawC(StateManager *statemanager, float deltatime);
int STATEMANAGER_pushtobottomC(StateManager *statemanager, State* state);
int STATEMANAGER_movetobottomC(StateManager *statemanager, State* state);
int STATEMANAGER_movetotopC(StateManager *statemanager, State* state);
int STATEMANAGER_movetoposC(StateManager *statemanager, State* state, int indexpos);
int STATEMANAGER_swapstatesC(StateManager *statemanager, State* state);




// create a function that can make states like xxxx(struct name, func1, func two func three) insed of struct state statename; statename.func1 = fun1; statename.func2 = fun2;


#endif