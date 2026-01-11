

DELETE FROM Customers;
DELETE Customers WHERE Id = 10;
DELETE TOP (10) FROM dbo.Customers;
DELETE TOP (5) PERCENT FROM dbo.Customers WHERE City = 'Chicago';
DELETE spqh FROM Sales.SalesPersonQuotaHistory AS spqh INNER JOIN Sales.SalesPerson AS sp ON spqh.BusinessEntityID = sp.BusinessEntityID WHERE sp.SalesYTD > 2500000.00;

DELETE FROM Sales.SalesPersonQuotaHistory;

DELETE Sales.SalesPersonQuotaHistory;

DELETE Production.ProductCostHistory
WHERE StandardCost > MaxStandardCost;

DELETE Production.ProductCostHistory
WHERE StandardCost BETWEEN MinCost AND MaxCost
  AND EndDate IS NULL;

DELETE Production.ProductCostHistory
WHERE ProductCode IN (CodeA, CodeB, CodeC);

DELETE Production.ProductCostHistory
WHERE EndDate IS NOT NULL;

DELETE FROM HumanResources.EmployeePayHistory
WHERE CURRENT OF complex_cursor;

DELETE TOP (10)
FROM Purchasing.PurchaseOrderDetail
WHERE DueDate < OldestDueDate;


DELETE TOP (5) PERCENT
FROM Purchasing.PurchaseOrderDetail
WHERE DueDate < OldestDueDate;

DELETE FROM Sales.SalesPersonQuotaHistory
FROM Sales.SalesPersonQuotaHistory AS spqh
INNER JOIN Sales.SalesPerson AS sp
  ON spqh.BusinessEntityID = sp.BusinessEntityID
WHERE sp.SalesYTD > TargetSales;

DELETE FROM Sales.SalesPersonQuotaHistory
FROM Sales.SalesPersonQuotaHistory AS spqh
JOIN Sales.SalesPerson AS sp
  ON spqh.BusinessEntityID = sp.BusinessEntityID
WHERE sp.SalesYTD > TargetSales;

DELETE FROM dbo.BigTable
FROM dbo.BigTable AS bt
INNER JOIN dbo.OtherTable AS ot
  ON bt.Id = ot.Id
WHERE (bt.Flag IS NULL OR bt.Flag IS NOT NULL)
  AND bt.ColA IN (Val1, Val2)
  AND bt.ColB BETWEEN LowerBound AND UpperBound;
DELETE Sales.ShoppingCartItem
OUTPUT DELETED.*
WHERE ShoppingCartID = 20621;