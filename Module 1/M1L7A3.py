english=int(input("What did you get for English(scale of 1-100)? "))
math=int(input("What did you get for Math(scale of 1-100)? "))
history=int(input("What did you get for History(scale of 1-100)? "))
science=int(input("What did you get for English(scale of 1-100)? "))
music=int(input("What did you get for Music(scale of 1-100)? "))
avg=(english+math+history+science+music)/5
if 60<=avg<=100:
    print("You passed!")
elif avg<60:
    print("You failed.")
else:
    print("Please redo the program.")