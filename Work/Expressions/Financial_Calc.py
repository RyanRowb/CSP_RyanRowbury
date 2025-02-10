#Ryan R, Financial calculator Python

print("Welcome to the Budget Caculator.")
income = float( input("What is your Monthly Income?\n:"))
rent = float(input("What do you pay in rent per month?:\n"))
utilities = float(input("What do you pay in utilities per month?:\n"))
groceries = float(input("What do you pay in groceries per month?:\n"))
transportation = float(input("What do you pay in transportation per month?:\n"))
savings = income*.1
print(f"You should save 10% or, {round(savings, 2)} dollars a month")
rent_per = (rent/income)*100
uti_per = (utilities/income)*100
groc_per = (groceries/income)*100
tran_per = (groceries/income)*100
print(f"You currently spending ${rent} or {round(rent_per, 2)}% on rent.")
print(f"You currently spending ${utilities} or {round(uti_per, 2)}% on utilities.")
print(f"You currently spending ${groceries} or {round(groc_per, 2)}% on groceries.")
print(f"You currently spending ${transportation} or {round(tran_per, 2)}% on transportation.")
spen = income-(rent+utilities+groceries+transportation+savings)
print(f"You have ${round(spen, 2)} to spend.")
spen_ver = (spen/income)*100
print(f"This equates to {round(spen_ver , 2)}% a month.")