//Ryan Rowbury, 1stCProgram
#include <stdio.h>
//Intergers |int when we set the varible and 5d when we print
// Floats float when we set the varible and %f when we print
// strings (words) char wehn we set the variable and %s
int mynum;
int percent;

int main(void){
    printf("Type a number: \n");
    scanf("%d", &mynum);
    printf("You inputed\n2%d", mynum);
    printf("\nGive me a perecent as a decimal:\n");
    scanf("%f", &percent);
}