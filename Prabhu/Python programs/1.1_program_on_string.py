print("Extract IP - 1 - way: PARTIAL")
print("-"*20)
# --------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
ip= input_data[0:15]
print(ip)


print("#"*40, end="\n\n")
#######################


print("Extract IP - 2 - way: FINAL")
print("-"*20)
# --------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

start_index = 0
end_index = input_data.index(" ")
ip = input_data[start_index:end_index]
print(ip)
# Example:
# >>> # About index() method
# >>> s = "WEL COME"
# >>> # Feature-1
# >>> s.index("E") # returns 1st occurance of 'E'
# 1
# >>>
# >>> # Feature-2
# >>> s.index("E", 4) # start from index
# 7
# >>> # Feature-3
# >>> s.index("nbdjksasada")
# Traceback (most recent call last):
#   File "<pyshell#14>", line 1, in <module>
#     s.index("nbdjksasada")
# ValueError: substring not found

print("#"*40, end="\n\n")
#######################

print("Extract IP - 3 - way: FINAL")
print("-"*20)
# --------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp = input_data.split()
print("sp:", sp)

ip = sp[0]
print(ip)

print("#"*40, end="\n\n")
#######################