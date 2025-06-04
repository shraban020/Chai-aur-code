"""
Get data from database and print
"""
print("Get data from database and print")
print("-"*20)
# ---------------

import sqlite3

my_db_connection = sqlite3.connect("mydatabase.db")
my_cursor = my_db_connection.cursor()
my_cursor.execute("SELECT * FROM MYTABLE")
my_db_result = my_cursor.fetchall()
print(my_db_result)

print("#"*40, end="\n\n")
#####################
