CREATE DATABASE college;

USE college;

CREATE TABLE student (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  age INT NOT NULL,
  marks INT NOT NULL
);

INSERT INTO student VALUES(1, "KHUSHAL", 23, 98);
INSERT INTO student VALUES(2, "NIDHI", 22, 78);
INSERT INTO student VALUES(3, "HARDIK", 24, 88);
INSERT INTO student VALUES(4, "AYUSH", 25, 66);
INSERT INTO student VALUES(5, "SNEHA", 21, 75);

SELECT * FROM  student;

UPDATE student SET marks = 95 WHERE id = 5;

DELETE FROM student WHERE id = 5;

SELECT * FROM student;
