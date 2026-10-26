
CREATE TABLE IF NOT EXISTS Activities (
    activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    activity_name TEXT NOT NULL,
    category TEXT NOT NULL,
    instructor TEXT NOT NULL,
    day TEXT NOT NULL,
    cost REAL NOT NULL,
    participants INTEGER NOT NULL
);


INSERT INTO Activities
(activity_name, category, instructor, day, cost, participants)
VALUES
('Football', 'Sports', 'Mr James', 'Monday', 5.00, 20),
('Basketball', 'Sports', 'Mr Smith', 'Tuesday', 4.00, 15),
('Painting', 'Arts', 'Mrs Brown', 'Wednesday', 8.00, 12),
('Dance', 'Fitness', 'Ms Taylor', 'Thursday', 6.00, 18),
('Coding', 'Technology', 'Mr Wilson', 'Friday', 10.00, 10),
('Yoga', 'Fitness', 'Mrs Green', 'Saturday', 7.00, 14),
('Guitar', 'Music', 'Mr Davis', 'Monday', 9.00, 8);


SELECT * FROM Activities;


SELECT *
FROM Activities
WHERE activity_name = 'Football';

SELECT *
FROM Activities
WHERE category = 'Sports';

SELECT activity_name, cost
FROM Activities
WHERE cost < 7;

SELECT activity_name, cost
FROM Activities
ORDER BY cost ASC;


SELECT COUNT(*) AS total_activities
FROM Activities;


SELECT AVG(cost) AS average_cost
FROM Activities;


SELECT activity_name, participants
FROM Activities
ORDER BY participants DESC
LIMIT 1;


SELECT category, COUNT(*) AS total_activities
FROM Activities
GROUP BY category;


SELECT category, COUNT(*) AS total_activities
FROM Activities
GROUP BY category
HAVING COUNT(*) > 1;


SELECT SUM(participants) AS total_participants
FROM Activities;


SELECT *
FROM Activities
WHERE instructor LIKE '%Smith%';


SELECT *
FROM Activities
WHERE day = 'Monday';


SELECT *
FROM Activities
WHERE cost BETWEEN 5 AND 9;


UPDATE Activities
SET cost = 6.00
WHERE activity_name = 'Football';


INSERT INTO Activities
(activity_name, category, instructor, day, cost, participants)
VALUES
('Swimming', 'Sports', 'Mr Lee', 'Sunday', 8.00, 16);


SELECT *
FROM Activities
WHERE participants >= 15
ORDER BY participants DESC;

SELECT * FROM Activities
ORDER BY activity_name ASC;
