//Ryan Rowbury, Name Decorator
#include <stdio.h>
#include <string.h>


char name[20];
char dec1[20]= "xX";
char dec2[20]= "Xx";

int main(void){
    printf("Please tell me your first name\n");
    scanf("%s", name);
    strcat(dec1, name);
    strcat(dec1, dec2);
    printf("This is your Decorated name, %s", dec1);
    return(0);
}