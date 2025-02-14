//Ryan R, Financial Calculator

//Calculate savings as 10% of income (variable)

//How much spending money they have left (Income-everything eles)

//Caculate the perecent of rent (Variables)

//Caculate the perecent of utilities (Variables)

//Caculate the perecent of groceries (Variables)

//Caculate the perecent of transportation (Variables)

//Tell user category spedning amount and percent Ex. ("You spend $XX.XX of your monthly wage on rent.")

//percent and aount of spending money

#include <stdio.h>
#include <math.h>
float mon_inc;
float rent;
float util;
float groc;
float tran;
float savemon_inc;


int main(void){
    printf("Hello, welcome to the Financial Budget Caculator\n");
    printf("What is your Monthly Income?\n");
    scanf("%f", &mon_inc);
    printf("What is your Monthly Rent?\n");
    scanf("%f", &rent);
    printf("What is your Monthly Utility bill?\n");
    scanf("%f", &util);
    printf("What is your Monthly Grociery bill?\n");
    scanf("%f", &groc);
    printf("What is your Monthly Transportation bill?\n");
    scanf("%f", &tran);
    printf("You spend $%.2f on rent or %.2f percent of your monthly income on rent\n", rent, (rent/mon_inc));
    printf("You spend $%.2f on utilities or %.2f percent of your monthly income on utilities\n", util, (util/mon_inc));
    printf("You spend $%.2f on groceries or %.2f percent of your monthly income on groceries\n", groc, (groc/mon_inc));
    printf("You spend $%.2f on transportatoin or %.2f percent of your monthly income on transportation\n", tran, (tran/mon_inc));
    printf("You should also save 10 perecent of your income or $%2.f", (mon_inc* savemon_inc));
    printf("This leaves you with $%.2f to spend this month (If you don't want to save more).", (mon_inc - rent - groc - tran - util -(mon_inc * .1)));

}