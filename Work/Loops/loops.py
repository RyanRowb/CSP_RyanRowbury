import random
#while x < 10:
    #print("Hello" , x)
    #x += 1

#nums = [3, 5, 7, 8, 9]
#for num in nums:
    #print(num)

#siblings = ["Adam", "Ethan", "Carmen", "Isaac", "Jason", "Jennifer", "Justin"]

#print one item
#print(siblings[3])
#change an item on list
#siblings[3] = "The best"
#print(siblings)
#remove an item from list
#siblings.pop(2)
#print(siblings)

#print("My family members are:")
#How to make it look good.
#for siblings in siblings:
#    print(siblings, "Rowbury")

#num = 1
#print("My family members are:")
#How to make it look good.
#for siblings in siblings:
#    print(f"{num}. {siblings}", "Rowbury")
#    num += 1

num = 1
rand = random.randint(1,20)
while num <21:
    if num == rand:
        print(f"Goose!")
        break
    else:
        print("Duck")
        num += 1