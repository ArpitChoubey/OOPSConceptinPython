class GrandParent:
    def grandparent_method(self):
        print("GrandParent Method")

class Parent(GrandParent):
    def parent_method(self):
        print("Parent Method")

class Child(Parent):
    def child_method(self):
        print("Child Method")

obj = Child()
obj.grandparent_method()
obj.parent_method()
obj.child_method()