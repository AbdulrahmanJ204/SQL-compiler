-- =========================
-- BASIC SELECT
-- =========================
SELECT *;

SELECT a, b, c FROM table1;

-- =========================
-- SELECT MODIFIERS
-- =========================
SELECT ALL * FROM users;

SELECT DISTINCT name FROM users;

SELECT TOP 5 * FROM users;

SELECT TOP (10) * FROM users;

SELECT TOP 20 PERCENT * FROM users;

SELECT DISTINCT TOP 3 name FROM users;

-- =========================
-- SELECT INTO
-- =========================
SELECT * INTO backup_users FROM users;

SELECT DISTINCT name INTO temp_names FROM users;

-- =========================
-- SELECT LIST VARIANTS
-- =========================
SELECT table1.* FROM table1;

SELECT *, col1 FROM table1;

SELECT col1 AS alias1, col2 alias2 FROM table1;

SELECT col1 + col2 AS sum_col FROM table1;

SELECT col1 = col2 FROM table1;

SELECT col1 += col2 FROM table1;

SELECT col1 *= col2 FROM table1;

-- =========================
-- WHERE / GROUP BY / HAVING
-- =========================
SELECT col1 FROM table1 WHERE col1 = 5;

SELECT col1 FROM table1 WHERE col1 > 10 AND col2 < 20;

SELECT col1 FROM table1 GROUP BY col1;

SELECT col1, COUNT(*) FROM table1 GROUP BY col1 HAVING COUNT(*) > 1;

-- =========================
-- SET OPERATORS
-- =========================
SELECT col1 FROM table1
UNION
SELECT col1 FROM table2;

SELECT col1 FROM table1
UNION ALL
SELECT col1 FROM table2;

SELECT col1 FROM table1
EXCEPT
SELECT col1 FROM table2;

SELECT col1 FROM table1
INTERSECT
SELECT col1 FROM table2;

-- =========================
-- NESTED QUERY EXPRESSION
-- =========================
(
    SELECT col1 FROM table1
)
UNION
SELECT col1 FROM table2;

-- =========================
-- COMPLEX COMBINATION
-- =========================
SELECT DISTINCT TOP (5) PERCENT
    t1.col1 AS c1,
    t1.col2 + t2.col3 AS total
INTO result_table
FROM table1 t1, table2 t2
WHERE t1.col1 = t2.col1
GROUP BY t1.col1, t1.col2, t2.col3
HAVING SUM(t2.col3) > 100
ORDER BY t1.col1;
