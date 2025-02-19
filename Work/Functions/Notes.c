//Ryan Rowbury, Functions notes


#include <stdio.h>

char input(char type[20]){
    char answer[50];
    printf("Please give me a %s; \n", type);
    scanf("%s", answer);
    return answer;
}
int main(void){
    return(0);
}