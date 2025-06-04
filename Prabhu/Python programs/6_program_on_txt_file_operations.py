"""
Get data from sample_data.log

then

extract
IP
DATE
URL

then
write extracted data to file log_report_3.txt
"""

"""
Get data from sample_data.log

then

extract
IP
DATE
URL

then
write extracted data to file log_report_3.txt
"""
print("Get data from sample_data.log")
print("-"*20)
# --------------

my_log_file_handle = open(file="sample_data.log", mode="r")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()
print(log_file_content)

print("#"*40, end="\n\n")
#######################

print("Extract Info and write to file")
print("-"*20)
# --------------

my_report_file_handle = open(file="log_report_3.txt", mode="w")

# Write Heading

# 1) write
# my_report_file_handle.write("IP\tDATE\tURL\n")

# 2) write
# L = ["IP\t", "DATE\t", "URL\n"]
# my_report_file_handle.writelines(L)

# 3) print-function
print("IP", "DATE", "URL", sep="\t", file=my_report_file_handle)

for each_line in log_file_content:
    if each_line.startswith("123"):
        # print("Each Line:", each_line)
        sp = each_line.split()

        ip =sp[0]

        raw_date = sp[3]  # '[26/Apr/2000:00:23:48'
        start_index = 1
        end_index = raw_date.index(":")
        dt = raw_date[start_index:end_index]

        raw_url = sp[10]  # '"http://www.jafsoft.com/asctortf/"'
        url = raw_url[1:-1]

        print(ip, dt, url, sep="\t", file=my_report_file_handle)


print("log_report_3.txt created p,lease check")
my_report_file_handle.close()

print("#"*40, end="\n\n")
#######################