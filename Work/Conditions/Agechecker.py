#Ryan R, Age Checker

print("Welcome to the Age checker")
age = int(input("What is your age?\n").strip())

if age < 6:
    print("You are not eligible for anything on this progam.")
elif age < 15:
    print("You can go to school")
elif age < 16:
    print("You can get a learners permit")
elif age < 18:
    print("You can drive (assuming you have a licence)")
else:
    print("You can vote in the USA!")