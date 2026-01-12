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
