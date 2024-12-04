class Person:
    name : str
    age : int

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_person_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")

class Employee:
    emp_id:int
    salary: int

    def __init__(self,id,salary):
        self.emp_id=id
        self.salary=salary

    def display_employee_info(self):
        print(f"ID : {self.emp_id}")
        print(f"Salary : {self.salary}")

class Manager(Person,Employee):
    department:str
    def __init__(self,name,age,eid,salary,dept):
        Person.__init__(self,name,age)
        Employee.__init__(self,eid,salary)
        self.department=dept
        self.display_manager_info()

    def display_manager_info(self):
        self.display_person_info()
        self.display_employee_info()
        print(f"Department : {self.department}")


manager_instance=Manager("Navya",21,1001,4000,"Cleaning")
# manager_instance.display_manager_info()