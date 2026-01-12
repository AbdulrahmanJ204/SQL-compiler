
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

ALTER USER Mary5 WITH NAME = Mary51;

ALTER USER Mary51 WITH DEFAULT_SCHEMA = Purchasing;

ALTER USER Philip
WITH NAME = Philipe,
     DEFAULT_SCHEMA = Development,
     PASSWORD = 'new' OLD_PASSWORD = 'old',
     DEFAULT_LANGUAGE = French;

ALTER USER Mai
WITH LOGIN = Mai;


ALTER FUNCTION dbo.GetServerDate ()
RETURNS DATETIME
AS
BEGIN
    RETURN GETDATE();
END;

ALTER FUNCTION dbo.AddTax
(
    @amount DECIMAL(10,2),
    @taxRate DECIMAL(5,2) = 15.00
)
RETURNS DECIMAL(10,2)
AS
BEGIN
    RETURN @amount + (@amount * @taxRate / 100);
END;

ALTER FUNCTION dbo.GetActiveOrdersByCustomer
(
    @customerId INT
)
RETURNS TABLE
AS
RETURN
(
    SELECT OrderID, OrderDate, TotalAmount
    FROM Sales.Orders
    WHERE CustomerID = @customerId
      AND Status = 'Active'
);

ALTER FUNCTION dbo.GetHighValueOrders
(
    @minAmount DECIMAL(10,2)
)
RETURNS @Result TABLE
(
    OrderID INT,
    CustomerID INT,
    TotalAmount DECIMAL(10,2)
)
AS
BEGIN
    INSERT INTO @Result (OrderID, CustomerID, TotalAmount)
    SELECT OrderID, CustomerID, TotalAmount
    FROM Sales.Orders
    WHERE TotalAmount >= @minAmount;

    RETURN;
END;

ALTER FUNCTION dbo.FormatName
(
    @firstName NVARCHAR(50) NOT NULL,
    @lastName NVARCHAR(50) NULL = NULL
)
RETURNS NVARCHAR(101)
AS
BEGIN
    RETURN COALESCE(@firstName, '') + N' ' + COALESCE(@lastName, '');
END;
