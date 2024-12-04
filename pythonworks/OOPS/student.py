class Student:
    roll:int
    name:str
    age:int
    course:str

    def set_student(self,roll,name,age,course):
        self.roll=roll
        self.name=name
        self.age=age
        self.course=course
    
    def display_student(self):
        print(self.roll)
        print(self.name)
        print(self.age)
        print(self.course)
    

stud=Student()

stud.set_student(5,"Navya",21,"Django")
stud.display_student()

#