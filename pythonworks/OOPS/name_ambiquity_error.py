class GrandParent:
    def m1(self):
        print("Grand parent class m1 method")

class Parent:
    def m1(self):
        print("Parent class m2 method")

class Child(Parent,GrandParent): #causes name ambiguity error in java,in python the program will inherit method from parent
    def m3(self):
        print("Child class m3 method")

child_instance1=Child()
child_instance1.m1()
child_instance1.m3()