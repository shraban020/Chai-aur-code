"""
How to get object?
- Using class

Here,
we are
    - writing class,
    - creating objects
    - store data/values
"""

print("writing class,")
print("-"*20)
# ---------------

class Employee:
    pass

# Above class is empty class
# Above class is valid class
# Valid class means, we can create object, we can store data BUT since it is empty, NO functionalities present

# pass: dummy keyword
# pass: Does nothing
# pass: use this to keep any EMPTY block. like if-block, for-block, while-block etc


print("#"*40, end="\n\n")
#####################

print("creating objects")
print("-"*20)
# ---------------

e1 = Employee() # It will create object and referred by e1
e2 = Employee() # It will create object and referred by e2
e3 = Employee() # It will create object and referred by e3

# Existing-class/builtin-class examples
a = int(10) # shortcut is a = 10
b = float(12.5) # shortcut is b = 12.5
c = str("Hi") # shortcut is c = "Hi"
d = list([10, 20, 30]) # shortcut is d = [10, 20, 30]
e = tuple([10, 20, 30]) # shortcut is e = (10, 20, 30)

print("#"*40, end="\n\n")
#####################

print("store data/values")
print("-"*20)
# ---------------

e1.name = "emp-1"
e1.email = "emp-1@abcxyz.com"
e1.address = "emp-1 address"

e2.name = "emp-2"
e2.email = "emp-2 email"
e2.address = "emp-2 address"
e2.phone = "111111111"

e3.name = "emp-3"
e3.email = "emp-3 email"
e3.address = "emp-3 address"
e3.another_email = "emp-3 another_email"

print("#"*40, end="\n\n")
#####################

print("DATA present inside each employee class objects")
print("-"*20)
# ---------------

print("Employee 1 name:", e1.name)
print("Employee 1 email:", e1.email)
print("Employee 1 address:", e1.address)

print("Employee 2 name:", e2.name)
print("Employee 2 email:", e2.email)
print("Employee 2 address:", e2.address)

print("Employee 3 name:", e3.name)
print("Employee 3 email:", e3.email)
print("Employee 3 address:", e3.address)

print("#"*40, end="\n\n")
#####################

print("METHODS/VARIABLES present inside each Employee class objects")
print("-"*20)
# ---------------

print("METHODS/VARIABLES present inside 'e1' object:", dir(e1), sep="\n", end="\n\n")
print("METHODS/VARIABLES present inside 'e2' object:", dir(e2), sep="\n", end="\n\n")
print("METHODS/VARIABLES present inside 'e3' object:", dir(e3), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
#####################