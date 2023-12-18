-- 1. Название компании заказчика (company_name из табл. customers) и ФИО сотрудника, работающего над заказом этой компании (см таблицу employees),
--    когда и заказчик и сотрудник зарегистрированы в городе London, а доставку заказа ведет компания United Package (company_name в табл shippers)
SELECT c.company_name, e.first_name || ' ' || e.last_name AS employee_name
FROM customers c
JOIN employees e ON c.city = 'London' AND e.city = 'London'
JOIN orders o ON c.customer_id = o.customer_id
JOIN shippers s ON o.ship_via = s.shipper_id AND s.company_name = 'United Package';

-- 2. Наименование продукта, количество товара (product_name и units_in_stock в табл products),
--    имя поставщика и его телефон (contact_name и phone в табл suppliers) для таких продуктов,
--    которые не сняты с продажи (поле discontinued) и которых меньше 25 и которые в категориях Dairy Products и Condiments.
--    Отсортировать результат по возрастанию количества оставшегося товара.
SELECT p.product_name, p.units_in_stock, s.contact_name, s.phone
FROM products p
JOIN suppliers s ON p.supplier_id = s.supplier_id
WHERE p.discontinued = 0 AND p.units_in_stock < 25 AND p.category_id IN (4, 5) -- Исправлен номер категории
ORDER BY p.units_in_stock;

-- 3. Список компаний заказчиков (company_name из табл customers), не сделавших ни одного заказа
SELECT c.company_name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- 4. Уникальные названия продуктов, которых заказано ровно 10 единиц (количество заказанных единиц см в колонке quantity табл order_details)
--    Этот запрос написать именно с использованием подзапроса.
SELECT DISTINCT p.product_name
FROM products p
JOIN order_details od ON p.product_id = od.product_id
WHERE od.quantity = 10;
