from random import randint
secret=randint(1,50)
guess=1
hearts=5
print("---Welcome to Secret Number Guesser Game---")
while guess<=5 or secret==num:
    for i in range(hearts):
        num=int(input("Choose a number between 1-50: "))
        guess+=1
        if secret-num>=30 or num-secret>=30:
            print("🧊 ice cold") 
        elif secret-num>=20 or num-secret>=20:
            print("🥶 cold") 
        elif secret-num>=10 or num-secret>=10:
            print("🌡️ warm")
        elif secret-num>=5 or num-secret>=5:
            print("🔥 hot")
        elif secret==num:
            print("Correct!")
            break
print(f"The number was {secret}")