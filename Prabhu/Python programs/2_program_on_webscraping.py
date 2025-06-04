"""
Web scraping using BeautifulSoup library
Documentation Link: https://pypi.org/project/beautifulsoup4/
Urllib Documentation: https://docs.python.org/3/library/urllib.request.html

Requirement:
Get data form website and parse,
finally get log data present in website

How to install?
    pip install beautifulsoup4
"""
print("Get data from website")
print("-"*20)
# ---------------

import urllib.request as u
my_web_file_handle = u.urlopen("https://www.jafsoft.com/searchengines/log_sample.html")
website_content = my_web_file_handle.read()
my_web_file_handle.close()

print(website_content)

print("#"*40, end="\n\n")
#####################