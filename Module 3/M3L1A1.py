def greet_customer():
    name=input("Hello! What's your name? ")
    return name
name=greet_customer()
price=0.50
cups=int(input("How many cups do you want? "))
def calculate_total(a,b):
    total=a*b
    return total
total=calculate_total(price,cups)
new=round(total, 2)
mone=float(input("How much money do you have? "))
def calculate_change(a,b):
    change=b-a
    return change
change=calculate_change(total,mone)
def thank_you_message():
    print(f"Thank you {name} for stopping by the stand")
print(f"""---Lemonade Stand Receipt---
Price per cup: ${price}
Cups sold: {cups}
Total cost: ${new}
Amount paid: ${mone}
Change due: ${change}""")
thank_you_message()