

DELETE FROM Customers;
DELETE Customers WHERE Id = 10;  
DELETE TOP (10) FROM dbo.Customers;
DELETE TOP (5) PERCENT FROM dbo.Customers WHERE City = 'Chicago';
DELETE spqh FROM Sales.SalesPersonQuotaHistory AS spqh INNER JOIN Sales.SalesPerson AS sp ON spqh.BusinessEntityID = sp.BusinessEntityID WHERE sp.SalesYTD > 2500000.00;