print("Welcome")
vec=input("Choose your vehicle: 1. Bike  2. Car\n")
if vec=="1":
    bick=input("Choose your bike type: 1. Scooty  2. Mountain bike\n")
    if bick=="1":
        speed="80 km/h"
        best="Roads"
        bick="Scooty"
    elif bick=="2":
        speed="40 km/h"
        best="Mountains"
        bick="Mountain bike"
    else:
        bick=input("Please enter 1 or 2: ")
elif vec=="2":
    bick=input("Choose your car type: 1. SUV  2. Sedan")
    if bick=="1":
            speed="100 km/h"
            best="City roads"
            bick="SUV"
    elif bick=="2":
            speed="120 km/h"
            best="Mountain roads"
            bick="Sedan"
    else:
            bick=input("Please enter 1 or 2: ")
else:
    vec=input("Please enter 1 or 2: ")
print(f"""You picked: {bick}
Top speed: {speed}
Best for: {best}""")
print("Goodbye")