def total_calc(bill_amount, tip_perc):
    tip=(tip_perc/100)*bill_amount
    total=bill_amount+tip
    round(total,2)
    return total
final=total_calc(150,20)
print(f"Final bill amount: ${final}")