import psycopg2
import os

try:

    conn = psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password="12345"
    )


    with conn.cursor() as cursor:


        def fill_employees_table():
            with open("north_data/employees.csv", "r") as file:
                next(file)
                for line in file:
                    data = line.strip().split(",")
                    cursor.execute("INSERT INTO employees (first_name, last_name, job_title, department, hire_date, salary) VALUES (%s, %s, %s, %s, %s, %s)",
                                   (data[0], data[1], data[2], data[3], data[4], data[5]))

        def fill_customers_table():
            with open("north_data/customers.csv", "r") as file:
                next(file)
                for line in file:
                    data = line.strip().split(",")
                    cursor.execute("INSERT INTO customers (first_name, last_name, email, phone_number, address) VALUES (%s, %s, %s, %s, %s)",
                                   (data[0], data[1], data[2], data[3], data[4]))

        def fill_orders_table():
            with open("north_data/orders.csv", "r") as file:
                next(file)
                for line in file:
                    data = line.strip().split(",")
                    cursor.execute("INSERT INTO orders (customer_id, employee_id, order_date, ship_date, product_name, quantity, total_price) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                   (data[0], data[1], data[2], data[3], data[4], data[5], data[6]))


        fill_employees_table()
        fill_customers_table()
        fill_orders_table()


    conn.commit()

except Exception as e:
    print(f"Error: {e}")

finally:
    if conn:
        conn.close()
