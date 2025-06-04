"""
Documentation:
https://docs.python.org/3/
https://docs.python.org/3/library/index.html
https://docs.python.org/3/reference/index.html


Why Object?

2 Things
1. Encapsulation: Keep data/values and related functions(called methods)
2. Abstraction: Achieving through methods. Here we just need to know how to use method
            No need to know its implementation
"""

print("DATA/VALUES present inside existing class 'str' objects")
print("-"*20)
# ---------------

a = "Hello"
b = "Hi"
c = "Hi Hello"

print("DATA/VALUES present inside 'str' object 'a':", a)
print("DATA/VALUES present inside 'str' object 'b':", b)
print("DATA/VALUES present inside 'str' object 'c':", c)

print("#"*40, end="\n\n") # after print, put 2 newline
#####################

print("METHODS/VARIABLES present inside existing class 'str' objects")
print("-"*20)
# ---------------

a = "Hello"
b = "Hi"
c = "Hi Hello"
d = 10 # int
e = "10" # str

print("METHODS/VARIABLES present inside existing class 'str' object 'a': ", dir(a), sep="\n", end="\n\n")
print("METHODS/VARIABLES present inside existing class 'str' object 'b': ", dir(b), sep="\n", end="\n\n")
print("METHODS/VARIABLES present inside existing class 'str' object 'c': ", dir(c), sep="\n", end="\n\n")

print("#"*40, end="\n\n") # after print, put 2 newline
#####################

# -----------
# Popularity
# -----------
# https://www.tiobe.com/tiobe-index/
######################

# -----------
# Official website
# -----------
# https://www.python.org/
######################

# -----------
# Few popular IDEs
# -----------
# IDLE -> Basic IDE, Getting installed when we install python
# PyCharm
# VS Code
# Notebook
# Spyder
# Anaconda bundle
# Many more
######################