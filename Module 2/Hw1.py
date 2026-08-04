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
    type=input("Choose one: 1. Hiking  2. Camping\n")
    if type=="1":
        print("""You picked: Hiking
Best time: Morning/Evening
Remember: Carry sunscreen, water, and climbing gear""")
    elif type =="2":
            print("""You picked: Camping
Best time: Night
Remember: Bring tent and food""")
    else:
            type=input("Please choose one of the valid options: 1. Hiking  2. Camping\n")