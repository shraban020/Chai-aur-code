"""
multiple inheritance: Inherit from 2 or more classes
"""

print("Existing classes")
print("-"*20)
# ---------------

# Existing class - 1
class Salary:
    def set_salary(self, salary):
        self.salary = salary
    def get_salary(self):
        return self.salary

# Existing class -2
class Tax:
    def set_tax(self, tax):
        self.tax = tax
    def get_tax(self):
        return self.tax


print("#"*40, end="\n\n")
#####################

print("Extending from more than 1 class")
print("-"*20)
# ---------------

# Requirement:
# Create class with below functionalities
# 1. add/get salary
# 2. add/get tax
# 3. add/get name

# We can make use of existiing classes for below 2 requiremnts
# 1. add/get salary
# 2. add/get tax

class Employee(Salary, Tax):
    def store_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

print("#"*40, end="\n\n")
#####################

print("Create objects ")
print("-"*20)
# ---------------

e1 = Employee()

print("#"*40, end="\n\n")
#####################


print("Store the values")
print("-"*20)
# ---------------

e1.set_salary(2000)
e1.set_tax(100)
e1.store_name("emp-1")

print("#"*40, end="\n\n")
#####################

print("Get the values")
print("-"*20)
# ---------------

print("Name:", e1.get_name())
print("Tax:", e1.get_tax())
print("Salary:", e1.get_salary())

print("#"*40, end="\n\n")
#####################