try:
    num=int(input("Enter a number: "))
    print(f"The number you entered: {num}")
except ValueError as m:
    print(f"Exception: {m}")