-- Задание: Работа с базой данных PostgreSQL

-- Цели задания:
вы
-- Проверка знаний и умений по добавлению, обновлению и заполнению данными таблиц в базе данных PostgreSQL.

-- Описание задания:

-- В рамках данного задания вам предстоит работать с базой данных для интернет-магазина. Вам будет необходимо создать таблицы, добавить в них данные, обновить определенные записи и выполнить ряд запросов для проверки введенной информации.

-- Часть 1: Подготовка базы данных

-- 1. Создайте базу данных OnlineStore`.

-- 2. Внутри базы данных создайте следующие таблицы:

-- Products (Товары): id (первичный ключ), пате (имя), price (цена), quantity (количество на складе).

-- . Customers (Покупатели): id (первичный ключ), first_name (имя), last_name (фамилия), email (электронная почта).

-- . Orders (Заказы): id (первичный ключ), customer_id (внешний ключ к таблице Customers), order_date (дата заказа), total_amount (общая сумма).

-- Часть 2: Заполнение таблиц данными

-- 1. Добавьте не менее пяти записей в таблицу 'Products'.

-- 2. Добавьте не менее трех записей в таблицу Customers.

-- 3. Создайте заказы в таблице Orders, связав их с покупателями и укажите общую сумму заказа.

-- Часть 3: Обновление данных

-- 1. Измените цены на некоторые товары в лице Products.

-- 2. Обновите информацию о количестве товара на складе после создания заказов.

CREATE TABLE Products (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    quantity INT
);

CREATE TABLE Customers (
    id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE Orders (
    id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES Customers(id)
);

INSERT INTO Products (id, name, price, quantity)
VALUES
    (1, 'Product1', 10.99, 50),
    (2, 'Product2', 25.49, 30),
    (3, 'Product3', 5.99, 100),
    (4, 'Product4', 15.79, 20),
    (5, 'Product5', 8.99, 75);
INSERT INTO Customers (id, first_name, last_name, email)
VALUES
    (1, 'John', 'Doe', 'john.doe@example.com'),
    (2, 'Jane', 'Smith', 'jane.smith@example.com'),
    (3, 'Bob', 'Johnson', 'bob.johnson@example.com');
UPDATE Products
SET price = 12.99
WHERE name = 'Product1';

UPDATE Products
SET price = 28.99
WHERE name = 'Product2';
UPDATE Products
SET quantity = quantity - 10
WHERE name = 'Product1';

UPDATE Products
SET quantity = quantity - 5
WHERE name = 'Product2';

UPDATE Products
SET quantity = quantity - 15
WHERE name = 'Product3';
