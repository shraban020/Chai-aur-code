print("Strings PART-7")
print("Data and Methods present inside each objects")
print("-"*20)
# --------------

a = 'PERSON'
b = "PERSON'S"
c = """PERSON'S HEIGHT IS XYZ" (" REPRESENTS INCH)"""

print('DATA present inside a:', a)
print('DATA present inside b:', b)
print('DATA present inside c:', c)

print('METHODS present inside a:', dir(a))
print('METHODS present inside b:', dir(b))
print('METHODS present inside c:', dir(c))

print("#"*40, end="\n\n")
#######################