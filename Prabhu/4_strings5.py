print("Strings PART-5")
print("Indexes: Get the sub string")
print("-"*20)
# --------------

my_string = "WEL COME"
print("my_string:",my_string, end="\n\n")

print("Sub string from index-1 to 6 using positive index number:", my_string[1:6])
print("Sub string from index-1 to 6 using negative index number:", my_string[-7:-2])
print("Sub string from index-1 to 6 using positive/negative index number:", my_string[-7:6])
print("Sub string from index-1 to 6 using positive/negative index number:", my_string[1:-2], end="\n\n")

print("Sub string from index-1 to END using positive index number:", my_string[1:])
print("Sub string from index-1 to END using negative index number:", my_string[-7:])

print("Sub string from BEGINNING to 6 using positive index number:", my_string[:6])
print("Sub string from BEGINNING to 6 using negative index number:", my_string[:-2])

print("#"*40, end="\n\n")
#######################