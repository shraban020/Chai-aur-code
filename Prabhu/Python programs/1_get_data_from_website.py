"""
Get data from website and print
"""

print("Get data from website and print")
print("-"*20)
# ---------------

import urllib.request as u
website_file_handle = u.urlopen("http://www.python.org")
web_content = website_file_handle.read()
website_file_handle.close()

print(web_content)

print("#"*40, end="\n\n")
#####################

print("type of web_content:")
print("-"*20)
# ---------------

print("type of web_content:", type(web_content))

print("#"*40, end="\n\n")
#####################

print("Methods present in bytes class")
print("-"*20)
# ---------------

print(dir(bytes))

print("#"*40, end="\n\n")
#####################4