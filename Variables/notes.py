# Ryan Rowbury, Variables Notes

name = input("please tell me you name: ")
print(name+ ", welcome to my Game.")
print("**GAME IS UNIFINISHED**")
q_var=input("Run Game? (Y or N):")
if(q_var == "N") :print("Okay, stopping Program")
if(q_var == "Y") :g_var = input("Where would you like to start,\n1. A tavern in a town \n2. The Enchanted Forest \n3. The Mountains of Halcion? ")

if(g_var == "1"): print("\nYou awake in a bed at the local tavern.")
if(g_var == "2"): print("\nYou find yourself in the Magical Forest. You don't know how you got here, but its warm glow and fresh smell make you want to stay.")
if(g_var == "3"): print("\nYou find yourself in the High Mountains of Halcion, it is cold and very harsh. Your failing camp fire won't do good against this lasting cold.")
print("\nWhat do you do?")
if(g_var == "1"): print("1. Leave Room\n2. Look around room\n3. Sleep Longer")