import sqlite3
conn=sqlite3.connect("student_database.db")
cursor=conn.cursor()

cursor.execute(''' 
       CREATE TABLE student 
(
               id INT PRIMARY KEY,
               name VARCHAR(50),
               age INT NOT NULL,
               marks INT NOT NULL
               
               
     )
''')
student_data = [
    ("khushal", 23, 85),
    ("harshita", 24, 75),
    ("tanishq", 25, 95),
    ("shubham", 22, 77),
    ("Golu", 21, 67)
]

cursor.executemany("INSERT INTO student (name, age, marks) VALUES (?, ?, ?)",student_data)
conn.commit()

print("all student records:")
cursor.execute("SELECT * FROM student")
for row in cursor.fetchall():
    print(row)

cursor.execute("UPDATE student SET marks = 83 WHERE name = 'khushal'")
conn.commit()

cursor.execute("DELETE FROM student WHERE id = 3")
conn.commit()

print("\nNew student record:")
cursor.execute("SELECT * FROM student")
for row in cursor.fetchall():
    print(row)
conn.close()