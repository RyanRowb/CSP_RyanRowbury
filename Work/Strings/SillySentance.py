#Ryan R, Silly Sentances

name = input("What is your name?\n")  .strip() .lower() .capitalize()
print(f"Hello {name}, welcome to my program")
charcter = input("Give me a random character\n").strip() .lower() .capitalize()
action = input("Give me a random action (ending in ing)\n").strip() .lower()
color = input("Give me a random color\n").strip() .lower()
print(f"When {name} went to find the {charcter}, he found it by {action} and gave it a {color} flower.")