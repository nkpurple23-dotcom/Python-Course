b=1
rows=int(input("How many rows do you want? "))
for i in range(rows):
    for t in range(i+1):
        print(b, end="")
        b+=1
    print()