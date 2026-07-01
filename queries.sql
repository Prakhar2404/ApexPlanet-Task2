-- Display first 10 records
SELECT * FROM Sales LIMIT 10;

-- Count total records
SELECT COUNT(*) AS Total_Records
FROM Sales;

-- Calculate average customer age
SELECT AVG(Age) AS Average_Age
FROM Sales;

-- Calculate total revenue
SELECT SUM(Total_Sales) AS Total_Revenue
FROM Sales;

-- Total sales by category
SELECT Category,
SUM(Total_Sales) AS Total_Sales
FROM Sales
GROUP BY Category
ORDER BY Total_Sales DESC;

-- Top 5 products by sales
SELECT Product,
SUM(Total_Sales) AS Sales
FROM Sales
GROUP BY Product
ORDER BY Sales DESC
LIMIT 5;

-- Sales by city
SELECT City,
SUM(Total_Sales) AS Total_Sales
FROM Sales
GROUP BY City
ORDER BY Total_Sales DESC;

-- Revenue by gender
SELECT Gender,
SUM(Total_Sales) AS Revenue
FROM Sales
GROUP BY Gender;