temp=int(input("What's today's temperature? "))
if temp<=50:
    print("You should wear a coat,a hat, gloves, and a scarf.")
    clothing="Coat,a hat, gloves, and a scarf."
elif temp>50:
    print("You should wear sunglasses and sunscreen.")
    clothing="Coat,a hat, gloves, and a scarf."
else:
    temp=input("Please enter a valid number")
rain=input("Is it raining today?(yes or no) ")
if rain.lower()=="yes":
    print("You need a umbrella.")
elif rain.lower()=="no":
    print("You don't need an umbrella.")
else:
    print("Please enter yes or no.")
windbreaker=int(input("What's the speed of the wind(mph)? "))
if windbreaker<=10:
    print("You don't need a windbreaker.")
    wind="No"
elif windbreaker>10:
    print("You need a windbreaker.")
    wind="Yes"
else:
    print("Please type a valid number.")
print("Check complete")
print(f"""**********WEATHER OUTFIT PICKER**********
      Temperature: {temp}
      Outfit Chosen: {clothing}
      Raining: {rain}
      Windbreaker Needed: {wind}
      ********************************************""")