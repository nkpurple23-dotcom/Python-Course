# 1) Ask the user to enter a number (greater than 1) and store it in `n`.
n=int(input("Please enter a numb er greater than 1: "))
# 2) Print a message saying you will display numbers from `n` down to 1.
print(f"I will display the numbers from {n} to 1")
# 3) Use a `for` loop that starts from `n`, goes down to 1, and decreases by 1 each time.
for n in range(n,0,-1):
    print(n)
# 4) Inside the loop, print the current value of `i` (so numbers appear in reverse order).