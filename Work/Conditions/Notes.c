//Ryan Rowbury, Notes Conditionals
#include <stdio.h>
#include <string.h>
char name[] = "Ryan";
int num = 8;

int main(void){
    if(strcmp(name, "Ryan") == 0){
        printf("Yo yo yo whats up my G");
    } else{
        printf("Wait a minute, Who are you?");
    };

    // != = not
    // || = or
    // && = and

    if(num > 5 && num < 10){
        printf("%d is a small digit number\n", num);
        }else if (num > 10){
        printf("%d is not a single digit number\n", num);
    }else{
        printf("%d is a small singe digit number \n", num);
    }
    return(0);
}