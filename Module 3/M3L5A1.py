from random import randint
num=randint(0,10)
running=True
print("---Welcome to the Number Game---")
while running:
    guess=int(input("Guess my number from 0-10: "))
    if guess<0 or guess>10:
        print("Invalid number")
        continue
    elif num==guess:
        print("That's correct!")
        running=False
    else:
        print("That's incorrect")
        continue
print("---Thank you for playing the Number Game---")