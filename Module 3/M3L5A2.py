from random import randint
print("---Welcome to Rock, Paper, Scissors---")
while True:
    user=input("Please choose rock, papper, or scissors: ").lower()
    if user!="rock" and user!="paper" and user!="scissors":
        print("Invalid choice")
        continue
    com=randint(1,3)
    if com==1:
        com="rock"
    elif com==2:
        com="paper"
    else:
        com="scissors"
    print(f"Computer's choice: {com}\nPlayer's choice: {user}")
    if com==user:
        print("Tie")
    elif com=="rock" and user=="paper":
        print("Player wins!!!")
    elif com=="rock" and user=="scissors":
        print("Computer wins")
    elif com=="paper" and user=="rock":
        print("Computer wins")
    elif com=="paper" and user=="scissors":
        print("Player wins!!!")
    elif com=="scissors" and user=="rock":
        print("Player wins!!!")
    else:
        print("Computer wins")
    play=input("Do you want to play again (yes/no)? ").lower()
    if play=="no":
        break
print("---Thank you for playing Rock, Paper, Scissors---")