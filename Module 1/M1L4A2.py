# 1) Take the total withdrawal amount as input from the user and store it in `Amount`.
amount=int(input("What's your total withdrawal amount? "))
# 2) Find how many 100-rupee notes are needed:
note_1=amount//100  
# 3) Find the remaining amount after taking out 100-rupee notes:
remaining100=amount%100 
# 4) From the remaining amount, find how many 50-rupee notes are needed:
note_2=remaining100//50 
# 5) Find the remaining amount after taking out 50-rupee notes:
remaining50=remaining100%50 
# 6) From the remaining amount, find how many 10-rupee notes are needed:
remaining10=remaining50//10  
# Divide the remainder by 10 (whole number division) and store it in `note_3`.
note_3=remaining50//10
# 7) Print the number of 100-rupee notes, 50-rupee notes, and 10-rupee notes.
print(f"Here's your total withdrawal amount: {amount}")
print(note_1, note_2, note_3)