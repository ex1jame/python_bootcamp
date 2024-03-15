import psycopg2


connection = psycopg2.connect(
    dbname = 'temirlan',
    user='temirlan',
    password = '1',
    host = 'localhost',
    port = '5432'
)

cursor = connection.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS positions (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        department VARCHAR(100) NOT NULL
    );
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        position_id INTEGER REFERENCES positions(id) NOT NULL,
        phone_number VARCHAR(15) NOT NULL
    );
""")

cursor.execute("""
    INSERT INTO positions (title, department) VALUES
        ('Manager', 'HR'),
        ('Frontend-Developer', 'IT'),
        ('Accountant', 'Finance');
""")

try:
    cursor.execute("""
        INSERT INTO employees (name, position_id, phone_number) VALUES
            ('John Doe', 1, '+1234567890'),
            ('Jane Smith', 2, '+9876543210'),
            ('Mike Johnson', 3, '+1122334455'); 
    """)
    # Если успешно, подтвердите изменения
    connection.commit()
except Exception as e:
    # Если возникает ошибка, откатите изменения и выведите ее
    connection.rollback()
    print(f"Ошибка вставки данных: {e}")

# Удаление всех данных из таблицы positions
# cursor.execute("DELETE FROM employees;")
# cursor.execute("DELETE FROM positions;")

# # Удаление всех данных из таблицы employees
# # 


cursor.execute("SELECT * FROM positions;")
positions_data = cursor.fetchall()

# Проверка наличия данных в таблице employees
cursor.execute("SELECT * FROM employees;")
employees_data = cursor.fetchall()
connection.commit()
cursor.close()
connection.close()

print("Таблица positions:")
print(positions_data)

print("\nТаблица employees:")
print(employees_data)