"""
Handling Exceptions:
"""

# print("WITHOUT Handling Exceptions")
# print("-"*20)
# # ---------------
#
# a = 10
# b = 0
# c = a /b # Program will terminate here
# print(c)
#
# print("#"*40, end="\n\n")
# #####################

print("Handling Exceptions using try-except")
print("-"*20)
# ---------------

# try block:
    # Here keep the code
    # If any error comes here then it will execute 'except' block
    # If NO error comes here then it will skip 'except' block
# except block:
    # If any error in try, what we want take care, that code we need to write here

try:
    a = 10
    b = 0
    c = a /b # Program will NOT terminate here, instead control will be passed to except block
    print(c)
except:
    print("Reached except block")

print("#"*40, end="\n\n")
#####################

# ---------------
# About Exception classes
# ---------------
# - If we want to handle exception using try-except then
#   we need to have exception class for that error
# - Few exception classes are present in builtins
# - default 'except' will be able to handle only the exceptions classes
#   present in builtins
# - For other type of error, we need to write exception-class if we want to handle
# - 'Exception' is super class for all 'Exception' classes
#####################

print("Handling Exceptions using try-except with class names")
print("-"*20)
# ---------------
try:
    a = 10
    b = 0
    c = a /b
    print(c)
except ZeroDivisionError: # 1-way: This is one-way to specify class name
    print("Reached except block")
    print("This is ZDE")

except NameError as ne: # 2-way: THis is second-way to specify class name, here we are storing error class object
    print("Reached except block")
    print("This is NE")

except Exception as e:
    print("Reached Default exception block and error message is:", e)

print("#"*40, end="\n\n")
#####################

print("Using try-except-else-finally blocks")
print("-"*20)
# ---------------

try:
    print("Reached try block")
    my_file_handle = open(file="D:\wrong\path.txt", mode="w")
except Exception as e:
    print("Reached except block")
    print("In this block, we are writing logic to handle file open error")
    print("Not able to open file. Error message:", e)
else:
    print("Reached else block")
    my_file_handle.write("Hi")
    my_file_handle.write("Hello")
finally:
    print("Reached finally block")
    try:
        my_file_handle.close()
    except Exception as e:
        print("Not able to close file, Reason:", e)


# About 'else-block':
# - if try success then execute 'else' block and skip 'except' block
# - if try failed then execute 'except' block and skip 'else' block

# About 'finally-block'
# - if try/except/else success/failed, In any case, finally block will execute

print("#"*40, end="\n\n")
#####################

print("User defined exception class example")
print("-"*20)
# ---------------

# Mandatory Step: Our class should be sub-class of 'Exception' class.
# OR if some classes are already inherited from 'Exception' class like all builtin exception casses.
#  then we can extend that class as well

class MyError(Exception):
    pass


# Empty Exception class
# Valid Exception class
# Valid Exception class means, we can use this class to handle exception using try-except

try:
    x = 10
    if x == 10:
        raise MyError("Here value of x is 10")
    if x > 10:
        raise MyError("Here value of x is greater than 10")
    if x < 10:
        raise MyError("Here value of x is less than 10")

except MyError as e:
    print("Reached MyError except block and error message:", e)



# class MyError(Exception):
#     def debug(self):
#         pass
#     def help(self):
#         pass

print("#"*40, end="\n\n")
#####################

