"""
Description:
    Frozenset:
        -- We have option store multiple values like list of employee names
        -- We can keep UNIQUE values
        -- NO index for each value
        -- it is unordered collection

Documentation:
    https://docs.python.org/3/library/index.html
"""
print("Frozenset PART-1:")
print("Store Values")
print("-"*20)
# --------------

# '  '  -> shortcut for string
# ()  -> shortcut for tuple
# []  -> shortcut for list
# {}  -> shortcut for dict
# {}  -> shortcut for set
# frozenset -> we don't have shortcut

my_fs = frozenset([10, 10, 10, "python", "python", "python", "java", "java", "java"])
print(my_fs)

# If we want index then convert to list/tuple
# OR
# iterate using for-loop
#
print("#"*40, end="\n\n")
#######################

print("Frozenset PART-2:")
print("Methods present in frozenset class:")
print("-"*20)
# --------------

print(dir(my_fs))

print("#"*40, end="\n\n")
#######################

print("Frozenset PART-3:")
print("union, difference, intersection methods")
print("-"*20)
# --------------

java_course_candidates = frozenset(["emp-1", "emp-2", "emp-3", "emp-4"])
python_course_candidates = frozenset([ "emp-3", "emp-4", "emp-5", "emp-6"])
print("java_course_candidates:", java_course_candidates)
print("python_course_candidates:", python_course_candidates, end="\n\n")

all_employees = java_course_candidates.union(python_course_candidates)
print("all_employees:", all_employees, end="\n\n")

employees_in_both_courses = java_course_candidates.intersection(python_course_candidates)
print("employees_in_both:", employees_in_both_courses, end="\n\n")

employees_only_in_java = java_course_candidates.difference(python_course_candidates)
print("employees_only_in_java:", employees_only_in_java, end="\n\n")

print("#"*40, end="\n\n")
#######################