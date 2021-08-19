#include<stdio.h>
#include<stdlib.h>

struct test{
    int num;
    int num2;
};

int main(){
    printf("hello wolrd \n");
    test w;
    w.num = 12;
    w.num2 = 13;

    printf("%i", w.num2);
}
