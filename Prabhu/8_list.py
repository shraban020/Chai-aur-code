"""
Description:
    list:
        -- We have option store multiple values like list of employee names
        -- We can keep DUPLICATE values
        -- Automatically, index number will be assigned to each value

Documentation:
    https://docs.python.org/3/library/index.html
"""

print("list PART-1")
print("Store multiple values like list of employee names")
print("-"*20)
# --------------

my_list = [10, 12.5, "python", "python", (100, 200), (100, 200)]
print("my_list:", my_list)

print("#"*40, end="\n\n")
#######################


print("list PART-2")
print('indexes are similar to strings')
print("-"*20)
# --------------

my_list = [10, 12.5, "python", "python", (100, 200), (100, 200)]
print("my_list:", my_list, end="\n\n")

print("1st value:", my_list[0])
print("2nd value:", my_list[1])
print("3rd value:", my_list[2])
print("4th value:", my_list[3])
print("5th value:", my_list[4])
print("6th value:", my_list[5])

print("#"*40, end="\n\n")
#######################

print("list PART-3")
print("Methods present inside list class")
print("-"*20)
# --------------

print(dir(my_list))
# OR
# print(dir(list))

print("#"*40, end="\n\n")
#######################

print("list PART-4")
print("Trying 'index' and 'count' method")
print("-"*20)
# --------------

my_list = [10, 12.5, "python","python","python","python", "python", (100, 200), (100, 200)]
print("my_list:", my_list, end="\n\n")

index_of_python = my_list.index('python')
count_of_python = my_list.count('python')

print("index_of_python:", index_of_python, end="\n\n")
print("count_of_python:", count_of_python, end="\n\n")

print("#"*40, end="\n\n")
#######################

print("list PART-5")
print("ADD/REMOVE/UPDATE")
print("-"*20)
# --------------

my_list = [10, 12.5, "python","python","python","python", "python", (100, 200), (100, 200)]
print("my_list:", my_list, end="\n\n")

# Add new value
my_list.append("java")
my_list.insert(2, "Perl")
print("my_list after adding java & perl:", my_list, end="\n\n")

# UPDATE
my_list[3] = "Perl"
print("my_list after updatin to perl:", my_list, end="\n\n")

# DELETE
x = my_list.pop(1)
my_list.remove("python")
print("my_list after deleting 12.5, & python:", my_list, end="\n\n")


print("#"*40, end="\n\n")
#######################