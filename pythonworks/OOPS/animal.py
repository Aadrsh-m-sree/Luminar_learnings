class Animal:
    name : str
    species : str

    def __init__(self,name,species):
        self.name=name
        self.species=species

    def __str__(self):
        return self.name

    def display(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")

class Lion(Animal):
    def __init__(self,name,species):
        super().__init__(name,species)
    
    def sound(self):
        print(f"Sound : Roar")

class Cat(Animal):
    def __init__(self,name,species):
        super().__init__(name,species)
        

    def sound(self):
        print(f"Sound : Meaw")

lion_instance1=Lion("Shibu","Panthera leo")
lion_instance1.display()
lion_instance1.sound()
print()
cat_instance1=Cat("Tom","Felis catus")
cat_instance1.display()
cat_instance1.sound()

