"""
From the given string,

extract
IP
DATE
URL

Expected Output:
--------------------------
123.123.123.123
26/Apr/2000
http://www.jafsoft.com/asctortf/
--------------------------

"""

print('Input data:')
print("-"*20)
# --------------
input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)

print("#"*40, end="\n\n")
#######################