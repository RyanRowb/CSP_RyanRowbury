//Ryan Rowbury, My Family Loop
#include <stdio.h>
char family[][50]= {"Adam", "Ethan", "Carmen", "Isaac", "Jason", "Jennifer", "Justin"};
int x;

int main(void){
    for(x = 0; x < 7; x++){
    printf("Hello %s, welcome to my program.\n", family[x]);}
}