habit_info="eating",True,7,3
weekly_habits=1,1,1,1,1,1,1
len(weekly_habits)
weekly_habits[0]
weekly_habits[3]
weekly_habits[0:3]
weekly_habits[5:7]
weekly_habits+=1,
done=weekly_habits.count(1)
not_done=weekly_habits.count(0)
eat=0
not_eat=0
for day in weekly_habits:
    if day==1:
        eat+=1
    else:
        not_eat+=1
if eat>not_eat:
    print("You ate everyday")
else:
    print("You did not eat everyday")