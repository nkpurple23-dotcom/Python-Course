print("===Welcome to Library Visit Planner===")
day=input("What day is it? ")
weather=input("What's the weather(sunny/cloudy/rainy)? ")
due=input("Are any of your books due?(yes/no) ")
if day.lower()=="monday" or day.lower()=="tuesday" or day.lower()=="wednesday" or day.lower()=="thursday" or day.lower()=="friday":
    day="Weekday"
elif day.lower()=="saturday" or day.lower()=="sunday":
    day="Weekend"
else:
    day=input("Please enter a day: ")
if weather=="sunny" and due=="yes":
    print("Final Summary: Please return your book.")
elif weather=="rainy" or weather=="cloudy":
    print("Final Summary: Make sure to bring an umbrella!")
elif not due=="yes":
    print("Final Summary: You have no books to return.")