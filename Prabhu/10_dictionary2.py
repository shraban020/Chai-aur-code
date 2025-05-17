print("Dictionary PART-2")
print("Access each value using key")
print("-"*20)
# --------------

my_dictionary = {
    "duration": 2,
    "course": "python",
    "mode": ["online", "offline"],
    "trainer": {"fname":"abc", "lname": "xyz"}
}
print("my_dictionary:", my_dictionary, end="\n\n")


print("Duration:", my_dictionary["duration"])

print("Course:", my_dictionary["course"])

print("Mode:", my_dictionary["mode"])

print("Trainer:", my_dictionary["trainer"])

print("#"*40, end="\n\n")
#######################