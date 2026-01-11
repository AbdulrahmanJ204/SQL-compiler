-- Test File 5: Comments, Whitespace, and Complex Combined Scenarios

-- ============================================
-- SECTION 1: Line Comments
-- ============================================

-- This is a simple line comment
SELECT * FROM users; -- Comment at end of line

-- Multiple consecutive line comments
-- Line 1
-- Line 2
-- Line 3
SELECT id, name FROM employees;

--Comment with no space after dashes
--Another comment without space
SELECT 1;

-- Comment with special characters: @#$%^&*()
-- Comment with numbers: 123456789
-- Comment with SQL keywords: SELECT FROM WHERE

SELECT 
    id,        -- user identifier
    name,      -- user name
    email,     -- contact email
    status     -- active/inactive status
FROM users;

-- ============================================
-- SECTION 2: Block Comments
-- ============================================

/* Single line block comment */
SELECT * FROM products;

/*
Multi-line block comment
Line 2
Line 3
*/
SELECT * FROM orders;

/* Comment with special characters: !@#$%^&*() */
/* Comment with SQL: SELECT * FROM table WHERE id = 1 */
/* Comment with numbers: 1234567890 */

SELECT 
    /* inline block comment */ col1,
    col2 /* another inline comment */,
    col3
FROM table1;

/* Nested block comments
   /* Inner comment level 1
      /* Inner comment level 2
         /* Inner comment level 3 */
      */
   */
*/
SELECT 1;

/*************************
 * Decorative comment box
 * with multiple lines
 * and asterisks
 *************************/
SELECT * FROM decorated;

-- ============================================
-- SECTION 3: Mixed Comments
-- ============================================

-- Line comment
/* Block comment */
-- Another line comment
/* Another block comment */
SELECT * FROM mixed_comments;

/* Block comment */ -- Line comment on same line
SELECT id FROM users; /* Inline block */ -- Inline line

/* Start of block
-- Line comment inside block comment
SELECT * FROM inside_block_comment;
End of block */

-- ============================================
-- SECTION 4: Whitespace Handling
-- ============================================

-- Multiple spaces
SELECT     id,     name,     email     FROM     users;

-- Tabs
SELECT	id,	name,	email	FROM	users;

-- Mixed spaces and tabs
SELECT  	id, 	 name,  	 email	 FROM	  users;

-- Newlines
SELECT
    id,
    name,
    email
FROM
    users
WHERE
    status = 1;

-- Excessive whitespace
SELECT      


    id,


    name


FROM     


    users;

-- ============================================
-- SECTION 5: Complex Combined Scenarios
-- ============================================

-- Scenario 1: All literal types in one query
SELECT 
    -- Boolean literals
    TRUE as bool_t,
    FALSE as bool_f,
    
    /* Number literals */
    42 as int_num,
    3.14 as dec_num,
    1.5E10 as sci_num,
    
    -- String literals
    'Simple string' as str1,
    'String with ''quotes''' as str2,
    N'Unicode string: ñ' as unicode_str,
    
    /* Hex and bit */
    0xABCDEF as hex_val,
    1 as bit_val;

-- Scenario 2: All identifier types with operators
DECLARE @user_id INT = 100;
DECLARE @price$ DECIMAL(10,2) = 99.99;

SELECT 
    u.id,
    u.[first name],
    u."last_name",
    @user_id as var_id,
    @@ROWCOUNT as sys_var,
    (u.salary + @price$) * 1.1 as calculated
FROM [User Table] u
WHERE u.id = @user_id
    AND u.status <> 'Inactive'
    AND u.age >= 18
    AND u.score > 50;

-- Scenario 3: Complex nested query with all elements
/* 
   Complex query demonstrating:
   - Nested subqueries
   - Multiple joins
   - All operator types
   - Mixed identifier types
   - Comments throughout
*/
DECLARE @threshold DECIMAL(10,2) = 1000.00;
DECLARE @status_flag INT = 1;

SELECT 
    o.order_id,                    -- Order identifier
    o.[order date],                /* Date of order */
    c."customer_name",             -- Customer name
    (o.amount * o.quantity) as total, /* Calculate total */
    CASE 
        WHEN o.amount >= @threshold THEN 'High Value'  -- High value order
        WHEN o.amount >= 100 THEN 'Medium Value'       /* Medium value */
        ELSE 'Low Value'                               -- Default case
    END as value_category
FROM 
    orders o                       /* Main orders table */
    INNER JOIN 
    customers c ON o.customer_id = c.id  -- Join customers
    LEFT JOIN
    [Order Details] od ON o.order_id = od.order_id  /* Order details */
WHERE 
    o.status = @status_flag        -- Active orders only
    AND o.amount > 0               /* Positive amounts */
    AND o.quantity >= 1            -- At least one item
    AND (o.flags & 0xFF) = 1       /* Bitwise check */
    AND c.id IN (                  -- Customer filter
        SELECT customer_id 
        FROM premium_customers     /* Subquery for premium */
        WHERE active = TRUE        -- Active premium customers
    )
