"""
Write a function for log process activity

Final requirement is:
Example:
    log_file_1_data = log_process_function("log_file_1.txt")
    log_file_1_data = [[ip, dt, url],[ip, dt, url],[ip, dt, url],]

    log_file_2_data = log_process_function("log_file_2.txt")
    log_file_2_data = [[ip, dt, url],[ip, dt, url],[ip, dt, url],]

    log_file_3_data = log_process_function("log_file_3.txt")
    log_file_3_data = [[ip, dt, url],[ip, dt, url],[ip, dt, url],]
"""

print("Writing Function")
print("-"*20)
# --------------

def log_process_function(log_file_name):
    """
    This function will take log file path as an argument,
    then it will extract data from it and return a list of lists.
    :param log_file_name:
    :return list of lists:
    """

    log_file_handle = open(file=log_file_name, mode="r")
    log_file_content = log_file_handle.readlines()
    log_file_handle.close()

    my_list = []
    for each_line in log_file_content:
        if each_line.startswith("123"):
            # print("Each Line:", each_line)
            sp = each_line.split()

            ip = sp[0]

            raw_date = sp[3]  # '[26/Apr/2000:00:23:48'
            start_index = 1
            end_index = raw_date.index(":")
            dt = raw_date[start_index:end_index]

            raw_url = sp[10]  # '"http://www.jafsoft.com/asctortf/"'
            url = raw_url[1:-1]

            each_line_list = [ip, dt, url]
            my_list.append(each_line_list)
    return my_list

print("#"*40, end="\n\n")
#######################

print("Testing Function")
print("-"*20)
# --------------

extracted_data = log_process_function("sample_data.log")
print("extracted_data:", extracted_data)

print("#"*40, end="\n\n")
#######################