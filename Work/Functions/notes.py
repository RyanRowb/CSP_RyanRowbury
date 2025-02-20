#Ryan R, Function Notes

#funcotions are stored in key words


#def add():
    #numone = int(input("Give me a number:\n"),20)
    #numtwo = int(input("Give me another number:\n"),20)
    #print(numone+numtwo)

#add()

def user():
    return int(input("Tell me a word"))


name = user("name")
verb = user("verb")
place = user("place")
print(f"{name} was {verb} and somehow got to {place}.")