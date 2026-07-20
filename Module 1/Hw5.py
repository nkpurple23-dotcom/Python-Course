temp=int(input("What's today's tempurature? "))
if temp<=20:
    activity="reading"
elif temp>20:
    activity="playing outside"
else:
    temp=int(input("Enter a valid number."))
rain=input("Is it raining(yes/no)? ")
if rain=="yes":
    rain="Make sure to use an umbrella if you go outside."
hw=int(input("How long have you been studying(just enter number in min)? "))
if hw>=30:
    hw="Take a break."
elif hw<30:
    hw="Keep studying."
else:
    hw=input(("Enter a number: "))
free=input("Do you have freetime(yes/no)? ")
if free=="yes":
    free="Do a hobby."
elif free=="no":
    free="Plan your day."
else:
    free=input("Please enter yes or no: ")
print(f"""---Final Summary---
    Temperature: {temp}
    Activity: {activity}
    Rain status: {rain}
    Study break status: {hw}
    Freetime: {free}
""")