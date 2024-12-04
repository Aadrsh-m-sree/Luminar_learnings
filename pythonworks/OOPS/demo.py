class Employee:
    def set_emp(self, name, age, salary,department):
        self.name = name
        self.age = age
        self.salary = salary
        self. department = department
    def __str__(self):
        return f"Employee('{self.name}', '{self.age}', '{self.salary}', '{self.department}')"

emp1 = Employee()
emp1.set_emp('Adarsh',25,80000,'IT')
print(emp1)

emp2 = Employee()
emp2.set_emp("Praveen",24,70000,'HR')
print(emp2)




class Employee:
    def __init__(self, name, age, salary,department):
        self.name = name
        self.age = age
        self.salary = salary
        self. department = department
    def __str__(self):
        return f"Employee('{self.name}', '{self.age}', '{self.salary}', '{self.department}')"

emp1 = Employee('Adarsh',25,80000,'IT')
print(emp1)

emp2 = Employee("Praveen",24,70000,'HR')
print(emp2)

# employee
# student