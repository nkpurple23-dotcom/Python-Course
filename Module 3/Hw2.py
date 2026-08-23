def calculate_change(paid, price):
    new=paid-price
    return new
ticket_price=30
print(f"""---Welcome to The Parking Ticket Payment Helper---
We accept 1, 5, 10, and 25 cent coins""")
total_inserted=0 
coins_inserted=0
while True:
    insert=int(input("Please insert your coins: "))
    if insert!=1 and insert!=5 and insert!=10 and insert!=25:
        print("Invalid coin value")
        continue
    total_inserted+=insert
    coins_inserted+=1
    if total_inserted>=ticket_price:
        print("Enough coins inserted")
        break
change=calculate_change(total_inserted, ticket_price)
print(f"""---Payment Summary---
Ticket price: {ticket_price}
Coins inserted: {coins_inserted}
Total paid: {total_inserted}
Change due: {change}
---Thank you for using The Parking Ticket Payment Helper---""")