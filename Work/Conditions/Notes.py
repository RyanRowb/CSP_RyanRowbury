#Ryan R, Conditional Notes

#print("Hello, welcome to my program that will sort you into a category.")
#name = input("What is your name:\n") .strip().lower().capitalize()

#if name == "Ryan":
#    print("Oh your the programer, why are you here get back to coding.")
#else:
#    print("Welcome to my program.")

#num = int (input("How many items did you buy?\n ").strip())

#if num == 1:
#    print("Listen I understand man. The socieoeconmic problems caused by the US government is so substation")
#elif num <= 3: 
#    print("GET OUT")
#elif num <= 5:
#    print("I told you to GET OUT")
#else:
#    print("You are banned from this store") 

#name = input("What is your name?\n").strip().lower()

#if "a" in name or "e" in name or "i" in name or "o" in name or "u" in name:
#    print("Your name has vowel!")
#else:
#    print("Your name doesn't have a vowel.")


num = int(input("Give me a random number between 1 and 10\n"))

if num > 5 and num < 10:
    if num == 7:
        print("That is an unluck number")
    else:
        print("that is a large single digit.")
else:
    print("Haha you loose the game")