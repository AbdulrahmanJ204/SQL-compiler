-- =============================================================================
-- T-SQL TRUNCATE TABLE Test File for Parser and AST Testing
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Basic TRUNCATE Statements
-- -----------------------------------------------------------------------------

-- Simple truncate
TRUNCATE TABLE Orders;

-- Truncate with schema qualifier
TRUNCATE TABLE dbo.Customers;

-- Truncate with database and schema qualifier
TRUNCATE TABLE MyDatabase.dbo.Products;

-- Truncate with brackets (quoted identifiers)
TRUNCATE TABLE [Order Details];

-- Truncate with fully qualified name and brackets
TRUNCATE TABLE [MyDatabase].[dbo].[Customer Orders];

-- -----------------------------------------------------------------------------
-- TRUNCATE with Partitions (SQL Server 2016+)
-- -----------------------------------------------------------------------------

-- Truncate specific partition
TRUNCATE TABLE Sales.SalesOrderDetail
WITH (PARTITIONS (1));

-- Truncate multiple partitions
TRUNCATE TABLE Sales.SalesOrderDetail
WITH (PARTITIONS (1, 2, 3));

-- Truncate partition range
TRUNCATE TABLE Sales.SalesOrderDetail
WITH (PARTITIONS (1 TO 5));

-- Truncate mixed partitions and ranges
TRUNCATE TABLE Sales.SalesOrderDetail
WITH (PARTITIONS (1, 3, 5 TO 10, 12));

-- Truncate with schema-qualified table and partitions
TRUNCATE TABLE [Sales].[SalesOrderDetail]
WITH (PARTITIONS (1 TO 100));

-- -----------------------------------------------------------------------------
-- Edge Cases and Variations
-- -----------------------------------------------------------------------------

-- Truncate with extra whitespace
TRUNCATE    TABLE    dbo.TestTable;

-- Truncate with newlines
TRUNCATE TABLE
    dbo.MultiLineTable;

-- Truncate with tab characters
TRUNCATE	TABLE	dbo.TabTable;

-- Multiple truncates in sequence
TRUNCATE TABLE Table1;
TRUNCATE TABLE Table2;
TRUNCATE TABLE Table3;

-- TODO : add transactions
-- Truncate in transaction
--BEGIN TRANSACTION;
--    TRUNCATE TABLE dbo.LogTable;
--COMMIT TRANSACTION;

-- Truncate with GO batch separator
TRUNCATE TABLE Batch1;
GO
TRUNCATE TABLE Batch2;
GO

-- -----------------------------------------------------------------------------
-- Complex Identifier Names
-- -----------------------------------------------------------------------------

-- Table with special characters
TRUNCATE TABLE [Table-With-Dashes];

-- Table with spaces
TRUNCATE TABLE [Table With Spaces];

-- Table with numbers
TRUNCATE TABLE [Table123];

-- Schema with special characters
TRUNCATE TABLE [my-schema].[my-table];

-- Unicode identifiers
TRUNCATE TABLE [Таблица];

-- Very long identifier (max 128 chars in SQL Server)
TRUNCATE TABLE [ThisIsAVeryLongTableNameThatIsUsedToTestTheParserHandlingOfLongIdentifiersWhichCanBeUpTo128CharactersInSQLServerDatabases];

-- -----------------------------------------------------------------------------
-- Conditional and Procedural Context
-- -----------------------------------------------------------------------------

-- Truncate in IF statement
IF EXISTS (SELECT 1 FROM sys.tables WHERE name = 'TempTable')
    TRUNCATE TABLE TempTable;

-- Truncate in stored procedure
CREATE PROCEDURE ClearStagingTables
AS
BEGIN
    TRUNCATE TABLE Staging.Table1;
    TRUNCATE TABLE Staging.Table2;
END;
GO

-- Truncate in dynamic SQL
DECLARE @TableName NVARCHAR(128) = 'MyTable';
DECLARE @SQL NVARCHAR(MAX) = 'TRUNCATE TABLE ' + @TableName;
EXEC sp_executesql @SQL;

-- -----------------------------------------------------------------------------
-- Comments and Mixed Content
-- -----------------------------------------------------------------------------

-- Single line comment before truncate
-- This truncates the orders table
TRUNCATE TABLE Orders;

/* Multi-line comment before truncate
   This will remove all data from customers
*/
TRUNCATE TABLE Customers;

-- Inline comment
TRUNCATE TABLE Products; -- Clear all products

/* Block comment in between */
TRUNCATE /* removing data */ TABLE Sales;

-- -----------------------------------------------------------------------------
-- Case Variations
-- -----------------------------------------------------------------------------

-- Lowercase
truncate table lowercase_table;

-- Mixed case
TrUnCaTe TaBlE MixedCase;

-- Uppercase (standard)
TRUNCATE TABLE UPPERCASE_TABLE;

-- -----------------------------------------------------------------------------
-- Schema Variations
-- -----------------------------------------------------------------------------

TRUNCATE TABLE sys.error_log;
TRUNCATE TABLE INFORMATION_SCHEMA.TestView; -- This would fail but tests parser
TRUNCATE TABLE ##GlobalTempTable; -- Global temp table
TRUNCATE TABLE #LocalTempTable; -- Local temp table

-- -----------------------------------------------------------------------------
-- Complex Partition Scenarios
-- -----------------------------------------------------------------------------

-- Single partition
TRUNCATE TABLE Sales.Orders WITH (PARTITIONS (10));

-- All partitions explicitly
TRUNCATE TABLE Sales.Orders
WITH (PARTITIONS (1, 2, 3, 4, 5, 6, 7, 8, 9, 10));

-- Multiple ranges
TRUNCATE TABLE Sales.Orders
WITH (PARTITIONS (1 TO 10, 15 TO 20, 25, 30 TO 35));

-- Large partition numbers
TRUNCATE TABLE Sales.Orders WITH (PARTITIONS (1000 TO 9999));

-- -----------------------------------------------------------------------------
-- Error-Prone Scenarios (for robust parser testing)
-- -----------------------------------------------------------------------------

-- Missing semicolon (should still parse)
TRUNCATE TABLE NoSemicolon

-- Extra semicolons
TRUNCATE TABLE ExtraSemicolons;;;

-- Truncate with trailing comma (invalid but tests error handling)
-- TRUNCATE TABLE InvalidTable,;

-- -----------------------------------------------------------------------------
-- Real-World Patterns
-- -----------------------------------------------------------------------------

-- ETL cleanup pattern
TRUNCATE TABLE Staging.CustomerImport;
-- INSERT new data here

-- Log rotation pattern
IF DATEPART(day, GETDATE()) = 1
    TRUNCATE TABLE Logs.MonthlyArchive;

-- Test data cleanup
TRUNCATE TABLE Test.Orders;
TRUNCATE TABLE Test.OrderDetails;
TRUNCATE TABLE Test.Customers;

-- Partition maintenance
TRUNCATE TABLE Archive.SalesHistory
WITH (PARTITIONS (1 TO 12)); -- Keep only last 12 months

-- =============================================================================
-- End of Test File
-- =============================================================================