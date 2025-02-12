name = input("What is your first name?\n").lower().strip().capitalize()
print(f"Hello {name}, welcome to the name decorator.")
decor = input("How would you like to decorate your name? (Just type the number) \n1. xXNameXx\n2. (:(: Name :) :)\n3. !?Name!?\n Number:") .strip()

if(decor == "1"): print(f"Here is your decorated name, xX{name}Xx")
if(decor == "2"): print(f"Here is your decorated name, (:(: {name} :) :)")
if(decor == "3"): print(f"Here is your decorated name, !?{name}!?")
