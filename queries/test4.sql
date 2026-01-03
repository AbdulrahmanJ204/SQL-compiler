-- Test File 4: All Operators and Punctuation

-- Semicolon (Statement Terminator)
SELECT * FROM users;
INSERT INTO logs VALUES (1, 'test');
UPDATE settings SET value = 1;
DELETE FROM temp;

-- Comma (List Separator)
SELECT col1, col2, col3, col4, col5 FROM table1;
INSERT INTO users (id, name, email, status) VALUES (1, 'John', 'john@example.com', 1);
SELECT a, b, c, d, e, f, g FROM multi_column_table;

-- Dot (Object Separator)
SELECT table1.column1, schema1.table2.column2;
SELECT dbo.users.id, dbo.users.name, dbo.users.email;
SELECT database.schema.table.column;
SELECT server.database.schema.table.column;

-- Parentheses
SELECT * FROM (SELECT id, name FROM users) AS subquery;
SELECT (col1 + col2) * col3 FROM calculations;
INSERT INTO table1 (col1, col2) VALUES (1, 2);
SELECT COUNT(*) FROM table1 WHERE id IN (1, 2, 3, 4, 5);
SELECT ((a + b) * (c - d)) / (e + f) FROM math_ops;

-- Nested Parentheses
SELECT (((a + b) * c) - ((d / e) + f)) FROM complex_calc;

-- Equality Operator (=)
SELECT * FROM users WHERE id = 100;
SELECT * FROM products WHERE price = 99.99;
UPDATE users SET status = 1 WHERE id = 5;

-- Assignment (also =)
DECLARE @var INT = 10;
SET @var = 20;
SET @name = 'John';

-- Not Equal (!=)
SELECT * FROM users WHERE status != 0;
SELECT * FROM orders WHERE customer_id != 999;

-- Not Equal (<>)
SELECT * FROM products WHERE category <> 'Discontinued';
SELECT * FROM employees WHERE department <> 'HR';

-- Less Than or Equal (<=)
SELECT * FROM products WHERE price <= 100;
SELECT * FROM users WHERE age <= 65;
SELECT * FROM orders WHERE quantity <= 10;

-- Greater Than or Equal (>=)
SELECT * FROM products WHERE stock >= 50;
SELECT * FROM employees WHERE salary >= 50000;
SELECT * FROM scores WHERE value >= 90;

-- Less Than (<)
SELECT * FROM users WHERE age < 18;
SELECT * FROM products WHERE price < 10;
SELECT * FROM orders WHERE order_date < '2024-01-01';

-- Greater Than (>)
SELECT * FROM products WHERE price > 1000;
SELECT * FROM employees WHERE years_experience > 5;
SELECT * FROM sales WHERE amount > 10000;

-- Plus (+)
SELECT 10 + 20 AS sum_result;
SELECT price + tax AS total FROM products;
SELECT col1 + col2 + col3 FROM additions;
SELECT 'First' + ' ' + 'Last' AS full_name;

-- Minus (-)
SELECT 100 - 25 AS difference;
SELECT price - discount AS final_price FROM products;
SELECT col1 - col2 AS result FROM subtractions;

-- Multiply (*)
SELECT 5 * 10 AS product;
SELECT price * quantity AS total FROM order_items;
SELECT col1 * col2 * col3 FROM multiplications;

-- Divide (/)
SELECT 100 / 4 AS quotient;
SELECT total / count AS average FROM stats;
SELECT col1 / col2 AS ratio FROM divisions;

-- Modulo (%)
SELECT 17 % 5 AS remainder;
SELECT id % 2 AS is_odd FROM numbers;
SELECT value % 10 AS last_digit FROM data;

-- Plus Equal (+=)
UPDATE counters SET value += 1 WHERE id = 1;
UPDATE scores SET points += 10 WHERE player_id = 5;
SET @counter += 5;

-- Minus Equal (-=)
UPDATE inventory SET quantity -= 3 WHERE product_id = 100;
UPDATE balance SET amount -= 50.00 WHERE account_id = 123;
SET @total -= 10;

