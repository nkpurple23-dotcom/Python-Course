print("Enter your scores in the 4 subjects (math, english, science, and hindi): ")
m=int(input("Math: "))
e=int(input("English: "))
s=int(input("Science: "))
h=int(input("Hindi: "))
total=m+e+s+h
print("Your total score is: ",total)
p=(total/400)*100
print(f"Score in percentage: {p}%")