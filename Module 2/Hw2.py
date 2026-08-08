print("---Welcome to the Power Calculator---")
y=True
while y==True:
    num=int(input("Enter a number for the base: "))
    pow=int(input("Enter a number for the exponent: "))
    new=num**pow
    print(new)
    cal=input("Do you have another calculation (yes/no)? ")
    if cal.lower()=="no":
        y=False
print("---Thank you for using the Power Calculator---")