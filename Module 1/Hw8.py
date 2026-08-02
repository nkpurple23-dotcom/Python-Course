rice=12
milk=4
fruit=5
basket=5
family=5
basket_cost_per_person=(rice+milk+fruit)*basket/family
print(f"Grocery basket cost per person: {basket_cost_per_person}")
item=int(input("Enter the total number of items: "))
people=int(input("Enter the total number of people: "))
if item%people==0:
    print(f"{item} can be equally divided between {people}")
else:
    print(f"{item} can not be equally divided between {people}")
avg=45
wrong=30
correct=60
week=2
total=int(avg*week)
print(f"Grocery total: {total}")
corrected=int(total-wrong+correct)
print(f"Corrected grocery total: {corrected}")
corrected_avg=int(corrected/week)
print(f"Corrected weekly average: {corrected_avg}")
a=60
b=50
c=40
print(f"Store A average: {a}")
print(f"Store B average: {b}")
print(f"Store C average: {c}")
if corrected_avg<a and corrected_avg<b and corrected_avg<c:
    print("Your corrected grocery average is less than all three store averages")
elif corrected_avg>a and corrected_avg>b and corrected_avg>c:
    print("Your corrected grocery average is greater than all three store averages")
else:
    print("Your corrected grocery average is between the three store averages")