class Mobile:
    name:str
    price:int
    brand:str

    def __init__(self, name, price, brand):
        self.name, self.price, self.brand = name, price, brand
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Brand: {self.brand}\n")

mobile1=Mobile("T3 5G",19999,"Vivo")
mobile1.display()
mobile2=Mobile("iphone 16",80999,"Apple")
mobile2.display()