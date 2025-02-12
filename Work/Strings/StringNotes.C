//Ryan Rowbury, String Notes
#include <stdio.h>
#include <string.h>

char name[20];

int main(void){
    //printf("Please tell me your full name\n");
    //scanf("%s", name);
    //fgets(name, 20, stdin);
    //printf("Hello %s, welcome to my program", name);
    //char sentance[] = "\nThe quick brown fox jumps over the lazy dog";
    //printf("%d\n", strlen(sentance));
    char one[] = "Hello ";
    char two[] = "World!";
    char three[]= "This is my program ";
    strcat(three, two);
    printf("%s\n", three);
    return(0);
}