//Ryan Rowbury, Silly Sentances
#include <stdio.h>
#include <strings.h>
//strng variables for my user inputs (minimum of 3)
char name[20];
char adj[20];
char verb[20];
char buy[20];
char sentance[6] = "When ";
char sentpart2[13] = " went to the ";
char sentpart3[14] = " Store, they ";
char sentpart4[27] = " to it and bought lots of ";

int main(void){
    //create user inputs (print statments with questions and scaf to collect the info)
    printf("Wellcome to the Silly Sentance Maker. Please answer all questoins\n");
    printf("Give me a random Name\n");
    scanf("%s", name);
    printf("Give me a random Adjective\n");
    scanf("%s", adj);
    printf("Give me a random Verb\n");
    scanf("%s", verb);
    printf("Give me a thing you would buy\n");
    scanf("%s", buy);
    printf("When", name, "went to the ", adj, "Store, they", verb, "to it and bough lots of", buy);
    return(0);
}