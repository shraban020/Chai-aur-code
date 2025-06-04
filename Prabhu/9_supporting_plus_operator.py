"""
Supporting + operator

In python, for each operator there is a name
example: + = __add__

If we want to support for + then we need to write __add__ method inside out class
"""
print("Supporting + operator")
print("-"*20)
# ---------------

class Employee:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name

    def __add__(self, other_object): # self=e1, other_object=e2
        return self.name + other_object.name


e1 = Employee("emp-1")
e2 = Employee("emp-2")
add_result = e1 + e2
print("add_result:", add_result)

print("#"*40, end="\n\n")
#####################