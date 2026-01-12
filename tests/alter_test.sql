
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
