import sqlite3

conn = sqlite3.connect("attendance.db")
# Create a cursor object to interact with the database
cursor = conn.cursor()
cursor.execute('''
Create table attendance (
name varchar(50), 
day varchar(20), 
date date DEFAULT CURRENT_DATE , 
time datetime DEFAULT CURRENT_DATETIME
)
''')


# Close the cursor and the database connection
cursor.close()

conn.close()  

