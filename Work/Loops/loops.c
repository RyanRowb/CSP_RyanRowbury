//Ryan Rowbury, Loops Notes
#include <stdio.h>
int x;
int i = 1;

int main(void){
for(x=0; x<10;x++){
    printf("Hello\n");
}
while(i<10){
    printf("%d\n", i);
    i++;
}
int grades[] = {97, 95, 100, 87, 70, 23, 64};
printf("%d\n", grades[5]);

grades[5] = 94;
printf("%d\n", grades[5]);
//this tells you bytes not number of data points
printf("%lu\n", sizeof(grades));
int length = sizeof(grades)/sizeof(grades[0]);
printf("%d\n", length);
int t;
for(t=0; t<=10; t+=2){
    printf("%d\n", t);
}
int l;
for(l=0; l<length; l++){
    printf("%d\n", grades[l]);
}

int interator= 100;
while (interator>= 0){
    printf("%d\n", interator);
    interator-= 10;
}

char movies[][20] = {"Reach", "The Prilgrims", "Credit Card Debt", "Up", "1984"};
int m = 0;
int mlength = sizeof(movies)/sizeof(movies[0]);
while(m<mlength){
    printf("%s\n", movies[m]);
    m++;
}
return(0);
}