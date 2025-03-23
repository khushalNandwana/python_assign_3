import sqlite3

conn=sqlite3.connect("student_database.db")
cursor=conn.cursor()

cursor.execute(''' 
       CREATE TABLE IF NOT EXISTS student (
           id INTEGER PRIMARY KEY,
           name TEXT NOT NULL,
           age INTEGER,
           marks REAL
               
     )
''')
student_data = [
    ("khushal", 23, 85.5),
    ("harshita", 24, 75.7),
    ("tanishq", 25, 95.8),
    ("shubham", 22, 77.5),
    ("Golu", 21, 67.6)
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