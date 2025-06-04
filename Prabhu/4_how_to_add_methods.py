"""
How to add methods

Requirement:
1. add method to store name, email, address
2. add method to store phone
3. add method to store another_email
4. add method to get name, email, address
5. add method to get phone
6. add method to get another_email
"""

print("writing class,")
print("-"*20)
# ---------------

class Employee:
    # 1. add method to store name, email, address
    def store_name_email_address(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    # 2. add method to store phone
    def store_phone(self, phone):
        self.phone = phone

    # 3. add method to store another_email
    def store_another_email(self, another_email):
        self.another_email = another_email

    # 4. add method to get name, email, address
    def get_name_email_address(self):
        return [self.name, self.email, self.address]

    # 5. add method to get phone
    def get_phone(self):
        return self.phone

    # 6. add method to get another_email
    def get_another_email(self):
        return self.another_email

print("#"*40, end="\n\n")
#####################

print("creating objects")
print("-"*20)
# ---------------

e1 = Employee() # It will create object and referred by e1
e2 = Employee() # It will create object and referred by e2
e3 = Employee() # It will create object and referred by e3

print("#"*40, end="\n\n")
#####################

print("store data/values")
print("-"*20)
# ---------------

e1.store_name_email_address("emp-1", "emp-1@emp-1.com", "emp-1 address")
# Internally, object 'e1' will be passed to 1st argument i.e self

e2.store_name_email_address("emp-2", "emp-2@emp-2.com", "emp-2 address")
# Internally, object 'e2' will be passed to 1st argument i.e self
e2.store_phone("111111")

e3.store_name_email_address("emp-3", "emp-3@emp-3.com", "emp-3 address")
# Internally, object 'e3' will be passed to 1st argument i.e self
e3.store_another_email("emp-3 @ another email")

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