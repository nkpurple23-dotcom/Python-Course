# 1) Ask the user to enter a number and store it in `n`.
n=int(input("How many whole numbers do you want to add? "))
# 2) Set `sum` to 0.
sum=0
# 3) Use a `for` loop from 1 to `n` (inclusive):
for i in range(n):
    sum+=i
# 4) After adding, print the current value of `sum`.
print(sum)