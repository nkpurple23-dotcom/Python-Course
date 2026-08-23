def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    try:
        a/b
        return a/b
    except ZeroDivisionError:
        print("Cannot divide by 0")
print("---Welcome to The Calculator---")
while True:
    op=int(input("1. Add  2. Subtract  3. Multiply  4. Division\n"))
    if op!=1 and op!=2 and op!=3 and op!=4:
        print("Please type a valid number")
        continue
    else:
        break
while True:
    if op==2:
        try:
            num1=float(input("Please enter the mineund: "))
            num2=float(input("Please enter the subtrahend: "))
        except ValueError:
            print("Not a number")
            continue
        print("Output:",subtract(num1,num2))
        break
    elif op==4:
        try:
            num1=float(input("Please enter the dividend: "))
            num2=float(input("Please enter the divisor: "))
        except ValueError:
            print("Not a number")
            continue
        print("Output:",division(num1,num2))
        break
    else:
        try:
            num1=float(input("Please enter a number: "))
            num2=float(input("Please enter a number: "))
        except ValueError:
            print("Not a number")
            continue
        if op==1:
            print("Output:",add(num1,num2))
            break
        if op==3:
            print("Output:",multiply(num1,num2))
            break