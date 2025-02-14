//Ryan Rowbury, Silly Sentances
#include <stdio.h>
#include <strings.h>
//strng variables for my user inputs (minimum of 3)
char name[20];
char adj[20];
char verb[20];
char buy[20];

int main(void){
    //create user inputs (print statments with questions and scaf to collect the info)
    printf("Wellcome to the Silly Sentance Maker. Please answer all questoins\n");
    printf("Give me a random Name\n");
    scanf("%s", name);
    printf("Give me a random Adjective\n");
    scanf("%s", adj);
    printf("Give me a random Action Verb\n");
    scanf("%s", verb);
    printf("Give me a thing you would buy\n");
    scanf("%s", buy);
    printf("When %s went to the %s Store, they %s to it and bough lots of $s", name, adj, verb, buy);
    return(0);
}