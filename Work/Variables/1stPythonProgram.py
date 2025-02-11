# Ryan Rowbury, First Python Program

lifename = input("please tell me you name: ")
print(lifename+ ", welcome to my Game.")
print("**GAME IS UNIFINISHED**")
q_var = input("Run Game? (Y or N)\n") .upper()
if(q_var == "N") :print("Okay, stopping Program")
if(q_var == "Y") :pname = input("What is your Character's name?\n")
g_var = input(f"Where would you like to start {pname},\n1. A tavern in a town \n2. The Enchanted Forest \n3. The Mountains of Halcion? ")

if(g_var == "1"): print(f"\nYou awake in a bed at the local tavern.")
if(g_var == "2"): print("\nYou find yourself in the Magical Forest. You don't know how you got here, but its warm glow and fresh smell make you want to stay.")
if(g_var == "3"): print("\nYou find yourself in the High Mountains of Halcion, it is cold and very harsh. Your failing camp fire won't do good against this lasting cold.")
print("What do you do?\n")
if(g_var == "1"): tav_var = input("1. Leave Room\n2. Look around room\n3. Sleep Longer\n")
if(g_var == "2"): for_var = input("1. Leave Forest\n2. Look around Forest\n3. Find what is giving off that warm glow\n")
if(g_var == "3"): mou_var = input("1. Try to climb down the mountain\n2. Try to restart the Campfire\n Look for something like a cave\n")

if(tav_var == "1"): print("You leave the safe room and enter the empty tavern. Your door slams behind you.")
if(tav_var == "2"): print("You see nothing")
if(tav_var == "3"): print ("You sleep longer and awake in a fire.\n\n GAME OVER\n\n\n\n")