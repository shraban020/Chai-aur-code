"""
Description:
    Tuple:
        -- We have option store multiple values like list of employee names
        -- We can keep DUPLICATE values
        -- Automatically, index number will be assigned to each value

Documentation:
    https://docs.python.org/3/library/index.html
"""

print("Tuple PART-1")
print("Store multiple values like list of employee names")
print("-"*20)
# --------------

my_tuple = (10, 12.5, "python", "python", (100, 200), (100, 200))
print("my_tuple:", my_tuple)

print("#"*40, end="\n\n")
#######################


print("Tuple PART-2")
print('indexes are similar to strings')
print("-"*20)
# --------------

my_tuple = (10, 12.5, "python", "python", (100, 200), (100, 200))
print("my_tuple:", my_tuple, end="\n\n")

print("1st value:", my_tuple[0])
print("2nd value:", my_tuple[1])
print("3rd value:", my_tuple[2])
print("4th value:", my_tuple[3])
print("5th value:", my_tuple[4])
print("6th value:", my_tuple[5])

print("#"*40, end="\n\n")
#######################

print("Tuple PART-3")
print("Methods present inside tuple class")
print("-"*20)
# --------------

print(dir(my_tuple))
# OR
# print(dir(tuple))

print("#"*40, end="\n\n")
#######################

print("Tuple PART-4")
print("Trying 'index' and 'count' method")
print("-"*20)
# --------------

my_tuple = (10, 12.5, "python","python","python","python", "python", (100, 200), (100, 200))
print("my_tuple:", my_tuple, end="\n\n")

index_of_python = my_tuple.index('python')
count_of_python = my_tuple.count('python')

print("index_of_python:", index_of_python, end="\n\n")
print("count_of_python:", count_of_python, end="\n\n")

print("#"*40, end="\n\n")
#######################