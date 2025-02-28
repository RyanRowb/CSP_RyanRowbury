#Ryan R, Time Greeter

import time
curent =time.time()
local_time = time.localtime(curent)
hour = local_time.tm_hour

name = input("What is your name?")
if (6 < hour < 11):
    print("Good Morning")
elif (hour < 14):
    print("Good Afternoon")
elif (hour <20):
    print("Good Night, sleep tight, don't let the bed bugs bite")
elif (hour <6 )