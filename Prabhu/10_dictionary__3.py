print("Dictionary PART-3")
print("Methods present in dict class")
print("-" * 20)

# Define a dummy dictionary first
my_dictionary = {"sample": 1}
print(dir(my_dictionary))

print("#" * 40, end="\n\n")
#######################

print("Dictionary PART-4")
print("ADD/REMOVE/UPDATE")
print("-" * 20)

# Reassign actual dictionary
my_dictionary = {
    "duration": 2,
    "course": "python",
}
print("my_dictionary:", my_dictionary, end="\n\n")

# ADD/UPDATE
my_dictionary["mode"] = "offline"
print("my_dictionary after adding mode:", my_dictionary, end="\n\n")

another_dict = {"trainer": {"fname": "abc", "lname": "xyz"}}
my_dictionary.update(another_dict)
print("my_dictionary after updating another dictionary:", my_dictionary, end="\n\n")

# REMOVE
my_dictionary.pop("trainer")
print("my_dictionary after removing trainer:", my_dictionary, end="\n\n")

my_dictionary.popitem()  # Removes the last item
print("my_dictionary after popitem:", my_dictionary, end="\n\n")

print("#" * 40, end="\n\n")
