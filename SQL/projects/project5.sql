

CREATE TABLE IF NOT EXISTS Students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    year_level INTEGER NOT NULL,
    class_name TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS Subjects (
    subject_id INTEGER PRIMARY KEY,
    subject_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    marks INTEGER NOT NULL CHECK (marks BETWEEN 0 AND 100),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
);


INSERT INTO Students VALUES
(1, 'Arjun', 10, '10A'),
(2, 'Rahul', 10, '10B'),
(3, 'Sam', 10, '10A'),
(4, 'Alex', 10, '10C'),
(5, 'Jay', 10, '10B');



INSERT INTO Subjects VALUES
(1, 'Mathematics'),
(2, 'Science'),
(3, 'English'),
(4, 'Computing'),
(5, 'Social Studies');



INSERT INTO Results (student_id, subject_id, marks)
VALUES
(1, 1, 85),
(1, 2, 90),
(1, 3, 78),
(1, 4, 95),
(1, 5, 82),
(2, 1, 72),
(2, 2, 80),
(2, 3, 75),
(2, 4, 88),
(2, 5, 70),
(3, 1, 92),
(3, 2, 86),
(3, 3, 89),
(3, 4, 94),
(3, 5, 91),
(4, 1, 65),
(4, 2, 70),
(4, 3, 68),
(4, 4, 75),
(4, 5, 72),
(5, 1, 80),
(5, 2, 83),
(5, 3, 85),
(5, 4, 79),
(5, 5, 88);


SELECT * FROM Students;


SELECT * FROM Subjects;


SELECT
    Students.student_name,
    Subjects.subject_name,
    Results.marks
FROM Results
JOIN Students
    ON Results.student_id = Students.student_id
JOIN Subjects
    ON Results.subject_id = Subjects.subject_id
ORDER BY Students.student_name;

SELECT *
FROM Students
WHERE student_name = 'Arjun';


SELECT
    Students.student_name,
    Subjects.subject_name,
    Results.marks
FROM Results
JOIN Students
    ON Results.student_id = Students.student_id
JOIN Subjects
    ON Results.subject_id = Subjects.subject_id
WHERE Results.marks > 80
ORDER BY Results.marks DESC;



SELECT
    Students.student_name,
    ROUND(AVG(Results.marks), 2) AS average_marks
FROM Students
JOIN Results
    ON Students.student_id = Results.student_id
GROUP BY Students.student_id, Students.student_name
ORDER BY average_marks DESC;

SELECT
    Students.student_name,
    Subjects.subject_name,
    MAX(Results.marks) AS highest_mark
FROM Results
JOIN Students
    ON Results.student_id = Students.student_id
JOIN Subjects
    ON Results.subject_id = Subjects.subject_id
WHERE Results.marks = (SELECT MAX(marks) FROM Results);



SELECT
    Students.student_name,
    Subjects.subject_name,
    Results.marks
FROM Results
JOIN Students
    ON Results.student_id = Students.student_id
JOIN Subjects
    ON Results.subject_id = Subjects.subject_id
WHERE Results.marks = (SELECT MIN(marks) FROM Results);


SELECT COUNT(*) AS total_students
FROM Students;

SELECT
    Subjects.subject_name,
    ROUND(AVG(Results.marks), 2) AS subject_average
FROM Subjects
JOIN Results
    ON Subjects.subject_id = Results.subject_id
GROUP BY Subjects.subject_id, Subjects.subject_name
ORDER BY subject_average DESC;


SELECT COUNT(*) AS high_scores
FROM Results
WHERE marks >= 80;

INSERT INTO Students
(student_id, student_name, year_level, class_name)
VALUES (6, 'Chris', 10, '10A');


INSERT INTO Results (student_id, subject_id, marks)
VALUES (6, 1, 87);



UPDATE Results
SET marks = 91
WHERE student_id = 1
AND subject_id = 1;



SELECT *
FROM Students
WHERE class_name = '10A';

SELECT
    Students.student_name,
    Subjects.subject_name,
    Results.marks
FROM Results
JOIN Students
    ON Results.student_id = Students.student_id
JOIN Subjects
    ON Results.subject_id = Subjects.subject_id
WHERE Results.marks >= 50;

SELECT
    Students.student_name,
    Subjects.subject_name,
    Results.marks
FROM Results
JOIN Students
    ON Results.student_id = Students.student_id
JOIN Subjects
    ON Results.subject_id = Subjects.subject_id
WHERE Results.marks < 50;

SELECT
    Students.student_name,
    Students.class_name,
    COUNT(Results.result_id) AS subjects_completed,
    ROUND(AVG(Results.marks), 2) AS average_marks,
    MAX(Results.marks) AS highest_mark,
    MIN(Results.marks) AS lowest_mark
FROM Students
LEFT JOIN Results
    ON Students.student_id = Results.student_id
GROUP BY Students.student_id, Students.student_name, Students.class_name
ORDER BY average_marks DESC;
