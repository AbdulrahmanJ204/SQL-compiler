INSERT INTO dbo.TableA VALUES (1);
INSERT dbo.TableA VALUES (1, 2, 3);
INSERT @myTable VALUES (10);
INSERT INTO dbo.TableA (col1, col2) VALUES (1, 2);
INSERT INTO dbo.TableA VALUES (DEFAULT);
INSERT INTO dbo.TableA VALUES (1, DEFAULT, 3);
INSERT INTO dbo.TableA VALUES
(1, 2),
(3, 4),
(5, 6);

INSERT INTO dbo.TableA
SELECT col1, col2 FROM dbo.TableB;

INSERT INTO dbo.TableA DEFAULT VALUES;

INSERT TOP (5) INTO dbo.TableA VALUES (1);

INSERT INTO dbo.TableA
OUTPUT inserted.col1
VALUES (1);


WITH cte AS (
    SELECT 1 AS col1
)
INSERT INTO dbo.TableA
SELECT col1 FROM cte;

INSERT INTO mydb.dbo.TableA VALUES (1);

INSERT INTO dbo.TableA VALUES (1)

WITH cte AS (
    SELECT 1 AS a, 2 AS b
)
INSERT TOP (1) INTO dbo.TableA (col1, col2)
OUTPUT inserted.col1
SELECT a, b FROM cte;


