#Ryan R, Timed Greeter

import time
#First instance of time in programming
#print(time.gmtime(0),"\n")

#Current time in second since gmtime
#print(time.time(),"\n")

#Current time were used to seeing
curent =time.time()
now = time.ctime(curent)
print(now)

#How to get just the hour
local_time = time.localtime(curent)
hour = local_time.tm_hour
min = local_time.tm_min
sec = local_time.tm_sec
print(f"{hour}:{min}:{sec}")