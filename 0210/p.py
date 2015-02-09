class Parent:
    def myMethod(self):
        print "Me parent"

class Child(Parent):
    def myMethod(self):
        print "Me child"

c = Child()
c.myMethod()
