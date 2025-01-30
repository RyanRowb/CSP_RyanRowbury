#include <stdio.h>

char nae3[]="Varibles here";
char name[]="Ryan R";
int num = 43;
float pi = 3.14;

char nae2[]="everything else below here";

int main(void){
    printf("Hello, my name is %s, my age is %d and my favorite number is %f");
    printf("%s\n", name);
    printf("%d\n", num);
    printf("%f\n", pi);
    return 0;
}