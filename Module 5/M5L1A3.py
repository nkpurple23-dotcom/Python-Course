class Parrot:
    color="blue"
    def __init__(self,name,age):
        self.name=name
        self.age=age
name1=Parrot("Mily",4)
name2=Parrot("Brian",6)
print(f"Mily is {name1.color}.")
print(f"Brian is {name2.color}.")
print(f"{name1.name} is {name1.age} years old.")
print(f"{name2.name} is {name2.age} years old.")