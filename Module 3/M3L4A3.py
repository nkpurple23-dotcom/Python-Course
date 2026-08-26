valid=True
while valid:
    try:
        num=int(input("Enter a number: "))
        if num%2==0:
            while valid:
                print("bye")
        valid=False
    except ValueError:
        print("Valur error")