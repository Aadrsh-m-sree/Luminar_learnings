class GrandParent:
    def m1(self):
        print("Grand parent class m1 method")

class Parent:
    def m2(self):
        print("Parent class m2 method")

class Child(GrandParent,Parent): #multiple inheritance
    def m3(self):
        print("Child class m3 method")

child_instance1=Child()
child_instance1.m1()
child_instance1.m2()
child_instance1.m3()