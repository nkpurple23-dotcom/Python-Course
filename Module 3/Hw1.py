def greet_customer():
    print("---Welcome to the Art Supplies Store---")
greet_customer()
price=float(input("What's the price per item? "))
num=int(input("How many items "))
def calculate_total(price, num):
    new=price*num
    return new
new=round(calculate_total(price, num), 2)
pay=round(float(input("Please pay: ")), 2)
def calculate_change(paid, new):
    change=paid-new
    return change
change=calculate_change(pay,new)
def thank_you(items):
    if num>5:
        print("Thank you for buying so many items")
    else:
        print("Please come back next time!")
thank_you(num)
print(f"""---Purchase Summary---

Price per item: ${price}
Number of items bought: {num}
Total cost: ${new}
Amount paid: ${pay}
Change due: ${change}

---Thank you for purchasing at the Art Supplies Store---""")