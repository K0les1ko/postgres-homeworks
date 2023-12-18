import psycopg2
import csv
import os

def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        return [row for row in reader]

def create_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="north",
            port='5433',
            user="postgres",
            password="1234"
        )
        return connection
    except Exception as e:
        print(f"Error: Unable to connect to the database. {e}")
        return None

def insert_data(connection, table_name, data):
    try:
        with connection.cursor() as cursor:

            header = data[0]
            for row in data[1:]:
                columns = ', '.join(header)
                values = ', '.join(['%s'] * len(row))
                query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
                cursor.execute(query, row)
        connection.commit()
    except Exception as e:
        print(f"Error: Unable to insert data into {table_name}. {e}")

def main():
    data_folder = '/Users/nikolayyaroshenko/Desktop/develop/pythonProject/skypro/Les_SQL/postgres-homeworks/homework-1/north_data'  # Укажите путь к папке с данными
    employees_data = read_csv(os.path.join(data_folder, 'employees_data.csv'))
    customers_data = read_csv(os.path.join(data_folder, 'customers_data.csv'))
    orders_data = read_csv(os.path.join(data_folder, 'orders_data.csv'))

    connection = create_connection()

    if connection:
        insert_data(connection, 'employees', employees_data)
        insert_data(connection, 'customers', customers_data)
        insert_data(connection, 'orders', orders_data)

        connection.close()

if __name__ == "__main__":
    main()
