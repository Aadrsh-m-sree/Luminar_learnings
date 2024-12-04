class Operations:
    def add(self,n1,n2):
        print(n1+n2)

    def add(self,n1,n2,n3):
        print(n1+n2+n3)

obj=Operations()
#obj.add(10,20)#error, the method must take 3 arguments


#python does not support method overloading for performing this *args can be used with self

class Operations:
    def add(self,*args):
        print(sum(args))

obj=Operations()
obj.add(10,20)