class Father:
    def father_method(self):
        print("Father Method")

class Mother:
    def mother_method(self):
        print("Mother Method")

class Child(Father, Mother):
    def child_method(self):
        print("Child Method")

obj = Child()
obj.father_method()
obj.mother_method()
obj.child_method()