//Ryan Rowbury, Time Checker
#include <stdio.h>
#include <time.h>

int main(void){
    time_t seconds;

    seconds = time(NULL);
    printf("It has been %d seconds since January 1, 1970", seconds);

    time_t rawtime;
    struct tm * timeinfo;

    time(&rawtime);
    timeinfo = localtime(&rawtime);
    printf("\nCurrent time and date is %s", asctime(timeinfo));
    
    time_t now = time(NULL);
    struct tm *tm_truckt = localtime(&now);
    int hour = tm_truckt->tm_hour;
    printf("%d\n", hour);
    return(0);
}