-- Test File 3: All Identifier Types and Variables

-- Unquoted Identifiers - Simple
SELECT id, name, email, username FROM users;
SELECT first_name, last_name, date_of_birth FROM employees;

-- Unquoted Identifiers - With Underscores
SELECT user_id, customer_name, order_date, shipping_address;
SELECT _private, __internal, ___hidden;

-- Unquoted Identifiers - Starting with @ (allowed)
SELECT @param, @value, @temp_var;

-- Unquoted Identifiers - Starting with # (temp tables)
SELECT * FROM #temp_table;
CREATE TABLE #session_data (id INT, value VARCHAR(100));
INSERT INTO #temporary (col1) VALUES ('test');

-- Unquoted Identifiers - Starting with ## (global temp)
SELECT * FROM ##global_temp;
CREATE TABLE ##shared_temp (id INT);

-- Unquoted Identifiers - With Numbers
SELECT col1, col2, table123, field99, item001;
SELECT a1b2c3, test123abc, data2023, year2024;

-- Unquoted Identifiers - With $ (allowed after first char)
SELECT price$, total$amount, value$1, special;

-- Bracket Identifiers - Simple
SELECT [id], [name], [order date], [user.name];
SELECT [first name], [last name], [email address];

-- Bracket Identifiers - With Spaces
SELECT [column with spaces], [another column], [multiple   spaces];

-- Bracket Identifiers - With Special Characters
SELECT [column-with-dashes], [column.with.dots], [column@special];
SELECT [price$], [value#1], [data%percent];

-- Bracket Identifiers - Escaped Brackets
SELECT [column]]name], [data]]with]]brackets], [test];

-- Bracket Identifiers - Reserved Keywords as Names
SELECT [select], [from], [where], [table], [index];
SELECT [user], [order], [group], [key], [view];

-- Bracket Identifiers - Numbers Only
SELECT [123], [456789], [001], [2024];

-- Double Quoted Identifiers - Simple
SELECT "id", "name", "email" FROM "users";
SELECT "first_name", "last_name", "age";

-- Double Quoted Identifiers - With Spaces
SELECT "column with spaces", "another column", "user name";

-- Double Quoted Identifiers - Escaped Quotes
SELECT "column""name", "data""with""quotes", "test""";

-- Double Quoted Identifiers - Special Characters
SELECT "column-dash", "column.dot", "column@at";
SELECT "price$", "value#", "percent%";

-- Double Quoted Identifiers - Reserved Keywords
SELECT "select", "from", "where", "insert", "update";

-- User Variables - Simple
DECLARE @id INT;
DECLARE @name VARCHAR(100);
DECLARE @price DECIMAL(10,2);

SET @id = 1;
SET @name = 'John Doe';
SET @price = 99.99;

-- User Variables - With Underscores
DECLARE @user_id INT;
DECLARE @order_total MONEY;
DECLARE @temp_value VARCHAR(50);

-- User Variables - With Numbers
DECLARE @var1 INT, @var2 INT, @test123 VARCHAR(20);

-- User Variables - With $ and #
DECLARE @price$ DECIMAL(10,2);
DECLARE @temp#1 INT;
DECLARE @value$$ MONEY;

-- User Variables - In Queries
SELECT * FROM users WHERE id = @user_id;
UPDATE products SET price = @new_price WHERE id = @product_id;
INSERT INTO logs (message) VALUES (@log_message);

-- System Variables (two @ symbols)
SELECT @@VERSION;
SELECT @@SERVERNAME;
SELECT @@SPID;
SELECT @@ROWCOUNT;
SELECT @@ERROR;
SELECT @@IDENTITY;
SELECT @@TRANCOUNT;
SELECT @@LANGUAGE;

-- System Variables - Complex Names
SELECT @@MAX_CONNECTIONS;
SELECT @@TOTAL_READ;
SELECT @@TOTAL_WRITE;
SELECT @@CURSOR_ROWS;

-- Mixed Identifier Types in Same Query
SELECT 
    id,
    [first name],
    "last_name",
    @user_var as user_value,
    @@ROWCOUNT as sys_rowcount
FROM [user table]
WHERE email = @email_param
AND status = 'active';

-- Schema Qualified Identifiers
SELECT dbo.users.id, dbo.users.name;
SELECT schema1.table1.col1, schema2.table2.col2;
SELECT [dbo].[users].[email];
SELECT "schema"."table"."column";

-- Database Qualified Identifiers
SELECT mydb.dbo.users.id;
SELECT database1.schema1.table1.column1;
SELECT [MyDatabase].[dbo].[Users].[ID];

-- Server Qualified Identifiers
SELECT server.database.schema.table.column;
SELECT [ServerName].[DatabaseName].[dbo].[Users].[Email];

-- Aliases with Different Identifier Types
SELECT 
    u.id as user_id,
    u.name as [user name],
    u.email as "email address",
    u.status as user$status
FROM users u;

-- Complex Identifier Scenarios
SELECT 
    _private_field,
    #temp_column,
    ##global_column,
    col123,
    abc$123,
    [special-characters],
    "quoted identifier",
    @variable,
    @@SYSTEM_VAR
FROM 
    [table with spaces]
INNER JOIN 
    "another_table" ON [table with spaces].id = "another_table".id;

-- Function Names (Identifiers)
SELECT 
    UPPER(name),
    LOWER(email),
    LEN(description),
    SUBSTRING(text, 1, 10),
    GETDATE(),
    COALESCE(col1, col2, 'default')
FROM products;

-- Stored Procedure Names
EXEC sp_procedure @param1 = 1, @param2 = 'value';
EXECUTE [dbo].[StoredProcedure] @id = @user_id;
EXEC "schema"."procedure" @input = @var;

-- Index Names
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX [Index With Spaces] ON [Table Name]([Column Name]);
DROP INDEX "index_name" ON "table_name";

-- Constraint Names
ALTER TABLE users ADD CONSTRAINT pk_users PRIMARY KEY (id);
ALTER TABLE orders ADD CONSTRAINT [FK Constraint] FOREIGN KEY (user_id) REFERENCES users(id);
ALTER TABLE products ADD CONSTRAINT "unique_sku" UNIQUE (sku);

-- All Identifier Types Together
DECLARE @test_var INT = 10;

SELECT 
    simple_column,
    _underscore,
    col123,
    [bracketed column],
    "quoted_column",
    @test_var as variable,
    @@VERSION as system
FROM 
    table_name t1
INNER JOIN 
    [Table With Spaces] t2 ON t1.id = t2.id
INNER JOIN
    "QuotedTable" t3 ON t2.id = t3.id
WHERE 
    t1.status = @test_var;