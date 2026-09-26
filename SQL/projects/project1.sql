
CREATE DATABASE SchoolDB;

USE SchoolDB;


CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Class VARCHAR(20),
    Marks INT
);


INSERT INTO Students (StudentID, Name, Age, Class, Marks)
VALUES
(1, 'Arnav', 14, '10A', 85),
(2, 'Rahul', 14, '10A', 92),
(3, 'Rohan', 15, '10B', 78),
(4, 'Aman', 14, '10B', 88),
(5, 'Karan', 15, '10A', 95);


SELECT * FROM Students;


SELECT * FROM Students
WHERE Marks > 80;


SELECT * FROM Students
ORDER BY Marks DESC;

SELECT AVG(Marks) AS AverageMarks
FROM Students;


SELECT MAX(Marks) AS HighestMarks
FROM Students;


SELECT COUNT(*) AS TotalStudents
FROM Students;