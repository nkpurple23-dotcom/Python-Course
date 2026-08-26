import random
import math
print("A random number:",random.randint(1,10))
act=["swimming", "sleeping", "eating"]
print("A random activity:",random.choice(act))
secret=random.randint(1,5)
while True:
    guess=int(input("Guess my secret number: "))
    if guess==secret:
        print("Correct! You got my secret number!")
        break
    else:
        print("That was incorrect. Please try again!")
        continue
deci=float(input("Please enter a number with a decimal: "))
print("Round down:",math.ceil(deci))
print("Round up:",math.floor(deci))
print("Copysign:",math.copysign(-1,5))
print("Absolute value of 10:",math.fabs(-10))
g1=int(input("Please enter your first number: "))
g2=int(input("Please enter your second number: "))
print("GCD:",math.gcd(g1,g2))