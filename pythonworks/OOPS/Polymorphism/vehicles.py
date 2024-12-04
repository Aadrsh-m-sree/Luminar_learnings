class Parent:
    def vehicles(self):
        self.bikes=["passion pro","activa"]
        return self.bikes

class Child(Parent):
    def vehicles(self):
        self.bikes=super().vehicles()
        self.bikes.append("hunter")
        return self.bikes

child_instance=Child()
print(child_instance.vehicles())