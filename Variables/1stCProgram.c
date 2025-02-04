//Ryan Rowbury, 1stCProgram
#include <stdio.h>
int greet;

int main(void){
    printf("What is your favorite Number?\n");
    scanf("%d", &greet);
    printf("%d", greet);
    printf(", Thats a good number!");
    return 0;
}