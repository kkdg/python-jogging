class Parent:
	parentAttr = 100
        def __init__(self):
            print "Calling parent constructor"

        def parentMethod(self):
            print "calling parent method"

        def setAttr(self, attr):
            Parent.parentAttr = attr

        def getAttr(self):
            print "Parent Attribute : ", Parent.parentAttr

class Brother:
        brotherAttr = 300

class Child(Parent,Brother):
        def __init__(self):
            print "Calling child constructor"

        def childMethod(self):
            print "Calling child method"

c = Child()
c.childMethod()
c.parentMethod()
c.getAttr()
c.setAttr(200)
c.getAttr()
print c.parentAttr
print c.brotherAttr
