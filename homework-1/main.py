"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os



# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="12345"
)

# Создание курсора для выполнения SQL-запросов
cursor = conn.cursor()

# Заполнение таблиц данными
def fill_employees_table():
    with open("north_data/employees.csv", "r") as file:
        next(file)  # Пропускаем заголовок
        for line in file:
            data = line.strip().split(",")
            cursor.execute("INSERT INTO employees (first_name, last_name, job_title, department, hire_date, salary) VALUES (%s, %s, %s, %s, %s, %s)",
                           (data[0], data[1], data[2], data[3], data[4], data[5]))

def fill_customers_table():
    with open("north_data/customers.csv", "r") as file:
        next(file)  # Пропускаем заголовок
        for line in file:
            data = line.strip().split(",")
            cursor.execute("INSERT INTO customers (first_name, last_name, email, phone_number, address) VALUES (%s, %s, %s, %s, %s)",
                           (data[0], data[1], data[2], data[3], data[4]))

def fill_orders_table():
    with open("north_data/orders.csv", "r") as file:
        next(file)  # Пропускаем заголовок
        for line in file:
            data = line.strip().split(",")
            cursor.execute("INSERT INTO orders (customer_id, employee_id, order_date, ship_date, product_name, quantity, total_price) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (data[0], data[1], data[2], data[3], data[4], data[5], data[6]))

# Заполнение таблиц данными
fill_employees_table()
fill_customers_table()
fill_orders_table()

# Применение изменений
conn.commit()

# Закрытие соединения с базой данных
cursor.close()
conn.close()
