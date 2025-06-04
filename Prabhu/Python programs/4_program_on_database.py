"""
Documentation Link:


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

then

write to database
"""

"""
How to communicate with database in python?
python-program  <--communicate using library--> Any databases

Example:
python-program  <--communicate using library(cx-oracle)--> Oracle databases
python-program  <--communicate using library(mysql.connector)--> MySQL databases
python-program  <--communicate using library(sqlite3)--> SQLite databases
"""

"""
We need one database..
- We can make use of SQLite database
- Lightweight databse
- It is serveless database, it will just create one db file and we can execute query on that db.
"""

"""
How to create/communicate with SQLite database
2 ways
1-way: Using sqlite database software
2-way: WITHOUT Using sqlite database software,
    using library sqlite3, we can create and communicate with database
    """


"""
Documentation: https://docs.python.org/3/library/sqlite3.html
"""

print("Create database and table")
print("-"*20)
# ---------------
import sqlite3

print("Creating/connecting to database")
my_db_connection = sqlite3.connect("mydatabase.db")
print("Done\n")

print("In order to execute query, we need cursor object")
my_db_cursor = my_db_connection.cursor()
print("Done\n")

print("Creating table if not present")
my_sql_query = """create table if not exists mytable(
                    IP VARCHAR(100),
                    DATE VARCHAR(100),
                    URL VARCHAR(100)
                  )
                """
my_db_cursor.execute(my_sql_query)
print("Done\n")

print("#"*40, end="\n\n")
#####################
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

print("Making list of lines")
print("-"*20)
# ---------------

list_of_lines = log_data.splitlines()
print(list_of_lines)

print("#"*40, end="\n\n")
#####################

print("Extract IP, DATE, URL and write to database")
print("-"*20)
# ---------------
import re

for each_line in list_of_lines:
    match_result = re.match(r'(\d{1,3}.\d{1,3}\.\d{1,3}\.\d{1,3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(http[s]?://[a-zA-Z.0-9/_]+)', each_line)  # match is like startswith()
    if match_result is not None:
        ip =  match_result.group(1)
        dt = match_result.group(2)
        url = match_result.group(3)

        my_sql_query = f"INSERT INTO MYTABLE VALUES('{ip}', '{dt}', '{url}')"
        print("Executing query:", my_sql_query)
        my_db_cursor.execute(my_sql_query)
        print("One record inserted")

my_db_connection.commit()
print("All records inserted to database")
my_db_connection.close()
print(":DB connection closed")

print("#"*40, end="\n\n")
#####################