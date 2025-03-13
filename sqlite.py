import sqlite3

## Connect to sqlite
connection = sqlite3.connect('student.db')

## Create a cursor object to insert records and create table
cursor = connection.cursor()

## Create the table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

## Insert some more records
cursor.execute('''INSERT INTO STUDENT VALUES('Ashutosh', 'Artificial Intelligence', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Komal', 'Intelligence', 'D', 36)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Lion', 'Beard', 'L', 105)''') # 5 marks for good handwriting
cursor.execute('''INSERT INTO STUDENT VALUES('Bauff', 'Tail', 'T', 20)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Gendu', 'GotHisNose', 'G', 75)''')

## Display all the records
print("The inserted records are:")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()