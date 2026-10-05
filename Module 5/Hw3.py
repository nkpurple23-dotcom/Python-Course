class Vehicle:
    def __init__(self,brand,max_speed):
        self.brand=brand
        self.max_speed=max_speed
    def show_details(self):
        print("Brand",self.brand)
        print("Max Speed",self.max_speed,"mph")
class Car(Vehicle):
    def __init__(self,model,brand,max_speed,seats):
        self.model=model
        self.seats=seats
        super().__init__(brand,max_speed)
    def show_details(self):
        print("Car model",self.model)
        print("Seats:",self.seats)
        super().show_details()
    def fuel_type(self,fuel):
        self.fuel=fuel
        print("Fuel:",fuel)
obj=Car("SUV","Jeep",180,5)
obj.show_details()
obj.fuel_type("Diesal")
print("Car is a subclass of Vehicle:",issubclass(Car,Vehicle))