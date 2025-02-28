#Ryan R, Time Greeter

import time
curent =time.time()
local_time = time.localtime(curent)
hour = local_time.tm_hour

name = input("What is your name?\n").strip().lower().capitalize()
if (6 < hour < 11):
    print(f"Good Morning {name}")
elif (hour < 14):
    print("Good Afternoon {name}")
elif (hour <20):
    print("Good Night {name}, sleep tight, don't let the bed bugs bite")
elif (hour<6) or (hour > 24):
    print("GO TO BED {name}")
else:
    print("You are beyond time itself")