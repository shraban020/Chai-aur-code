"""
Get data from log_report_1.json

and

write to log_report_5.txt
"""
print("Get data from log_report_1.json")
print("-"*20)
# --------------

my_json_file_handle = open("log_report_1.json", "r")

import json
json_file_content = json.load(my_json_file_handle)

my_json_file_handle.close()

print(json_file_content)

print("#"*40, end="\n\n")
#######################

print("Write to log_report_5.txt")
print("-"*20)
# --------------

my_file_handle = open("log_report_5.txt", "w")

print("IP", "DATE", "URL", sep="\t", file=my_file_handle)

for i in json_file_content.values(): # [[ip, dt, url],[ip, dt, url],[ip, dt, url]]
    print(i[0], i[1], i[2], sep="\t", file=my_file_handle)

my_file_handle.close()

print("log_report_5.txt created")

print("#"*40, end="\n\n")
#######################