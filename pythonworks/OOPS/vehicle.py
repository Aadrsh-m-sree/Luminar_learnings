class Car:
    name : str
    brand : str
    fuel_type : str

    def __init__(self,name,brand,fuel):
        self.name,self.brand, self.fuel_type=name,brand,fuel
    
    def display(self):
        print(f"Name : {self.name}")
        print(f"Brand : {self.brand}")
        print(f"Fuel type : {self.fuel_type}")
    
    def __str__(self): # string representation of object
        return self.name

car_instance1=Car("Nexon","TATA","Petrol")
car_instance1.display()
print(car_instance1)