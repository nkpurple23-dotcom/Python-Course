def total_bill(bill_amount, tip_perc):
    tip=bill_amount*tip_perc
    total=tip+bill_amount
    print(f"Please pay: {total}")
    return
total_bill(150,20)
def seating_arrangements(guests):
    """This calculates the number of seating arrangements for guests"""
    if guests==0 or guests==1:
        return 1
    elif guests>1:
        return guests*seating_arrangements(guests-1)
    print(seating_arrangements.__doc__)
print("Seating arrangement for 1 guests:", seating_arrangements(1))
print("Seating arrangement for 2 guests:", seating_arrangements(2))
print("Seating arrangement for 3 guests:", seating_arrangements(3))
print("Seating arrangement for 5 guests:", seating_arrangements(5))