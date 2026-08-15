print("---Star Pyramid Pattern---")
rows=int(input("How many rows do you want? "))
for i in range(rows):
    for t in range(i+1):
        print("*", end="")
    print()
print("---Floyd's Triangle")
b=1
rows=int(input("How many rows do you want? "))
for i in range(rows):
    for t in range(i+1):
        print(b, end="")
        b+=1
    print()
print("---Diamond Number Pattern---")
rows=int(input("How many rows do you want? "))
for i in range(rows):
    for t in range(rows-i-1):
        print(" ", end="")
    for y in range(2*i+1):
        print("*", end="")
    print()
for i in range(rows-2,-1,-1):
    for t in range(rows-i-1):
            print(" ", end="")
    for y in range(2*i+1):
            print("*", end="")
    print()