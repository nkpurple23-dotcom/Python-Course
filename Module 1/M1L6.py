print("===Welcome to Smart School Day Planner===")
weather=input("What's the weather (rainy, sunny, cloudy)? ")
day=input("What day is it today? ")
hw=input("What's the status of your homework(complete or incomplete)? ")
print(f"====={day}======")
if day.lower()=="monday" or day.lower()=="tuesday" or day.lower()=="wednesday" or day.lower()=="thursday" or day.lower()=="friday":
    day="weekday"
elif day.lower()=="saturday" or day.lower()=="sunday":
    day="weekend"
else:
    day="not a valid day"
if weather=="sunny" and hw=="complete":
    m1="you can have fun at the beach!"
    h="complete"
elif weather=="cloudy" or weather=="rainy":
    m1="you should bring an umbrella"
elif not hw=="complete":
    h="finish your homework!!!"
print(f"""Day Type: {day}
Weather: {m1}
Homework status: {h}""")