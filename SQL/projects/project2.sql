
CREATE DATABASE ComputerStore;


USE ComputerStore;

CREATE TABLE Inventory (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Brand VARCHAR(50),
    Price DECIMAL(10,2),
    Quantity INT
);

INSERT INTO Inventory (ProductID, ProductName, Category, Brand, Price, Quantity)
VALUES
(1, 'MacBook Air', 'Laptop', 'Apple', 1599.00, 10),
(2, 'Inspiron 15', 'Laptop', 'Dell', 999.00, 15),
(3, 'Galaxy Book', 'Laptop', 'Samsung', 1199.00, 8),
(4, 'iPhone 16', 'Phone', 'Apple', 1399.00, 20),
(5, 'Galaxy S25', 'Phone', 'Samsung', 1299.00, 12),
(6, 'Wireless Mouse', 'Accessory', 'Logitech', 49.00, 30),
(7, 'Mechanical Keyboard', 'Accessory', 'Razer', 129.00, 18),
(8, 'Gaming Monitor', 'Monitor', 'LG', 499.00, 7);


SELECT * FROM Inventory;


SELECT * FROM Inventory
WHERE Quantity < 10;


SELECT * FROM Inventory
WHERE Category = 'Laptop';


SELECT * FROM Inventory
ORDER BY Price DESC
LIMIT 1;


SELECT * FROM Inventory
ORDER BY Price ASC
LIMIT 1;


SELECT SUM(Price * Quantity) AS TotalInventoryValue
FROM Inventory;

SELECT AVG(Price) AS AveragePrice
FROM Inventory;

SELECT COUNT(*) AS TotalProducts
FROM Inventory;


SELECT * FROM Inventory
ORDER BY Price DESC;

UPDATE Inventory
SET Quantity = Quantity + 5
WHERE ProductID = 1;


UPDATE Inventory
SET Price = 1499.00
WHERE ProductID = 1;


DELETE FROM Inventory
WHERE ProductID = 8;

SELECT * FROM Inventory;