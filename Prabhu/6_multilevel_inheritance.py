"""
Inheritance:
1. multilevel inheritance
2. multiple inheritance

Here,
1. multilevel inheritance
"""
print("Existing class - 1")
print("-"*20)
# ---------------

class Salary:
    def set_salary(self, salary):
        self.salary = salary
    def get_salary(self):
        return self.salary

print("#"*40, end="\n\n")
#####################

print("Extending Existing class - 1")
print("-"*20)
# ---------------

# Add below methods to existing class Salary
# 1. set tax method
# 2. get tax method
# 3. modify, get_salary to return (salary-tax)
# 4. add methods to get_old_salary
# 5. Use @property decorator to access salary using method name as like variable name

class Employee(Salary):
    # 1. set tax method
    def set_tax(self, tax):
        self.tax = tax

    # 2. get tax method
    def get_tax(self):
        return self.tax

    # 3. modify, get_salary to return (salary-tax)
    def get_salary(self): # Method Overriding
        return self.salary - self.tax

    # 4. add methods to get_old_salary
    def get_old_salary(self):
        # We can also Access super class methods
        # 1 - way : using super()
        old_salary = super().get_salary()
        # OR
        # 2-way : Using class name
        old_salary = Salary.get_salary(self)
        return old_salary

    # 5. Use @property decorator to access salary using method name as like variable name
    @property
    def salary_property(self):
        return self.salary

print("#"*40, end="\n\n")
#####################

print("Creating Objects")
print("-"*20)
# ---------------

e1 = Employee()
e2 = Employee()
e3 = Employee()

print("#"*40, end="\n\n")
#####################

print("Store the values of e1, e2, e3")
print("-"*20)
# ---------------

e1.set_salary(100)
e2.set_salary(200)
e3.set_salary(300)

e1.set_tax(10)
e2.set_tax(20)
e3.set_tax(30)

print("#"*40, end="\n\n")
#####################

print("Access values from e1, e2, e3")
print("-"*20)
# ---------------

print("e1 Salary:", e1.get_salary())
print("e2 Salary:", e2.get_salary())
print("e3 Salary:", e3.get_salary())

print("e1 tax:", e1.get_tax())
print("e2 tax:", e2.get_tax())
print("e3 tax:", e3.get_tax())

print("e1 old_salary:", e1.get_old_salary())
print("e2 old_salary:", e2.get_old_salary())
print("e3 old_salary:", e3.get_old_salary())

print("e1 salary using property:", e1.salary_property)
# Using @property, we can use method like a variable
print("e2 salary using property:", e2.salary_property)
# Using @property, we can use method like a variable
print("e3 salary using property:", e3.salary_property)
# Using @property, we can use method like a variable

print("#"*40, end="\n\n")
#####################
