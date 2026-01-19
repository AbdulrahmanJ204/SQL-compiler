UPDATE dbo.TableA
SET col1 = 1;
UPDATE dbo.TableA
SET @x = 5;

UPDATE dbo.TableA
SET col1 = DEFAULT;

UPDATE dbo.TableA
SET col1 = 1,
    col2 = 2,
    col3 = 3;

UPDATE dbo.TableA
SET col1 += 1,
    col2 -= 2,
    col3 *= 3,
    col4 /= 4,
    col5 %= 5;

UPDATE dbo.TableA
SET col1 &= 1,
    col2 |= 2,
    col3 ^= 3;

UPDATE @myTable
SET col1 = 10;

UPDATE TOP (5) dbo.TableA
SET col1 = 1;

UPDATE dbo.TableA
SET col1 = 1
OUTPUT inserted.col1;

UPDATE dbo.TableA
SET col1 = b.col1
FROM dbo.TableB b;

UPDATE dbo.TableA
SET col1 = 1
WHERE col2 = 2;

UPDATE a
SET a.col1 = b.col1
FROM dbo.TableA a
JOIN dbo.TableB b ON a.id = b.id
WHERE b.col1 > 10;

UPDATE dbo.TableA
SET textcol.WRITE('abc', 1, 3);

UPDATE dbo.TableA
SET geomcol.MakeValid();

UPDATE dbo.TableA
SET geomcol.STBuffer(10, 2);

WITH cte AS (
    SELECT id, val FROM dbo.TableB
)
UPDATE dbo.TableA
SET col1 = cte.val
FROM cte
WHERE dbo.TableA.id = cte.id;

WITH cte AS (
    SELECT id, val FROM dbo.TableB
)
UPDATE TOP (1) a
SET a.col1 += 1,
    a.textcol.WRITE('x', 1, 1),
    a.geomcol.STBuffer(5)
OUTPUT inserted.col1
FROM dbo.TableA a
JOIN cte ON a.id = cte.id
WHERE a.col2 > 0;
