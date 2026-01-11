-- SELECT * FROM t WHERE (a = 1 OR b = 2);
-- SELECT * FROM users WHERE id = 10 AND age > 20;

-- SELECT * FROM t WHERE a = 1 AND b = 2;
-- SELECT * FROM t WHERE a = 1 OR c =3 AND b = 2;
-- SELECT * FROM t WHERE a = 1 AND c =3 AND b = 2 OR d=5 OR e=34 AND 4=2 OR 3=2 AND 3>=1;

-- select * from table1;
-- select [name],name2,"name3" from "table3";

-- SELECT * FROM users WHERE id = 10;
-- SELECT name FROM people WHERE age >= 18;

-- INSERT INTO employees (id, name) VALUES (1, 'John');
-- INSERT INTO employees (id, name) VALUES (1, 'John'), (2, 'Jane');
-- INSERT INTO employees SELECT * FROM temp_employees;

UPDATE t SET salary = 5000
-- FROM employees t
-- WHERE t.id = 10;