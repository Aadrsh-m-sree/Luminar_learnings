class SuperHero:
    name : str
    suit : str

    def __init__(self,name,suit):
        self.name=name
        self.suit=suit
    
    def __str__(self):
        return self.name

    def display(self):
        print(f"Name : {self.name}")
        print(f"Suit : {self.suit}")

class SpiderMan(SuperHero):
    def __init__(self,name,suit):
        super().__init__(name,suit)
    
    def power(self):
        print(f"Power : Spider sense,Sticky hands")

class MinnalMurali(SuperHero):
    def __init__(self,name,suit):
        super().__init__(name,suit)
    
    def power(self):
        print(f"Power : Running,Reflex")

spiderman_instance1=SpiderMan("spiderman","spidersuit")
spiderman_instance1.display()
spiderman_instance1.power()
print(spiderman_instance1)
print()
minnalmurali_instance1=MinnalMurali("minnal murali","minnal murali suit")
minnalmurali_instance1.display()
minnalmurali_instance1.power()
print(minnalmurali_instance1)
