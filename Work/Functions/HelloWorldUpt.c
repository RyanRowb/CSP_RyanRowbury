//Ryan Rowbury, Hello World Updated
#include <stdio.h>

char name1[]= "Jade Foster";
char name2[]= "Mara Ballard";
char name3[]= "Aidyn Ross";
char name4[]= "Samir Santiago";
char name5[]= "Isaac Cline";

void nameprinter(char* name){
    printf("Hello %s, and welcome to my program.\n", name);
}

int main(void){
    nameprinter(name1);
    nameprinter(name2);
    nameprinter(name3);
    nameprinter(name4);
    nameprinter(name5);
}