print("Welcome to Holiday Activity Planner")
choice=input("Choose one: 1. Beach Holiday  2. Mountain Holiday\n")
if choice=="1":
    type=input("Choose one: 1. Swimming  2. Sandcastle Building\n")
    if type=="1":
        print("""You picked: Swimming
        Best time: Morning
        Remember: Carry sunscreen and water""")
    elif type =="2":
        print("""You picked: Sandcastle Building
        Best time: Evening
        Remember: Carry sunscreen and water""")
    else:
        type=input("Please choose one of the valid options: 1. Swimming  2. Sandcastle Building\n")
elif choice=="2":
    