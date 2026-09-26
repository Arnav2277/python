
CREATE DATABASE MarineLifeExplorer;


USE MarineLifeExplorer;


CREATE TABLE Observations (
    ObservationID INT PRIMARY KEY,
    SpeciesName VARCHAR(100),
    Category VARCHAR(50),
    Location VARCHAR(100),
    ObservationDate DATE,
    DepthMeters INT,
    NumberObserved INT
);


INSERT INTO Observations
(ObservationID, SpeciesName, Category, Location, ObservationDate, DepthMeters, NumberObserved)
VALUES
(1, 'Bottlenose Dolphin', 'Mammal', 'Bay of Islands', '2026-01-15', 20, 8),
(2, 'Great White Shark', 'Shark', 'Chatham Islands', '2026-02-10', 45, 2),
(3, 'Blue Penguin', 'Bird', 'Wellington', '2026-03-05', 5, 12),
(4, 'Humpback Whale', 'Mammal', 'Kaikoura', '2026-03-18', 30, 5),
(5, 'Giant Kelp', 'Plant', 'Fiordland', '2026-04-02', 10, 25),
(6, 'Common Octopus', 'Mollusc', 'Poor Knights Islands', '2026-04-15', 18, 4),
(7, 'Yellow-Eyed Penguin', 'Bird', 'Otago Peninsula', '2026-05-01', 3, 7),
(8, 'Blue Shark', 'Shark', 'Hauraki Gulf', '2026-05-12', 35, 6),
(9, 'Orca', 'Mammal', 'Hauraki Gulf', '2026-06-08', 15, 9),
(10, 'Sea Turtle', 'Reptile', 'Bay of Islands', '2026-06-20', 12, 3);

SELECT * FROM Observations;


SELECT * FROM Observations
WHERE Category = 'Mammal';


SELECT * FROM Observations
WHERE DepthMeters > 20;


SELECT * FROM Observations
WHERE NumberObserved > 5;


SELECT * FROM Observations
ORDER BY DepthMeters DESC;


SELECT * FROM Observations
ORDER BY DepthMeters DESC
LIMIT 1;


SELECT * FROM Observations
ORDER BY DepthMeters ASC
LIMIT 1;

SELECT COUNT(*) AS TotalObservations
FROM Observations;


SELECT SUM(NumberObserved) AS TotalAnimals
FROM Observations;


SELECT AVG(DepthMeters) AS AverageDepth
FROM Observations;


SELECT Category, COUNT(*) AS NumberOfObservations
FROM Observations
GROUP BY Category;


SELECT Category, COUNT(*) AS NumberOfObservations
FROM Observations
GROUP BY Category
HAVING COUNT(*) > 1;


UPDATE Observations
SET NumberObserved = 10
WHERE ObservationID = 1;


DELETE FROM Observations
WHERE ObservationID = 10;


SELECT * FROM Observations;