-- Test File 2: All Literal Types

-- Boolean Literals
SELECT TRUE as true_value, FALSE as false_value;

INSERT INTO settings (feature_enabled) VALUES (TRUE);
UPDATE config SET is_active = FALSE WHERE id = 1;

-- Number Literals - Integers
SELECT 0, 1, 42, 100, 9999, 1234567890;

-- Number Literals - Decimals
SELECT 3.14, 0.5, 99.99, 0.001, 123.456789;

-- Number Literals - Starting with Decimal
SELECT .5, .999, .123456;

-- Number Literals - Scientific Notation (positive exponent)
SELECT 1E10, 2.5E5, 3.14E2, 1.0E+10;

-- Number Literals - Scientific Notation (negative exponent)
SELECT 1E-10, 2.5E-5, 3.14E-2, 1.0E-10;

-- Number Literals - Scientific Notation (no sign)
SELECT 1E10, 5E3, 9.99E8;

-- Hexadecimal Literals
SELECT 0x0, 0x1, 0xA, 0xF, 0xFF, 0x1234, 0xABCDEF;
SELECT 0x00, 0x0A0B0C, 0xDEADBEEF, 0x123456789ABCDEF;

-- Hexadecimal with line breaks (multiline hex)
SELECT 0x01\
02\
03;

SELECT 0xAB\
CD\
EF;

-- Bit Literals
SELECT 0 as bit_zero, 1 as bit_one;
INSERT INTO flags (is_enabled) VALUES (1);
UPDATE settings SET flag = 0 WHERE id = 1;

-- String Literals - Simple
SELECT 'Hello World';
SELECT 'SQL', 'Database', 'Testing';

-- String Literals - Empty
SELECT '';

-- String Literals - With Spaces
SELECT '   spaces   ';
SELECT 'Multiple    spaces';

-- String Literals - Escaped Quotes
SELECT 'It''s a string';
SELECT 'She said, ''Hello''';
SELECT 'That''s ''interesting''';

-- String Literals - Special Characters
SELECT 'Line 1\
Line 2';

SELECT 'Backslash: \\';
SELECT 'Tab\tCharacter';

-- String Literals - Long Text
SELECT 'This is a very long string literal that contains multiple words and could span across what would be multiple lines in the source code but is still a single string literal';

-- Unicode String Literals (N prefix)
SELECT N'Hello';
SELECT N'Unicode: ñ, é, ü, ø';
SELECT N'Chinese: 你好';
SELECT N'Japanese: こんにちは';
SELECT N'Arabic: مرحبا';
SELECT N'Emoji: 😀🎉';

-- Unicode String - Escaped Quotes
SELECT N'It''s Unicode';
SELECT N'Quote: ''text''';

-- Unicode String - Empty
SELECT N'';

-- Unicode String - With Line Breaks
SELECT N'Line 1\
Line 2';

-- Mixed Literals in Expressions
SELECT 
    100 + 50 as sum_int,
    3.14 * 2.0 as product_decimal,
    'First' + ' ' + 'Last' as concat_string,
    N'Unicode' + N' String' as concat_unicode;

-- Literals in WHERE Clauses
SELECT * FROM products WHERE price = 99.99;
SELECT * FROM users WHERE username = 'admin';
SELECT * FROM settings WHERE enabled = TRUE;
SELECT * FROM data WHERE hex_value = 0xABCD;
SELECT * FROM flags WHERE bit_flag = 1;

-- Literals in INSERT Statements
INSERT INTO products (id, name, price, in_stock, description) 
VALUES (
    1, 
    'Product Name',
    29.99,
    TRUE,
    'This is a description'
);

INSERT INTO unicode_data (text) VALUES (N'Ünîcödé tëxt');

INSERT INTO binary_data (hash) VALUES (0xDEADBEEF);

-- Literals in UPDATE Statements
UPDATE products SET price = 39.99, discount = 0.15 WHERE id = 100;
UPDATE users SET status = TRUE, last_login = 'Logged in' WHERE active = FALSE;
UPDATE settings SET hex_config = 0x0F, description = N'Configuración';

-- Number Literals - Edge Cases
SELECT 0.0, 0.00000001, 999999999.999999999;
SELECT 1E308, 1E-308; -- Very large and very small
SELECT .0, .00, .000;

-- Complex String Scenarios
SELECT 'String with ''multiple'' ''escaped'' ''quotes''';
SELECT 'Path: C:\\Users\\Admin\\Documents';
SELECT 'SQL Injection attempt: '' OR ''1''=''1';

-- All Literal Types in Single Query
SELECT 
    42 as integer_lit,
    3.14159 as decimal_lit,
    1.5E10 as scientific_lit,
    'Regular String' as string_lit,
    N'Unicode String' as unicode_lit,
    0xABCDEF as hex_lit,
    1 as bit_lit,
    TRUE as bool_true,
    FALSE as bool_false,
    .5 as decimal_start,
    1E-5 as negative_exp;