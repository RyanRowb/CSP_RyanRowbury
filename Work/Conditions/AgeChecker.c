//Ryan Rowbury, Age Checker
#include <stdio.h>
int age;

int main(void){
    printf("What is your age (Number Form)\n");
    scanf("%d", &age);
    if(age < 5){printf("You are not eligible for anything on this progam.");
    }else if (age < 15){
        printf("You can go to school");
        }else if (age < 16){
        printf("You can get a learners permit");
        }else if (age < 18){
        printf("You can drive (assuming you have a licence)");
        }else{
    printf("You can vote in the USA!");
    }
}