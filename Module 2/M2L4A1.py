#Step 1: Set up six counter variables (one per note value) plus counters for customers served and total dispensed, all starting at 0.
one=0
five=0
ten=0
twenty=0
fifty=0
hundred=0
served=0
dispensed=0
serving=True
#Step 2: Start an outer while loop that keeps serving customers until the flag variable serving becomes False.
while serving:
    idx=0
    name=input("What's your name? ")
    wit=int(input("What's your withdrawal amount? "))
    dispensed+=wit
    if wit<=0:
        print("Invalid amount")
        continue
    while idx<6:
        hundred=wit/100
        wit=wit%100
        fifty=wit/50
        wit=wit%50
        twenty=wit/20
        wit=wit%20
        ten=wit/10
        wit=wit%10
        five=wit/5
        wit=wit%5
        one=wit/1
        served+=1
        idx=7
    next=input("Is there another customer(yes/no)? ")
    if next=="no":
        serving=False

#Step 3: Ask for the customer's name and withdrawal amount; if the amount is invalid, print a message and continue back to the top of the loop.

#Step 4: Inside that same repeat, run an inner while loop that checks each of the six note values one at a time and works out how many of each note to dispense.

#Step 5: Update the matching counter variable for whichever note value was just dispensed, then ask if there is a next customer, setting serving to False if not.

#Step 6: Once the outer while loop ends, start an outer for loop stepping through each of the six note values to print the daily denomination report.

#Step 7: Inside that same repeat, run an inner for loop that prints one symbol for every note of that value dispensed across the whole day.