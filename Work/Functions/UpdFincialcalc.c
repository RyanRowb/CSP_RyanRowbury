//Ryan R, Financial Calculator

#include <stdio.h>
#include <math.h>

int mon_inc;
int rent;
int util;
int groc;
int tran;

int user (char* type, int amount){
    printf("What is your %s per month\n", type);
    return scanf( "%d", amount);
}

int spend (char* type2, int charge, int income){
    char buffer[100];
    return sprintf(buffer, "You spend $%.2f on %s or %.2f percent of your monthly income on rent\n", charge, type2, (float)charge/income * 100);  
}

int main(void){
    printf("Hello, welcome to the Financial Budget Caculator\n");
    //printf("What is your Monthly Income?\n");
    //scanf("%f", &mon_inc);
    //printf("What is your Monthly Rent?\n");
    //scanf("%f", &rent);
    //printf("What is your Monthly Utility bill?\n");
    //scanf("%f", &util);
    //printf("What is your Monthly Grociery bill?\n");
    //scanf("%f", &groc);
    //printf("What is your Monthly Transportation bill?\n");
    //scanf("%f", &tran);
    user("Income", mon_inc);
    user("Rent", rent);
    user("Utilities", util);
    user("Grocieries", groc);
    user("Trasportation", tran);
    spend("Rent", rent, mon_inc);
    return 0;
    //printf("You spend $%.2f on rent or %.2f percent of your monthly income on rent\n", rent, (rent/mon_inc));
    //printf("You spend $%.2f on utilities or %.2f percent of your monthly income on utilities\n", //util, (util/mon_inc));
    //printf("You spend $%.2f on groceries or %.2f percent of your monthly income on groceries\n", groc, (groc/mon_inc));
    //printf("You spend $%.2f on transportatoin or %.2f percent of your monthly income on transportation\n", tran, (tran/mon_inc));
    //printf("You should also save at least 10 perecent of your income or $%2.f\n", (mon_inc* 0.1));
    //printf("This leaves you with $%.2f or %.2f percent of your monthly income to spend this month (If you don't want to save more).", (mon_inc - rent - groc - tran - util -(mon_inc * 0.1)), (((mon_inc - rent - groc - tran - util -(mon_inc * 0.1))/mon_inc)));

}