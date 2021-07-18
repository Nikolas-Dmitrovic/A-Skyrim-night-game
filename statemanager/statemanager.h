#ifndef ENGINE_STATEMANAGER_H
#define ENGINE_STATEMANAGER_H

typedef unsigned int (*FnPrt)();
typedef unsigned int (*FnPrt)(float);


typedef struct{
    FnPrt init;
    FnPrt update;
    FnPrt draw;
    FnPrt destroy


} State;

typedef struct{
    int capacity;
    struct State states[];
    int top;
} Stack;



// defines

#endif