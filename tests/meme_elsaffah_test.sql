-- UPDATE students
-- SET grade = 90;
-- -- تحديث عمود واحد
-- UPDATE students SET grade = 90;

-- -- تحديث عمود واحد مع WHERE
-- UPDATE students SET grade = 95 WHERE student_id = 1;

-- -- تحديث عدة أعمدة
-- UPDATE students SET grade = 85, status = 'active';

-- -- تحديث مع عمليات حسابية
-- UPDATE products SET price = price + 10;

-- UPDATE employees SET salary = salary * 1.1;
-- شروط متعددة مع AND
-- UPDATE students 
-- SET grade = 100 
-- WHERE grade >= 90 AND status = 'active';

-- -- شروط مع OR
-- UPDATE products 
-- SET discount = 20 
-- WHERE category = 'electronics' OR category = 'books';

-- -- شروط مركبة
-- UPDATE orders 
-- SET status = 'shipped' 
-- WHERE order_date >= '2024-01-01' AND total > 1000;

-- -- مقارنات مختلفة
-- UPDATE items 
-- SET available = 'yes' 
-- WHERE quantity > 0 AND quantity <= 100;
-- UPDATE مع JOIN بسيط
-- UPDATE students 
-- SET grade = 100 
-- FROM students s 
-- JOIN classes c ON s.class_id = c.class_id 
-- WHERE c.name = 'Math';

-- -- UPDATE مع عدة JOINs
-- UPDATE orders 
-- SET discount = 15 
-- FROM orders o 
-- JOIN customers c ON o.customer_id = c.customer_id 
-- JOIN regions r ON c.region_id = r.region_id 
-- WHERE r.name = 'North';

-- -- UPDATE باستخدام alias
-- UPDATE s 
-- SET s.grade = 95 
-- FROM students s 
-- JOIN enrollments e ON s.student_id = e.student_id 
-- WHERE e.course_name = 'Database';
-- -- استخدام متغيرات في التحديث
-- UPDATE products SET @old_price = price, price = 150;

-- UPDATE students SET grade = @new_grade WHERE student_id = @student_id;
-- عمليات حسابية معقدة


-- -- مثال شامل مع كل العناصر
-- UPDATE employees 
-- SET salary = salary * 1.2, 
--     bonus = (salary * 0.15) + 1000,
--     @old_salary = salary
-- FROM employees e
-- JOIN departments d ON e.dept_id = d.dept_id
-- JOIN locations l ON d.location_id = l.location_id
-- WHERE l.country = 'USA' 
--   AND e.years_of_service > 5 
--   AND (e.performance_rating >= 4 OR e.role = 'manager');

