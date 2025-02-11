name = input("What is your first name?\n").lower().strip().capitalize()
print(f"Hello {name}, welcome to the name decorator.")
decor = input("How would you like to decorate your name? (Just type the number) \n1. xX name Xx\n2. (:(: name :) :)\n3. !? name !?\n") .strip()

if(decor == "1"): print(f"xX{name}Xx")