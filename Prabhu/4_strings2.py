print("Strings PART-2")
print("Store Values")
print("-"*20)
# --------------

my_file_path_1 = "C:\newfolder\test.py"
# inside string \n replaced with newline , \t replaced with tab space
print("my_file_path_1=", my_file_path_1, end="\n\n")

my_file_path_2 = r"C:\newfolder\test.py"
# r -> raw string
print("my_file_path_2=", my_file_path_2, end="\n\n")

print("Convert already created string to raw format:", repr(my_file_path_1))

print("#"*40, end="\n\n")
#######################