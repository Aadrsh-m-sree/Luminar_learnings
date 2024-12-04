class Parent:
    def mobile(self):
        print("Nokia")

class Child(Parent):
    def mobile(self):#redefining existing method of Parent
        print("iphone 16 pro")

child_instance=Child()
child_instance.mobile()