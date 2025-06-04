"""
In this program, we are accessing
variables
functions
classes present in mymodule library
"""
print("1-Way using 'import-statement'")
print("-"*20)
# ---------------

import mymodule

print("Course:", mymodule.course)

add_result = mymodule.add(1, 2)
print("Add result:", add_result)

e1 = mymodule.Employee()
e1.set_name("emp-1")
print("e1 name:", e1.get_name())

print("#"*40, end="\n\n")
#####################

print("2-Way using 'from-import-statement'")
print("-"*20)
# ---------------

from mymodule import add, course, Employee

print("Course:", course)

add_result = add(1, 2)
print("Add result:", add_result)

e1 = Employee()
e1.set_name("emp-1")
print("e1 name:", e1.get_name())

print("#"*40, end="\n\n")
#####################

print("WITH SHORT NAME: 1-Way using 'import-statement'")
print("-"*20)
# ---------------

import mymodule as mm

print("Course:", mm.course)

add_result = mm.add(1, 2)
print("Add result:", add_result)

e1 = mm.Employee()
e1.set_name("emp-1")
print("e1 name:", e1.get_name())

print("#"*40, end="\n\n")
#####################

print("WITH SHORT NAME: 2-Way using 'from-import-statement'")
print("-"*20)
# ---------------

from mymodule import add as a, course as c, Employee as E

print("Course:", c)

add_result = a(1, 2)
print("Add result:", add_result)

e1 = E()
e1.set_name("emp-1")
print("e1 name:", e1.get_name())

print("#"*40, end="\n\n")
#####################