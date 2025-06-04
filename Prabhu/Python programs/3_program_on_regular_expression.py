"""
Documentation Link:
    1)  https://packaging.python.org/en/latest/tutorials/packaging-projects/
    2) https://docs.python.org/3/library/re.html

Problem Statement:

Get data from website

then

Get log data from html content

then

extract
IP
DATE
URL
using regular expression
"""

print("Get data from website")
print("-"*20)
# ---------------

import urllib.request as u
my_web_file_handle = u.urlopen("http://www.jafsoft.com/searchengines/log_sample.html")
website_content = my_web_file_handle.read()
my_web_file_handle.close()

print(website_content)

print("#"*40, end="\n\n")
#####################

print("Create object of beautifulsoup4 class and store website_content")
print("-"*20)
# ---------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(website_content, "html.parser")
print(soup)

print("#"*40, end="\n\n")
#####################

print("Get log data:")
print("-"*20)
# ---------------

log_data = soup.body.pre.text
print(log_data)

print("#"*40, end="\n\n")
#####################

print("Type of  log data:")
print("-"*20)
# ---------------

print(type(log_data))

print("#"*40, end="\n\n")
#####################


print("log data in raw format:")
print("-"*20)
# ---------------

print(repr(log_data))

print("#"*40, end="\n\n")
#####################

print("Making list of lines")
print("-"*20)
# ---------------

list_of_lines = log_data.splitlines()
print(list_of_lines)

print("#"*40, end="\n\n")
#####################
print("Check whether it is IP address line or not")
print("WITHOUT writing pattern ")
print("-"*20)
# ---------------
import re

for each_line in list_of_lines:
    match_result = re.match('123.123.123.123', each_line) # match is like startswith()
    if match_result is not None:
        print("Each Line:", each_line)
        print("match_result:", match_result)


print("#"*40, end="\n\n")
#####################

print("Check whether it is IP address line or not")
print("USING writing pattern ")
print("-"*20)
# ---------------
import re

for each_line in list_of_lines:
    match_result = re.match(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d', each_line) # match is like startswith()
    if match_result is not None:
        print("Each Line:", each_line)
        print("match_result:", match_result)
        print()

# Regular expressom
r"""
\d -> represent 1 digit
\D -> represent any character except digit
. -> represent any ONE character.
\. -> Strictly DOT

"""


print("#"*40, end="\n\n")
#####################
print("Check whether it is IP address line or not: Specify Quantity")
print("USING writing pattern ")
print("-"*20)
# ---------------
import re

for each_line in list_of_lines:
    match_result = re.match(r'\d{3}.\d{3}\.\d{3}\.\d{3}', each_line) # match is like startswith()
    if match_result is not None:
        print("Each Line:", each_line)
        print("match_result:", match_result)
        print()

# Regular expressom
r"""
\d{3} -> it makes \d\d\d
"""


print("#"*40, end="\n\n")
#####################

print("Check whether it is IP address line or not: Specify Quantity")
print("USING writing pattern ")
print("-"*20)
# ---------------
import re

for each_line in list_of_lines:
    match_result = re.match(r'\d{1,3}.\d{1,3}\.\d{1,3}\.\d{1,3}', each_line) # match is like startswith()
    if match_result is not None:
        print("Each Line:", each_line)
        print("match_result:", match_result)
        print()

# Regular expressom
r"""
\d{1,3} -> it makes One digit OR 2 digits or 3 digits
"""


print("#"*40, end="\n\n")
#####################
print("Extract IP")
print("-"*20)
# ---------------
import re

for each_line in list_of_lines:
    match_result = re.match(r'((\d{1,3}.\d{1,3})\.(\d{1,3}\.\d{1,3}))', each_line) # match is like startswith()
    if match_result is not None:
        # print("Each Line:", each_line)
        # print("match_result:", match_result)
        complete_ip =  match_result.group(1)
        ip_1st_half = match_result.group(2)
        ip_2nd_half = match_result.group(3)

        print("complete_ip:", complete_ip)
        print("ip_1st_half:", ip_1st_half)
        print("ip_2nd_half:", ip_2nd_half)

# Regular expressom
r"""
put () to IP address pattern to capture separately
- this is called group
- we can put multiple () to capture multiple values
- each group will be having index number starting from 1
"""

print("#"*40, end="\n\n")
#####################

print("Extract IP, DATE")
print("-"*20)
# ---------------
import re

for each_line in list_of_lines:
    # match_result = re.match(r'(\d{1,3}.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(\d{2}/[a-zA-Z]{3}/\d{4})', each_line) # match is like startswith()
    # OR use .* to tell 0 or more any characters
    match_result = re.match(r'(\d{1,3}.\d{1,3}\.\d{1,3}\.\d{1,3}).*(\d{2}/[a-zA-Z]{3}/\d{4})', each_line)  # match is like startswith()
    if match_result is not None:
        # print("Each Line:", each_line)
        # print("match_result:", match_result)
        complete_ip =  match_result.group(1)
        complete_date = match_result.group(2)
        print("Cpmpleted IP:", complete_ip)
        print("Cpmpleted date:", complete_date)

# Regular expressom
r"""
Pattern for: 26/Apr/2000

26
-----
\d\d # Strictly 2 digits
\d{2} # Strictly 2 digits
[0-9][0-9] # Strictly 2 digits
[0-9]{2} # Strictly 2 digits
[0-9]\d # Strictly 2 digits
\d[0-9] # Strictly 2 digits

\d{1,2} # Minimum 1 digit, maximum 2 digits
[0-9]{1,2} # Minimum 1 digit, maximum 2 digits
\d?\d # Minimum 1 digit, maximum 2 digits
\d?[0-9] # Minimum 1 digit, maximum 2 digits
[0-9]?\d  # Minimum 1 digit, maximum 2 digits
-----

Apr
----
[A-Z][a-z][a-z]
# OR
[A-Z][a-z]{2}
# OR
[A-Za-z]{3}
# OR
(Jan|Feb|Mar)
[JFMASOND][a-z]{2}


# Difference
[JFMASOND] -> represent, Any ONE character in this group of characters
(JFMASOND) ->exact complete word it will match
----

"""

"""
Modifiers
* -> to tell 0 or more times
+ -> to tell 1 or more times
? -> to tell 0 or 1 time

# Example
abc* -> ab followed by 0 or more times 'c'
(abc)* -> exact 'abc' 0 or more times 'c'
[abc]* -> Any one char in this group, that too 0 or more times
"""

print("#"*40, end="\n\n")
#####################

print("Extract IP, DATE, URL")
print("-"*20)
# ---------------
import re

for each_line in list_of_lines:
    # match_result = re.match(r'(\d{1,3}.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(\d{2}/[a-zA-Z]{3}/\d{4})', each_line) # match is like startswith()
    # OR use .* to tell 0 or more any characters
    match_result = re.match(r'(\d{1,3}.\d{1,3}\.\d{1,3}\.\d{1,3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(http[s]?://[a-zA-Z.0-9/_]+)', each_line)  # match is like startswith()
    if match_result is not None:
        # print("Each Line:", each_line)
        # print("match_result:", match_result)
        complete_ip =  match_result.group(1)
        complete_date = match_result.group(2)
        compte_url = match_result.group(3)
        print("Complete IP:", complete_ip)
        print("Complete date:", complete_date)
        print("Complete URL:", compte_url, end="\n\n")

# Regular expressom
r"""
Pattern for URL : http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF

http[s]?://[a-zA-Z.0-9/_]+

http[s]? -> Here s is optional
https? -> Here also s is optional

"""

print("#"*40, end="\n\n")
#####################