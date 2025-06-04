print("Extract DATE")
print("-"*20)
# --------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp = input_data.split()
# print("sp:", sp)

raw_date = sp[3] # '[26/Apr/2000:00:23:48'

start_index = 1
end_index = raw_date.index(":")

dt = raw_date[start_index:end_index]
print(dt)

print("#"*40, end="\n\n")
#######################

print("Extract URL")
print("-"*20)
# --------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp = input_data.split()
print("sp:", sp)

raw_url = sp[10] # '"http://www.jafsoft.com/asctortf/"'

url = raw_url[1:-1]
print(url)

print("#"*40, end="\n\n")
#######################