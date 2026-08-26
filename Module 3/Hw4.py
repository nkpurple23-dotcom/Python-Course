valid=False
while not valid:
    try:
        bill=float(input("Please enter the bill amount: "))
        discount=float(input("Please enter discount percentage: "))
        people=int(input("How many people are there? "))
        if bill<=0 or discount<0 or people<0:
            print("Invalid value")
            continue
    except ValueError:
        print("Invalid value")
        continue
    try:
        dis=(bill*discount)/100
        total=bill-dis
        per=total/people
    except ZeroDivisionError:
        print("Zero division error")
        continue
    except ValueError:
        print("Value error")
        continue
    else:
        print(f"""---Shopping Discount Summary---
Bill amount: ${bill}
Discount percentage: {discount}%
Amount of people: {people}
Total amount: ${per}""")
        valid=True