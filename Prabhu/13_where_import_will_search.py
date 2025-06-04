"""
List of directories where import will search
and also
we are discussing on how to add new location
"""
print("List of directories where import will search")
print("-"*20)
# ---------------

import sys
print(sys.path)

print("#"*40, end="\n\n")
#####################

print("How to add new location")
print("-"*20)
# ---------------

import sys
sys.path.append(r"D:\mylib1")
sys.path.append(r"D:\mylib2")
sys.path.append(r"D:\mylib3")

print(sys.path)

print("#"*40, end="\n\n")
#####################

# This is for all directory and file operattions
# import os
# print(os.getcwd())