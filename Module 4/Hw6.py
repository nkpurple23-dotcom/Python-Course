grades={"Alice":96,"Mary":65,"Hans":45,"Jane":86,"Kate":75}
total=0
for grade in grades.values():
    total+=grade
average=total/len(grades)
print(f"Average: {average:.1f}")
print("Person with highest grade",max(grades,key=grades.get))
print("Person with lowest grade",min(grades,key=grades.get))
person=input("Who do you want to lookup? ")
print(grades.get(person,"Not Found"))