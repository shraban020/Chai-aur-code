"""
Rewriting or overriding __init__ method which is coming from 'object' class

When we create object like e1=Employee()
then
internally it calls 2 methods
1) __new__ : which has logic to construct a new object
2) __init__: Which has nothing, but automatically it will execute after __new__

Here,
we are making use of init to initialize each object with
"""

print("writing class,")
print("-"*20)
# ---------------

class Employee:
    def __init__(self, name, email, address, phone=None, another_email=None):
        self.name = name
        self.email = email
        self.address = address
        if phone is not None:
            self.phone = phone
        if another_email is not None:
            self.another_email = another_email

    def get_name_email_address(self):
        return [self.name, self.email, self.address]

    def get_phone(self):
        return self.phone

    def get_another_email(self):
        return self.another_email

print("#"*40, end="\n\n")
#####################

print("creating objects")
print("-"*20)
# ---------------

# e1 = Employee("emp-1", "emp-1@email", "emp-1 address") # It will create object and referred by e1
# OR
e1 = Employee(name="emp-1", email="emp-1@email", address="emp-1 address") # It will create object and referred by e1
e2 = Employee(name="emp-2", email="emp-2@email", address="emp-2 address", phone="11111111") # It will create object and referred by e1
e3 = Employee(name="emp-3", email="emp-3@email", address="emp-3 address", another_email="emp-3@another-email") # It will create object and referred by e1

print("#"*40, end="\n\n")
#####################

print("Access each values")
print("-"*20)
# ---------------

print("Employee 1 Details:", e1.get_name_email_address())
# Internally object 'e1' will be passed to self

print("Employee 2 Details:", e2.get_name_email_address())
print("Employee 2 Phone no:", e2.get_phone())
# Internally object 'e2' will be passed to self

print("Employee 3 Details:", e3.get_name_email_address())
print("Employee 3, another email:", e3.get_another_email())
# Internally object 'e3' will be passed to self

print("#"*40, end="\n\n")
#####################