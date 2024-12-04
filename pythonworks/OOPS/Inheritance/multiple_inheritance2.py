class Cuisine:
    cuisine:str

    def __init__(self,cus):
        self.cuisine=cus

    def display_cuisine_info(self):
        print(f"Cuisine : {self.cuisine}")

class MealType:
    name:str

    def __init__(self,name):
        self.name=name

    def display_meal_info(self):
        print(f"Meal Type : {self.name}")

class Dish(Cuisine,MealType):
    dish_name:str

    def __init__(self,cuisine,name,dish_name):
        Cuisine.__init__(self,cuisine)
        MealType.__init__(self,name)
        self.dish_name=dish_name

    def display_dish_info(self):
        self.display_cuisine_info()
        self.display_meal_info()
        print(f"Dish name : {self.dish_name}")

dish_instance1=Dish("Indian","Breakfast","Gheeroast")
dish_instance1.display_dish_info()
