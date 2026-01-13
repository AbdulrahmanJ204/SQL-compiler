CREATE TABLE Customers
(
    CustomerID INT NOT NULL,
    Name NVARCHAR(100) NULL
);

CREATE TABLE Sales.Orders
(
    OrderID INT NOT NULL,
    CustomerID INT NOT NULL,
    OrderDate DATETIME2 NOT NULL,
    TotalAmount DECIMAL(10,2) NOT NULL,
    CONSTRAINT PK_Orders PRIMARY KEY (OrderID),
    CONSTRAINT FK_Orders_Customers FOREIGN KEY (CustomerID)
        REFERENCES Customers (CustomerID),
    CONSTRAINT CK_Orders_TotalAmount CHECK (TotalAmount > 0)
);


CREATE INDEX IX_Customers_Name
ON Customers (Name);

CREATE INDEX IX_Customers_Name_Email
ON dbo.Customers (Name ASC, Email DESC);

CREATE CLUSTERED INDEX IX_Orders_OrderDate
ON SalesDB.dbo.Orders (OrderDate);

CREATE UNIQUE INDEX IX_Customers_Email_Unique
ON dbo.Customers (Email ASC, Country DESC);

CREATE NONCLUSTERED INDEX IX_Orders_CustomerId
ON dbo.Orders (CustomerID)
INCLUDE (OrderDate, TotalAmount);

CREATE NONCLUSTERED INDEX IX_Orders_OpenOrders
ON dbo.Orders (Status)
WHERE Status = 'Open';

CREATE NONCLUSTERED INDEX IX_Orders_TotalAmount
ON dbo.Orders (TotalAmount DESC)
WITH (
    PAD_INDEX = ON,
    FILLFACTOR = 80,
    IGNORE_DUP_KEY = OFF,
    ALLOW_ROW_LOCKS = ON,
    ALLOW_PAGE_LOCKS = OFF
);

CREATE VIEW Sales.CustomerOrderSummary
    (CustomerId, FullName, TotalOrders, TotalAmount)
WITH ENCRYPTION, SCHEMABINDING, VIEW_METADATA
AS
SELECT
    c.Id                           AS CustomerId,
    c.FirstName + ' ' + c.LastName AS FullName,
    COUNT(o.Id)                    AS TotalOrders,
    SUM(o.TotalAmount)             AS TotalAmount
FROM Sales.Customers AS c
LEFT JOIN Sales.Orders AS o
    ON o.CustomerId = c.Id
WHERE c.IsActive = 1
GROUP BY c.Id, c.FirstName, c.LastName
WITH CHECK OPTION;


CREATE USER Mary
FROM LOGIN MaryLogin
WITH DEFAULT_SCHEMA = Sales, DEFAULT_LANGUAGE = English;

CREATE USER [Contoso\Fritz]
FROM LOGIN [Contoso\Fritz]
WITH DEFAULT_SCHEMA = HR, DEFAULT_LANGUAGE = 'en-US';

CREATE USER AppUser
WITH PASSWORD = 'P@ssw0rd!',
     DEFAULT_SCHEMA = dbo,
     DEFAULT_LANGUAGE = 1033;

CREATE USER CustomApp
WITHOUT LOGIN
WITH DEFAULT_SCHEMA = Reporting, DEFAULT_LANGUAGE = NONE;

CREATE USER CarmenW
WITH PASSWORD = 'a8ea v*(Rd##+',
     SID = 0x01050000000000090300000063FF0451A9E7664BA705B10E37DDC4B7;
