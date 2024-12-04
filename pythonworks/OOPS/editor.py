class Editor:
    name : str
    vendor : str

    def __init__(self,name,vendor):
        self.name, self.vendor = name , vendor
    
    def display(self):
        print(f"Name : {self.name}")
        print(f"Vendor : {self.vendor}")

    def __str__(self):
        return self.name
editor_instance1 = Editor("VScode","Microsoft")
editor_instance2 = Editor("PyCharm","Jetbrains")
editor_instance1.display()
print(editor_instance1)
print(editor_instance2)