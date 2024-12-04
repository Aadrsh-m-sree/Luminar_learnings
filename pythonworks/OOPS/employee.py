class Employee:
    id:int
    name:str
    age:int
    department:str
    salary:int

    def set_employee(self,id,name,age,department,salary):
        self.id=id
        self.name=name
        self.age=age
        self.department=department
        self.salary=salary
    
    def display_emp(self):
        print(self.id)
        print(self.name)
        print(self.age)
        print(self.department)
        print(self.salary)
    

emp1=Employee()

emp1.set_employee(1001,"Navya",21,"HR",36000)
emp1.display_emp()