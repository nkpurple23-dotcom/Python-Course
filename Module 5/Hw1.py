class Pet:
    print("Hi")
pet_object=Pet()
class PetProfile:
    category="pet"
    def __init__(self,name,animal_type,age,favorite_food):
        self.name=name
        self.animal_type=animal_type
        self.age=age
        self.favorite_food=favorite_food
pet1=PetProfile("Greg","Dog",8,"Chicken")
pet2=PetProfile("Mary","Cat",6,"Fish")
print(f"""Greg is a {pet1.category}. 
Mary is also a {pet2.category}.
{pet1.name} is a {pet1.animal_type} and is {pet1.age} years old.
{pet1.name} likes eating {pet1.favorite_food}.
{pet2.name} is a {pet2.animal_type} and is {pet2.age} years old.
{pet2.name} likes eating {pet2.favorite_food}.""")