#Ryan R, Name Decorator

name = input("What is your first name?\n").lower().strip().capitalize()
print(f"Hello {name}, welcome to the name decorator.")
decor = input("How would you like to decorate your name? (Just type the number) \n1. xXNameXx\n2. (:(: Name :) :)\n3. !?Name!?\n Number:") .strip()

dec1 = "xX"
dec2 = "Xx"
dec3 = "(:(:"
dec4 = ":):)"
dec5 = "!?"
if(decor == "1"): print(dec1+name+dec2)
if(decor == "2"): print(dec3+name+dec4)
if(decor == "3"): print(dec5+name+dec5)
