-- Test File 1: All Keywords and Data Types

-- Basic Keywords
SELECT ALL DISTINCT TOP 10
FROM employees
WHERE id = 1
AND status = 'active'
OR salary > 50000
ORDER BY name ASC, hire_date DESC
GROUP BY department
HAVING COUNT(*) > 5;

-- Join Keywords
SELECT e.name, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id
LEFT OUTER JOIN positions p ON e.pos_id = p.id
RIGHT JOIN locations l ON d.loc_id = l.id
CROSS JOIN benefits b
FULL JOIN projects pr ON e.id = pr.emp_id;

-- DDL Keywords
CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email NVARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE users
ADD COLUMN status BIT,
DROP COLUMN temp_field;

DROP TABLE IF EXISTS temp_table;

TRUNCATE TABLE logs;

-- DML Keywords
INSERT INTO users (username, email) 
VALUES ('john_doe', 'john@example.com');

UPDATE users 
SET status = 1 
WHERE id = 100;

DELETE FROM users 
WHERE created_at < CURRENT_DATE;

MERGE INTO target_table AS t
USING source_table AS s
ON t.id = s.id
WHEN MATCHED THEN UPDATE SET t.value = s.value;

-- Transaction Keywords
BEGIN TRANSACTION;
COMMIT;
ROLLBACK;
SAVE TRANSACTION savepoint1;

-- Constraint Keywords
ALTER TABLE orders
ADD CONSTRAINT fk_customer
FOREIGN KEY (customer_id) REFERENCES customers(id)
ON DELETE CASCADE;

CHECK (price > 0);

-- Index Keywords
CREATE INDEX idx_name ON users(username);
CREATE CLUSTERED INDEX idx_id ON users(id);
CREATE NONCLUSTERED INDEX idx_email ON users(email);

-- Data Types
CREATE TABLE data_types_test (
    col_bigint BIGINT,
    col_int INT,
    col_smallint SMALLINT,
    col_tinyint TINYINT,
    col_bit BIT,
    col_decimal DECIMAL(10,2),
    col_numeric NUMERIC(18,4),
    col_money MONEY,
    col_float FLOAT,
    col_real REAL,
    col_date DATE,
    col_time TIME,
    col_datetime DATETIME,
    col_timestamp TIMESTAMP,
    col_char CHAR(10),
    col_varchar VARCHAR(255),
    col_text TEXT,
    col_nchar NCHAR(10),
    col_nvarchar NVARCHAR(MAX),
    col_binary BINARY(16),
    col_varbinary VARBINARY(MAX),
    col_uniqueidentifier UNIQUEIDENTIFIER,
    col_xml XML
);

-- Set Operations
SELECT id FROM table1
UNION
SELECT id FROM table2;

SELECT id FROM table1
INTERSECT
SELECT id FROM table2;

SELECT id FROM table1
EXCEPT
SELECT id FROM table2;

-- Special Keywords
EXECUTE sp_procedure @param1 = 'value';
EXEC sp_help;

DECLARE @variable INT;
SET @variable = 100;

GRANT SELECT ON users TO public;
REVOKE INSERT ON users FROM user1;
DENY DELETE ON users TO user2;

-- Window Functions Keywords
SELECT 
    name,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as rank
FROM employees;

-- Case Expression
SELECT 
    CASE 
        WHEN status = 1 THEN 'Active'
        WHEN status = 0 THEN 'Inactive'
        ELSE 'Unknown'
    END as status_text
FROM users;

-- Exists and In
SELECT * FROM orders 
WHERE EXISTS (SELECT 1 FROM customers WHERE customers.id = orders.customer_id);

SELECT * FROM products 
WHERE category IN ('Electronics', 'Books', 'Clothing');

SELECT * FROM items 
WHERE price BETWEEN 10 AND 100;

-- Null Handling
SELECT COALESCE(phone, email, 'No contact') as contact
FROM users
WHERE name IS NOT NULL
AND email IS NULL;

SELECT NULLIF(column1, column2) FROM table1;

-- Additional Keywords
USE database_name;
GO

BACKUP DATABASE mydb TO DISK = 'backup.bak';
RESTORE DATABASE mydb FROM DISK = 'backup.bak';

CHECKPOINT;
DBCC CHECKDB;

WAITFOR DELAY '00:05:00';

PIVOT and UNPIVOT operations;
TABLESAMPLE SYSTEM (10 PERCENT);

-- Full Text Search
SELECT * FROM documents
WHERE CONTAINS(content, 'search term');

SELECT * FROM documents
WHERE FREETEXT(content, 'search phrase');

-- Current Values
SELECT CURRENT_USER, SESSION_USER, SYSTEM_USER, CURRENT_TIMESTAMP;