ORDER BY 
    total DESC,                    /* Sort by total descending */
    o.[order date] ASC;            -- Then by date ascending

-- Scenario 4: All keywords in context
/*************************************************
 * Comprehensive DDL/DML example
 * Tests: CREATE, ALTER, INSERT, UPDATE, DELETE
 * With: Constraints, indexes, transactions
 *************************************************/

-- Create database and use it
CREATE DATABASE TestDB;
USE TestDB;
GO

-- Create table with all constraint types
CREATE TABLE Users (
    UserID INT PRIMARY KEY IDENTITY(1,1),        -- Primary key with identity
    Username VARCHAR(50) UNIQUE NOT NULL,        -- Unique constraint
    Email NVARCHAR(100) NOT NULL,                -- Not null constraint
    Age INT CHECK (Age >= 18),                   -- Check constraint
    DepartmentID INT FOREIGN KEY REFERENCES Departments(ID), -- Foreign key
    CreatedDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    IsActive BIT DEFAULT 1,
    Balance MONEY CHECK (Balance >= 0)
);

-- Create indexes
CREATE CLUSTERED INDEX IX_UserID ON Users(UserID);
CREATE NONCLUSTERED INDEX IX_Username ON Users(Username);
CREATE INDEX IX_Email ON Users(Email);

-- Transaction with all DML operations
BEGIN TRANSACTION;                              -- Start transaction

    -- Insert data
    INSERT INTO Users (Username, Email, Age, DepartmentID)
    VALUES ('john_doe', 'john@example.com', 25, 1);
    
    -- Update data
    UPDATE Users 
    SET Balance += 100.00,                       -- Compound assignment
        IsActive = TRUE
    WHERE Username = 'john_doe';
    
    -- Delete old records
    DELETE FROM Users 
    WHERE CreatedDate < DATEADD(YEAR, -5, GETDATE())
        AND IsActive = FALSE;
    
    -- Conditional logic
    IF @@ROWCOUNT > 0                            -- Check rows affected
    BEGIN
        PRINT 'Records deleted';
        COMMIT;                                  -- Commit transaction
    END
    ELSE
    BEGIN
        PRINT 'No records deleted';
        ROLLBACK;                                -- Rollback transaction
    END

-- Scenario 5: All data types with literals
CREATE TABLE DataTypeTest (
    -- Integer types with various literals
    Col_TinyInt TINYINT DEFAULT 1,
    Col_SmallInt SMALLINT DEFAULT 100,
    Col_Int INT DEFAULT 1000,
    Col_BigInt BIGINT DEFAULT 1000000,
    
    -- Decimal types
    Col_Decimal DECIMAL(10,2) DEFAULT 99.99,
    Col_Numeric NUMERIC(18,4) DEFAULT 123.4567,
    Col_Float FLOAT DEFAULT 3.14E10,
    Col_Real REAL DEFAULT .5,
    Col_Money MONEY DEFAULT 1234.56,
    
    -- String types with literal examples
    Col_Char CHAR(10) DEFAULT 'CHAR',
    Col_Varchar VARCHAR(50) DEFAULT 'Variable character',
    Col_Text TEXT DEFAULT 'Large text',
    Col_NChar NCHAR(10) DEFAULT N'Unicode',
    Col_NVarchar NVARCHAR(100) DEFAULT N'Unicode variable: ñ',
    
    -- Date/Time types
    Col_Date DATE DEFAULT CURRENT_DATE,
    Col_Time TIME DEFAULT CURRENT_TIME,
    Col_DateTime DATETIME DEFAULT CURRENT_TIMESTAMP,
    Col_Timestamp TIMESTAMP,
    
    -- Binary types
    Col_Binary BINARY(16) DEFAULT 0xABCDEF,
    Col_Varbinary VARBINARY(MAX) DEFAULT 0x123456,
    Col_Bit BIT DEFAULT 1,
    
    -- Other types
    Col_UniqueId UNIQUEIDENTIFIER DEFAULT NEWID(),
    Col_XML XML
);

-- Scenario 6: Window functions and advanced features
SELECT 
    employee_id,
    department,
    salary,
    
    /* Window functions with OVER clause */
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as rank,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dense_rank,
    SUM(salary) OVER (PARTITION BY department) as dept_total,
    AVG(salary) OVER (PARTITION BY department) as dept_avg,
    
    -- Running totals
    SUM(salary) OVER (ORDER BY employee_id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as running_total,
    
    /* Lead and Lag */
    LAG(salary, 1) OVER (ORDER BY employee_id) as prev_salary,
    LEAD(salary, 1) OVER (ORDER BY employee_id) as next_salary
FROM 
    employees
WHERE 
    department IN ('Sales', 'Engineering', 'Marketing')  -- Filter departments
    AND salary BETWEEN 50000 AND 150000                  -- Salary range
    AND hire_date >= '2020-01-01'                       -- Recent hires
ORDER BY 
    department,
    rank;

/*
   END OF COMPREHENSIVE TEST FILE
   This file tests: keywords, data types, literals, identifiers,
   operators, punctuation, comments, whitespace, and complex scenarios
*/