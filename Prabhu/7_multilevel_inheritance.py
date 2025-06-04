"""
multilevel inheritance: extend list class

Here, add below methods to list class
1. add course name method
2. get course name method
"""
print("Extending from list class")
print("-"*20)
# ---------------

class NewListClass(list):
    def store_course_name(self, course_name):
        self.append(course_name)
    def get_course_name(self):
        return self.pop()

print("#"*40, end="\n\n")
#####################

print("Testing new list class")
print("-"*20)
# ---------------

my_list = NewListClass([100, 200, "Java", "Python"])
print("my_list:", my_list)

my_list.append("C++")
my_list.append("Java-2")
print("my_list after appending C++ and Java-2:", my_list)

my_list.store_course_name("MyCourse")
print("my_list after adding 'MyCourse' using store_course_name method:", my_list)

print("#"*40, end="\n\n")
#####################