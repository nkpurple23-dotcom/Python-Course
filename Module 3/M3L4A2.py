try:
    first=int(input("Enter a number: "))
    second=int(input("Enter another number: "))
    first/second
except ZeroDivisionError:
    print("Zero division error")
except ValueError:
    print("Value error")
except SyntaxError:
    print("Syntax error")
except:
    print("Error detected")
else:
    print("No exceptions")
finally:
    print("This will happen no matter what")