#Ryan R, Financial calculator Python

def info(income, amount, type):
   pertype = amount/income*100
   print(f"You send ${amount:.2f} on {type} and that is {pertype:.2f}% of your income")

def minc

print("Welcome to the Budget Caculator.")
income = float( input("What is your Monthly Income?\n:"))
rent = float(input("What do you pay in rent per month?:\n"))
utilities = float(input("What do you pay in utilities per month?:\n"))
groceries = float(input("What do you pay in groceries per month?:\n"))
transportation = float(input("What do you pay in transportation per month?:\n"))
savings = income*.1
print(f"You should save 10% or, ${round(savings, 2)} dollars a month")
info(income, rent, "rent")
info(income, utilities, "utilities")
info(income, groceries, "groceries")
info(income, transportation, "transportation")

print(f"This means you have ${round(spen, 2)} to spend.")
spen_ver = (spen/income)*100
print(f"This equates to {round(spen_ver , 2)}% a month.")
