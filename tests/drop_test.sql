DROP TABLE ProductVendor1;
DROP TABLE AdventureWorks2022.dbo.SalesPerson2 ;

CREATE TABLE #temptable (col1 int);

INSERT INTO #temptable
VALUES (10);

SELECT col1 FROM #temptable;

IF OBJECT_ID(N'tempdb..#temptable', N'U') IS NOT NULL
  DROP TABLE #temptable;

SELECT col1 FROM #temptable;

DROP TABLE T1;

DROP TABLE IF EXISTS T1;

