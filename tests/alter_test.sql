
ALTER TABLE Sales.Orders
    ALTER COLUMN OrderDate DATETIME2 NOT NULL;

ALTER TABLE Sales.Orders
    ADD Discount DECIMAL(5,2) NULL;

ALTER TABLE Sales.Orders
    ADD CONSTRAINT PK_Orders PRIMARY KEY (OrderID);

ALTER TABLE employees
    RENAME COLUMN emp_name TO employee_name;

ALTER TABLE employees
    ALTER COLUMN salary DECIMAL(10,2) NOT NULL,
    ADD bonus DECIMAL(5,2) NULL;

ALTER INDEX IX_Orders_Date
    ON Sales.Orders
    REBUILD;

ALTER INDEX IX_Orders_Date
    ON Sales.Orders
    REBUILD WITH (
        FILLFACTOR = 80,
        SORT_IN_TEMPDB = ON,
        ONLINE = OFF,
        MAXDOP = 4
    );

ALTER INDEX IX_Orders_Date
    ON Sales.Orders
    REORGANIZE WITH (LOB_COMPACTION = ON);

ALTER INDEX IX_Orders_Date
    ON Sales.Orders
    DISABLE;

ALTER INDEX IX_Orders_Old
    ON Sales.Orders
    RENAME TO IX_Orders_New;

ALTER INDEX ALL
    ON Sales.Orders
    REBUILD;


ALTER VIEW Sales.ActiveOrders
AS
SELECT OrderID, CustomerID, OrderDate
FROM Sales.Orders
WHERE Status = 'Active';

ALTER VIEW dbo.CustomerSummary (CustomerID, TotalOrders, LastOrderDate)
AS
SELECT c.CustomerID,
       COUNT(o.OrderID) AS TotalOrders,
       MAX(o.OrderDate) AS LastOrderDate
FROM dbo.Customers c
LEFT JOIN dbo.Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID;

ALTER VIEW dbo.HighValueOrders
AS
SELECT OrderID, CustomerID, TotalAmount
FROM dbo.Orders
WHERE TotalAmount > 1000
WITH CHECK OPTION;

ALTER VIEW dbo.RecentOrders (OrderID, OrderDate, CustomerID)
AS
SELECT OrderID, OrderDate, CustomerID
FROM dbo.Orders
WHERE OrderDate >= '2025-01-01'
WITH CHECK OPTION;
