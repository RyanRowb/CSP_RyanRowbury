#Ryan R, Financial calculator Python

def info(income, amount, type):
   pertype = amount/income*100
   print(f"You send ${amount:.2f} on {type} and that is {pertype:.2f}% of your income")

def expen(type):
   return float(input(f"What is your {type} per month\n"))

print("Welcome to the Budget Caculator.")
income = expen("income")
rent = expen("rent")
utilities = expen("utilities")
groceries = expen("groceries")
transportation = expen("transportation")
savings = (income/10)

print(f"You should save 10% or, ${savings:.2f} dollars a month")
info(income, rent, "rent")
info(income, utilities, "utilities")
info(income, groceries, "groceries")
info(income, transportation, "transportation")

spen = income - rent - utilities - groceries - transportation - savings
print(f"This means you have ${round(spen, 2)} to spend if you don't want to save more.")
spen_ver = (spen/income)*100
print(f"This equates to {round(spen_ver , 2)}% a month.")
