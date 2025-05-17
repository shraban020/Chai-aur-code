print("Strings PART-7")
print("negative Step Value: reverse order of string")
print("-"*20)
# --------------

my_string = "WEL COME"
print("my_string:",my_string, end="\n\n")

# Step we need to follow for reverse order of string
# Example: from 6 to 1 reverse
# step-1: start index should be 6
# step-2: end index should be 1
# step-3: step value should be negative i.e -1 here
# If we miss any step then we will get EMPTY string

print("Substring from index-6 to 1 using positive index number with step value -1:", my_string[6:1:-1])
print("Substring from index-6 to 1 using negative index number with step value -1:", my_string[-2:-7:-1], end="\n\n")

print("Substring from index-6 to 1 using positive index number with step value -2:", my_string[6:1:-2])
print("Substring from index-6 to 1 using negative index number with step value -2:", my_string[-2:-7:-2], end="\n\n")

print("#"*40, end="\n\n")
#######################