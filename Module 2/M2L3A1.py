chore_num=1
total_chore=4
while chore_num<=total_chore:
    if chore_num==1:
        num1=input("Have you made your bed(yes/no)? ")
        if num1=="no":
            print("Please finish it then check again.")
        elif num1=="yes":
            chore_num+=1
    if chore_num==2:
            num1=input("Have you done the laundry(yes/no)? ")
            if num1=="no":
                print("Please finish it then check again.")
            elif num1=="yes":
                chore_num+=1
    if chore_num==3:
                num1=input("Have you washed the dishes(yes/no)? ")
                if num1=="no":
                    print("Please finish it then check again.")
                elif num1=="yes":
                    chore_num+=1
    if chore_num==4:
                num1=input("Have you done your homework(yes/no)? ")
                if num1=="no":
                    print("Please finish it then check again.")
                elif num1=="yes":
                    break
print("You have completed your chores!")