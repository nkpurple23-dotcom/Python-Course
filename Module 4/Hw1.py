emp=[]
marks=[12,68,84,99,43]
print(marks)
sample=[30,40,20]
sample*=2
len(marks)
marks[0]
marks[-1]
marks[0:3]
marks[::-1]
def match():
    count=[]
    for mark in marks:
        m=str(mark)
        if m[0]==m[-1]:
            count.append(m)
            m=int(mark)
    print("Matched marks:",count)
def add():
    count=0
    for m in marks:
        count+=m
    print("Total:",count)
    return count
match()
count=add()
avg=count/len(marks)
marks.sort()
print("Smallest number:", marks[0])
print("Largest number:", marks[-1])