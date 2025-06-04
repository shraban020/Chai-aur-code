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
print("Create object of beautifulsoup4 class and store website_content")
print("-"*20)
# ---------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(website_content, "html.parser")
print(soup)

print("#"*40, end="\n\n")
#####################

print("METHODS present inside BeautifulSoup class")
print("-"*20)
# ---------------

print(dir(soup))

print("#"*40, end="\n\n")
#####################

print("Only head tag")
print("-"*20)
# ---------------

head_tag = soup.head
print(head_tag)

print("#"*40, end="\n\n")
#####################


print("Only body tag")
print("-"*20)
# ---------------

body_tag = soup.body
print(body_tag)

print("#"*40, end="\n\n")
#####################
print("Title Tag: 1-way")
print("-"*20)
# ---------------

title_tag = soup.title
print(title_tag)

print("#"*40, end="\n\n")
#####################

print("Title Tag: 2-way")
print("-"*20)
# ---------------

title_tag = soup.head.title # <title>A Web server log file explained</title>
print(title_tag)

print("#"*40, end="\n\n")
#####################

print("Title Tag: Content")
print("-"*20)
# ---------------

title_tag_text = soup.head.title.text # A Web server log file explained
print(title_tag_text)

print("#"*40, end="\n\n")
#####################
print("1st Link Tag: 1-way")
print("-"*20)
# ---------------

link_tag = soup.link # <LINK REL="StyleSheet" HREF="../style.css" TYPE="text/css">
print("1st link tag:", link_tag)


print("#"*40, end="\n\n")
#####################

print("1st Link Tag: 2-way")
print("-"*20)
# ---------------

link_tag = soup.head.link # <LINK REL="StyleSheet" HREF="../style.css" TYPE="text/css">
print("1st link tag:", link_tag)

print("#"*40, end="\n\n")
#####################

print("1st Link Tag: Attributes")
print("-"*20)
# ---------------

link_tag = soup.head.link # <LINK REL="StyleSheet" HREF="../style.css" TYPE="text/css">
print("1st link tag:", link_tag)

print("rel:", link_tag.get("rel"))
print("href:", link_tag.get("href"))
print("type:", link_tag.get("type"))

print("#"*40, end="\n\n")
#####################
print("All paragraph tags")
print("-"*20)
# ---------------

all_paragraph_tags = soup.find_all('p')
print(all_paragraph_tags)

print("#"*40, end="\n\n")
#####################

print("Comprehension: list/tuple/set/dictionary")
print("We can write one line expression in list/tuple/set/dictionary")
print("-"*20)
# ---------------

L = [10, 20, 30, 40, 50]
square_L = [i*i for i in L]
print(square_L)

print("#"*40, end="\n\n")
#####################

print("All paragraphs content")
print("-"*20)
# ---------------

all_paragraph_contents = [each_p_tag.text        for each_p_tag in all_paragraph_tags]
print(all_paragraph_contents)

print("#"*40, end="\n\n")
#####################

print("all anchor/url tags")
print("-"*20)
# ---------------

all_url_tags = soup.find_all('a')
print(all_url_tags)

print("#"*40, end="\n\n")
#####################

print("all urls")
print("-"*20)
# ---------------

all_urls = [each_a_tag.get("href")        for each_a_tag in all_url_tags]
print(all_urls)

print("#"*40, end="\n\n")
#####################


print("all urls WITHOUT None values")
print("-"*20)
# ---------------

all_urls = [each_url        for each_url in all_urls       if each_url is not None]
print(all_urls)

print("#"*40, end="\n\n")
###################### ---------------
# json file
# ---------------
# - We can write data present in int, float, string, list, tuple, dictionary to json file
# - other type like set, frozenset, convert to list/tuple then write to json file
#####################

print("Prepare dictionary")
print("-"*20)
# ---------------

my_dictionary = {}
my_dictionary["all_paragraphs"] = all_paragraph_contents
my_dictionary["all_urls"] = all_urls
print(my_dictionary)

print("#"*40, end="\n\n")
#####################

print("Write to web_scrape_report.json")
print("-"*20)
# ---------------

my_file_handle = open(file="web_scrape_report.json", mode="w")
# mode 'w' will create new file

# Documentation: https://docs.python.org/3/library/json.html
import json
json.dump(my_dictionary, my_file_handle) # dump is write to file

my_file_handle.close()

print("Created web_scrape_report.json, Please check")

print("#"*40, end="\n\n")
#####################