//Ryan Rowbury, Time Greeter
#include <stdio.h>
#include <time.h>
int hour;

int main(void){
time_t now = time(NULL);
    struct tm *tm_truckt = localtime(&now);
    int hour = tm_truckt->tm_hour;

    if (hour < 11){
        printf("Good morning");
    }else if(hour < 17){
        printf("Good afternoon");
    }else if (hour < 22){
        printf("Good evening");
    }else if (hour < 6){
        printf("Welcome to the AM my G bro");
    }else if (hour > 22){
        printf("Go to be lil bro");
    }else{
        printf("You are outside the boundries of time, so good luck");
    }
}