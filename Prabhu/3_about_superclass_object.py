"""
About builtin class 'object'
- 'object' is one class
- 'object' has some basic methods required for each and every classes
    like __new__ which is constructor, required for all classes
    like __init__ which is initializer, required for all classes
- These basic methods which is present in 'object-class'
    will automatically comes to each and every classes.
    This is called inheritance
"""
import builtins

print("Complete builtins list")
print("-"*20)
# ---------------

print(dir(builtins))

print("#"*40, end="\n\n")
#####################

print("Inside 'object' class")
print("-"*20)
# ---------------

print(dir(object))

# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__']

# These many things will come to each and every class. It can be builtin class or any class

print("#"*40, end="\n\n")
#####################


print("Inside 'str' class")
print("-"*20)
# ---------------

print(dir(str))

print("#"*40, end="\n\n")
#####################

print("Inside 'Employee' class")
print("-"*20)
# ---------------


class Employee:
    pass

print(dir(Employee))

print("#"*40, end="\n\n")
#####################

print("Inside 'Employee' class object 'e1'")
print("-"*20)
# ---------------


e1 = Employee()
# e1.name = "emp-1"
print(dir(e1))

print("#"*40, end="\n\n")
#####################