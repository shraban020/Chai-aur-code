"""
Description:
    Dictionary:
            -- We have option store multiple values like list of employee names
            -- We can keep DUPLICATE values
            -- Manually We-have-to/we-need-to provide index to each value(KEY/VALUE pair)
Documentation: https://docs.python.org/3/library/index.html
"""
print("Dictionary PART-1")
print("Store Values")
print("-"*20)
# --------------

my_dictionary = {
    "duration": 2,
    "course": "python",
    "mode": ["online", "offline"],
    "trainer": {"fname":"abc", "lname": "xyz"}
}
print(my_dictionary)

# FOR KEYS: Use int, float, strings, tuple
# FOR VALUES: We can store any values inside dictionary

print("#"*40, end="\n\n")
#######################