-- Multiply Equal (*=)
UPDATE prices SET amount *= 1.1 WHERE category = 'Premium';
UPDATE scores SET value *= 2 WHERE bonus_round = 1;
SET @multiplier *= 2;

-- Divide Equal (/=)
UPDATE costs SET price /= 2 WHERE clearance = 1;
UPDATE shares SET portion /= 3 WHERE split_date = '2024-01-01';
SET @divisor /= 10;

-- Modulo Equal (%=)
UPDATE numbers SET value %= 100 WHERE id > 10;
SET @modulo %= 7;

-- Ampersand (Bitwise AND)
SELECT col1 & col2 AS bitwise_and FROM bitwise_ops;
SELECT flags & 0xFF AS masked_flags FROM settings;
SELECT 12 & 10 AS result; -- 8

-- Pipe (Bitwise OR)
SELECT col1 | col2 AS bitwise_or FROM bitwise_ops;
SELECT permissions | 0x04 AS new_permissions FROM access;
SELECT 12 | 10 AS result; -- 14

-- Caret (Bitwise XOR)
SELECT col1 ^ col2 AS bitwise_xor FROM bitwise_ops;
SELECT flags ^ 0xFF AS inverted FROM settings;
SELECT 12 ^ 10 AS result; -- 6

-- Complex Expressions with Multiple Operators
SELECT 
    (price * quantity) + tax AS total,
    (price * quantity) - discount AS subtotal,
    (col1 + col2) / (col3 - col4) AS ratio,
    value % 10 AS last_digit,
    flags & 0xFF AS masked,
    status | 0x01 AS enabled
FROM complex_table;

-- Comparison Chains
SELECT * FROM data 
WHERE val1 > 10 AND val2 < 100 
AND val3 >= 50 AND val4 <= 75
AND val5 = 60 AND val6 != 70
AND val7 <> 80;

-- Arithmetic Expression Chains
SELECT 
    a + b - c * d / e % f AS complex_calc,
    ((x + y) * z) - (w / v) AS grouped_calc,
    p + q + r + s + t AS sum_many
FROM calculations;

-- Compound Assignment Chains
UPDATE stats SET 
    counter1 += 1,
    counter2 -= 2,
    multiplier *= 1.5,
    divisor /= 2,
    modval %= 10;

-- Bitwise Operation Chains
SELECT 
    (flags & 0xFF) | 0x01 AS modified1,
    (value ^ 0xFF) & 0x0F AS modified2,
    col1 & col2 | col3 ^ col4 AS complex_bitwise
FROM bitwise_complex;

-- All Operators in WHERE Clause
SELECT * FROM all_ops
WHERE 
    id = 1
    AND status != 0
    AND category <> 'Test'
    AND price >= 10
    AND price <= 100
    AND quantity > 5
    AND stock < 1000
    AND (price + tax) * quantity > 500
    AND amount - discount < 1000
    AND value / count >= 10
    AND id % 2 = 0
    AND flags & 0x01 = 1
    AND (permissions | 0x04) > 0
    AND checksum ^ 0xFF <> 0;

-- All Punctuation
SELECT 
    t1.col1, 
    t2.col2, 
    (t1.col3 + t2.col4) AS sum,
    schema.table.column,
    (SELECT MAX(value) FROM sub) AS max_val
FROM table1 t1, table2 t2
WHERE t1.id = t2.id;

-- Nested Expressions with All Operators
SELECT 
    ((a + b) * (c - d)) / ((e * f) - (g / h)) AS nested1,
    (x & y) | (z ^ w) AS nested2,
    ((p >= q) AND (r <= s)) OR (t <> u) AS nested3
FROM nested_ops;

-- Operators with Variables
DECLARE @a INT = 10, @b INT = 20, @c INT = 30;

SET @a += 5;
SET @b -= 3;
SET @c *= 2;

SELECT 
    @a + @b AS sum,
    @b - @a AS diff,
    @c * @a AS product,
    @c / @b AS quotient,
    @c % @b AS remainder,
    @a & @b AS bit_and,
    @a | @b AS bit_or,
    @a ^ @b AS bit_xor;