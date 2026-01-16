-- SELECT * FROM t WHERE (a = 1 OR b = 2);
-- SELECT * FROM users WHERE id = 10 AND age > 20;

-- SELECT * FROM t WHERE a = 1 AND b = 2;
-- SELECT * FROM t WHERE a = 1 OR c =3 AND b = 2;
-- SELECT * FROM t WHERE a = 1 AND c =3 AND b = 2 OR d=5 OR e=34 AND 4=2 OR 3=2 AND 3>=1;

-- select * from table1;
-- select [name],name2,"name3" from "table3";

-- SELECT * FROM users WHERE id = 10;
-- SELECT name FROM people WHERE age >= 18;

--INSERT INTO employees (id, name) VALUES (1, 'John');
--INSERT INTO employees (id, name) VALUES (1, 'John'), (2, 'Jane');
--INSERT INTO employees SELECT * FROM temp_employees;

-- UPDATE t SET salary = 5000
-- FROM employees t
-- WHERE t.id = 10;

--PRINT 'Hello';
--GO
--PRINT @VAR;
--GO

--DELETE FROM emp
--a = 5
--@x <> @y

--@@ROWCOUNT > 0
--a = 1 AND b = 2
--a = 1 OR b = 2
--a = 1 OR b = 2 AND c = 3

--NOT a = 5
----NOT a = 5
--NOT NOT a = 5
--(a = 1 OR b = 2) AND c = 3
--a IN (1, 2, 3)
--a NOT IN (10, 20)
--a IN (SELECT id FROM t) -- TODO : This should be tested when select is finished




--age BETWEEN 18 AND 65
--salary NOT BETWEEN 1000 AND 5000
--name LIKE 'A%'
--name NOT LIKE '%test%'
--deleted_at IS NULL
--deleted_at IS NOT NULL

--EXISTS (SELECT 1 FROM users)
--NOT EXISTS (SELECT 1 FROM users)
--salary > ALL (SELECT salary FROM employees)
--price * quantity + tax
--
---5 + 10
----5
--a & b
--a | b ^ c & d
--(((a)))
--a IN (a + b * c,- -5 , 5+ 10, a | b ^ c & d,(((a))))
--a IN (1, 2) AND (b BETWEEN 3 AND 4 OR c IS NULL)
--NOT (a = 1 AND b IN (SELECT id FROM t)) OR c IS NOT NULL
-- ERRORS TESTS
--a =
--@``
a == 5
--DELETE FROM emp WHERE CURRENT OF cur1;



