print("---Welcome to the Grocery Billing Program---")
low_price=0
medium_price=0
high_price=0
customers_served=0
total_sales=0
random=True
item=1
customer_total=0
while random:
    flower=True
    name=input("What's your name? ")
    num=int(input("How many items are you going to buy? "))
    if num<=0:
        print("Please enter a valid number")
        continue
    while item<=num:
        item_name=input("Enter item name: ")
        price=int(input("Enter item price: "))
        amount=int(input("Enter quantity: "))
        if price<=0 or amount<=0:
            print("Invalid price or quantity. Please enter again.")
            continue
        total=price*amount
        customer_total+=total
        if price<=50:
            low_price+=amount
        elif price<=100:
            medium_price+=amount
        else:
            high_price+=amount
        item+=1
    customers_served+=1
    total_sales+=customer_total
    print(f"Total bill for {name}: {customer_total}")
    while flower:
        next=input("Is there another customer? (yes/no): ").lower()
        if next=="no":
            random = False
            flower=False
        elif next=="yes":
            flower=False
        else:
            continue
print("=== Grocery Category Report ===")
if low_price>0:
     print(f"Low price items: {low_price}")
if medium_price>0:
    print(f"Medium price items: {medium_price}")
if high_price>0:
    print(f"High price items: {high_price}")
print(f"""Customers served: {customers_served}
Total sales: {total_sales}
Thank you for using the Grocery Billing Program""")