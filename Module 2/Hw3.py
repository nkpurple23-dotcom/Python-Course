print("---Welcome to Homework Completion Tracker---")
total_homework=4
completed_task=0
task_num=1
while task_num<=total_homework:
    if task_num==1:
        task=input("Have you washed the dishes(yes/no)? ")
        if task.lower()=="yes":
            completed_task+=1
            task_num+=1
            print(f"Total tasks left: {total_homework-completed_task}")
    elif task_num==2:
        task=input("Have you vaccumed the floor(yes/no)? ")
        if task.lower()=="yes":
            completed_task+=1
            task_num+=1
            print(f"Total tasks left: {total_homework-completed_task}")
    elif task_num==3:
            task=input("Have you made your bed(yes/no)? ")
            if task.lower()=="yes":
                completed_task+=1
                task_num+=1
                print(f"Total tasks left: {total_homework-completed_task}")
    elif task_num==4:
            task=input("Have you cleaned your room(yes/no)? ")
            if task.lower()=="yes":
                completed_task+=1
                task_num+=1
                break
print(f"""Original task count: {total_homework}
Completed task count: {completed_task}
Remaining task count: {total_homework-completed_task}""")