-- 1. Добавить ограничение на поле unit_price таблицы products (цена должна быть больше 0)
ALTER TABLE products
ADD CONSTRAINT chk_unit_price_positive CHECK (unit_price > 0);

-- 2. Добавить ограничение, что поле discontinued таблицы products может содержать только значения 0 или 1
ALTER TABLE products
ADD CONSTRAINT chk_discontinued_values CHECK (discontinued IN (0, 1));

-- 3. Создать новую таблицу, содержащую все продукты, снятые с продажи (discontinued = 1)
CREATE TABLE discontinued_products AS
SELECT *
FROM products
WHERE discontinued = 1;

-- 4. Удалить из products товары, снятые с продажи (discontinued = 1)
--    Перед удалением товаров, сначала удалим все связанные записи из order_details
DELETE FROM order_details
WHERE product_id IN (SELECT product_id FROM discontinued_products);

--    Удалим товары из products
DELETE FROM products
WHERE discontinued = 1;

--    Удаление временной таблицы discontinued_products
DROP TABLE IF EXISTS discontinued_products;