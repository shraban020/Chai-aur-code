print("Strings PART-6")
print("Step Value: We can skip characters")
print("-"*20)
# --------------

my_string = "WEL COME"
print("my_string:",my_string, end="\n\n")

print("Sub string from index-1 to 6 using positive index number and default step by 1:", my_string[1:6])
print("Sub string from index-1 to 6 using negative index number  and default step by 1:", my_string[-7:-2], end="\n\n")
# default step=1: which means from index-1 to 6, give me every character

print("Sub string from index-1 to 6 using positive index number and step by 1:", my_string[1:6:1])
print("Sub string from index-1 to 6 using negative index number  and step by 1:", my_string[-7:-2:1], end="\n\n")
# step=1: which means from index-1 to 6, give me every character

print("Sub string from index-1 to 6 using positive index number and step by 2:", my_string[1:6:2])
print("Sub string from index-1 to 6 using negative index number  and step by 2:", my_string[-7:-2:2], end="\n\n")
# step=2: which means from index-1 to 6, give me every 2nd character

print("Sub string from index-1 to 6 using positive index number and step by 3:", my_string[1:6:3])
print("Sub string from index-1 to 6 using negative index number  and step by 3:", my_string[-7:-2:3], end="\n\n")
# step=3: which means from index-1 to 6, give me every 3rd character

print("#"*40, end="\n\n")
#######################