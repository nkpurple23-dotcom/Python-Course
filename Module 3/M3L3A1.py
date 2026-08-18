def calculate_change(paid, price):
    return paid-price
snack_price=100
running_total=0
print(f"""---Welcome to Snack Vending Machine---
Price per snack: {snack_price}
We accept 1, 5, 10, 25 cent coins.""")
while True:
    money=int(input("Please insert your coins one at a time: "))
    if money!=1 and money!=5 and money!=10 and money!=25:
        continue
    running_total+=money
    print(f"{running_total} cents has been inserted")
    if running_total>=snack_price:
        break
change=calculate_change(running_total,snack_price)
print(f"""---Purchase Summary---
Snack Price: ¢{snack_price}
Money Inserted: ¢{running_total}
Change: ¢{change}
""")