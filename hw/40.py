
# """
# 1) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга -
#  синий, и число Пи(3.14). Экземпляры класса Circle в свою очередь должны иметь 
#  обязательный аттрибут - радиус. Также класс должен иметь метод расчета площади круга. 
#  Создайте экземпляр класса, переопределите цвет экземпляра и расчитайте площадь фигуры.
# """
# # class Circle:
# #     color = 'Blue'
# #     pi = 3.14
    
# #     def __init__(self,radius) -> None:
# #         self.radius = radius

    
# #     def square(self):
# #         return print(f'Square is {self.pi *self.radius ** 2} color is {self.color}')
    
# # obj = Circle(5)
# # obj.color = 'Red'
# # obj.square()

# """
# 2) Создайте класс для песен Song. Каждая песня имеет название,
#  автора и год выпуска. Добавьте три метода show_author, show_title,
#    show_year, выводящие утверждения о каждом атрибуте экземпляра класса Song, 
#    например: "Эта песня вышла в 2010 году". Создайте экземпляр класса с вашей 
#    любимой песней и примените все методы.
# # """
# # class Song:

# #     def __init__(self,title,author,year) -> None:
# #         self.title = title
# #         self.author = author
# #         self.year = year
    
# #     def show_author(self):
# #         print(f'Author is {self.author}')
    
# #     def show_title(self):
# #         print(f'Title is {self.title}')
    
# #     def show_year(self):
# #         print(f'Year is {self.year}')

# # kivano = Song('Die for you','The Weeknd','2021')
# # kivano.show_title()
# # kivano.show_author()
# # kivano.show_year()
        
# """
# 3) Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании, 
# стоимость посадки, стоимость за каждый пройденный километр. Также добавьте к классу 
# метод расчитывающий стоимость поездки. Создайте три экземпляра класса Taxi для трех 
# разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждом из них.
# """
# # class Taxi:
# #     def __init__(self,name,landing_cost,cost_traveled) -> None:
# #         self.name = name
# #         self.landing_cost = landing_cost
# #         self.cost_traveled = cost_traveled

# #     def work(self,kilometr):
# #         print(f'{self.name} cost: {self.landing_cost+self.cost_traveled*kilometr} ')

# # namba = Taxi('Namba',50,10)
# # yandex = Taxi('Yandex',40,25)
# # jorgo = Taxi('Jorgo',70,15)

# # namba.work(10)
# # yandex.work(10)
# # jorgo.work(10)

        
# """
# 4) Создайте класс телефонной книги. У контактов должны быть имена и фамилии 
# и номер телефона. Также создайте метод get_info, который выводит информацию о
#  контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888".
# Затем объявите экземляр класса и вызовите метод.
# """
# # class Phone_book:
# #     def __init__(self,first_name,last_name,phone) -> None:
# #         self.name = first_name + ' ' + last_name
# #         self.phone = phone
    
# #     def get_info(self):
# #         print(f'Контакт: {self.name}, number= {self.phone}')


# # obj = Phone_book('Raychel' , 'Adamson' , '+99655514842')
# # obj.get_info()
        

# """
# 5) Напишите класс Salary для расчета налогов на заработную плату. 
# У класса должна быть обязательная переменная класса - процент налога от зарплаты - 
# 8%. Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. 
# Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж 
# работы. Создайте экземпляр класса и посчитайте сумму вашего налога.
# """

# class Salary:
#     procent_nalog = 0.8

#     def __init__(self,sum_zp,staj_year,) -> None:
#         self.sum_zarp = sum_zp
#         self.staj = staj_year
    
#     def sum_all(self):
#         print(f'Nalog: {self.sum_zarp * self.staj / self.procent_nalog}')
    

# obj = Salary(30000,5)
# obj.sum_all()
        
# Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент 
# при инициализации (отвечающий за добавку к выбираемому лимонаду). В этом классе реализуйте
# # метод show_my_drink(), выводящий на печать Газировка и {ДОБАВКА} в случае наличия добавки,
# # а иначе отобразится следующая фраза: Обычная газировка.

# # class Soda:
# #     def __init__(self,type_gas=None) -> None:
# #         if isinstance(type_gas,str):
# #             self.gas = type_gas
# #         else:
# #             self.gas = None
        

# #     def show_my_drink(self):
# #         if self.gas:

# #             print(f'Gazirovka and {self.gas}')
# #         else:
# #             print('Обычная газировка')


# # obj = Soda()

# # obj.show_my_drink()
        

# # Создайте класс Student. При создании его экземпляра, мы должны записать имя 
# # и фамилию студента в соответствующие переменные объекта. В классе должны быть:
# #  1 переменная объекта books = [ ]
# #  2 переменная объекта “knowledge” со значением по умолчанию 0
# #  3 метод read_book, который принимает название книги, добавляет книгу в books, добавляет 100 баллов в knowledge
# #  4 метод do_homework, который при вызове добавляет 10 баллов в knowledge
# #  5 Создайте экземпляры, вызовите методы.
# # 6. Создайте класс имеющий атрибут "дата рождения" и автоматически просчитываемый возраст
# # ' по входящей дате рождения. Используйте модуль time/datetime
# from datetime import datetime
# class Student:
#     books = []
#     knowledge = 0
    
#     def __init__(self,f_name,l_name) -> None:
#         self.name = f_name + ' ' + l_name

#     def read_book(self,name_book):
#         self.books.append(name_book)
#         self.knowledge +=100
        
#     def do_homework(self):
#         self.knowledge += 10
    
# class Time_student(Student):
#     def __init__(self, name,birthdate):
#         super().__init__(name.split()[0], name.split()[1])

    
#         self.dates = datetime.strptime(birthdate, '%Y-%m-%d')

#     # Получение текущей даты
#         current_date = datetime.now()


#     # Расчет разницы между текущей датой и датой рождения
#         age_timedelta = current_date - self.dates
#         print(f"{self.name}'s age: {age_timedelta.days // 365} years")

# students = [
#     Student('Raychel','Adamson'),
#     Student('Tratil','Dengi'),
#     Student('Abu','Dabi'),

# ]


# def does(students):
#     for student in students:
#         student.read_book('Mariarty')
#         student.do_homework()

# does(students)

# # Create a Time_student object and calculate age
# obj = Time_student('Raychel Adamson', '2003-01-20')


# Задание 2: Класс "Студент"

# Задача: Определите класс Студент с атрибутами имя и оценки (список оценок). 
# Добавьте методы для добавления оценки к списку оценок и метод для расчета среднего балла.

# Пример использования:

# студент = Студент("Иван")
# студент.добавить_оценку(5)
# студент.добавить_оценку(4)
# print(студент.расчет_среднего()) -> 4.5
# class Student:
#     def __init__(self,name,*grade) -> None:
#         self.name = name
#         self.grades = grade
    
#     def avg_grade(self):
#         print(f'cost: {sum(self.grades) / len(self.grades)}')


# obj = Student('Gera',5,4,5,2,5,5,4,3)
# obj.avg_grade()
# Sanzhar, [19/2/24 13:55]
# Задание 1: Класс "Комната" и "Дом"
# Цель: Практика в создании взаимодействующих объектов и управлении ими.

# Задача: Создайте класс Комната с атрибутами название, ширина и длина.
#  Добавьте метод, который вычисляет площадь комнаты. Затем создайте класс Дом,
#  который содержит список комнат. В классе Дом должны быть методы для добавления
#  комнаты и вычисления общей площади дома.

        

# class Room():

#     def __init__(self,width,length) -> None:
#         self.width = width
#         self.lenght = length


    
#     def square_room(self):
#         return self.lenght * self.width

# class Home(Room):
    
#     def __init__(self,rooms,width,lenght) -> None:
#         super().__init__(width,lenght)
#         self.rooms = rooms

#     def square_home(self):
#         print(f'{self.rooms * self.square_room()} ')

# obj = Room(15,21)

# obj1=Home(3,obj.width,obj.lenght)
# obj1.square_home()


# Sanzhar, [19/2/24 13:55]
# Задание 3: Класс "Библиотека" и "Книга"
# Цель: Работа с коллекциями объектов и их методами.

# Задача: Расширьте класс Книга из предыдущего задания,
#  добавив атрибут количество. Создайте класс Библиотека,
# который будет содержать список книг. В классе Библиотека реализуйте методы для 
# добавления книги (с учетом уже существующих тайтлов), удаления книги по названию,
#  и поиска книг по автору.
# class Book:
#     def __init__(self,title,author) -> None:
#         self.title = title
#         self.author = author
        
# class Library:
#     def __init__(self,title,author,list_books = None) -> None:
#         self.list_books = list_books or []
#         self.list_books.append(Book(title,author))
    
#     def append_to_list(self,book):
#         if book not in self.list_books:
#             self.list_books.append(book)
#     def remove_list(self,book):
#         if book in self.list_books:
#             self.list_books.remove(book)

# book1 = Book('Azerot', 'Crimist')
# book2 = Book('Azkaban', 'Serenada')
# book3 = Book('Copilka', 'Unknown')

# library1 = Library(book1.title, book1.author)
# library1.append_to_list(book2)
# library1.append_to_list(book3)

# for book in library1.list_books:
#     print(f'Title: {book.title}, Author: {book.author}')

# # Удаляем книгу из библиотеки
# library1.remove_list(book2)

# # Выводим обновленное содержимое библиотеки
# print("Updated library:")
# for book in library1.list_books:
#     print(f'Title: {book.title}, Author: {book.author}')
# Sanzhar, [19/2/24 13:56]
# Задание 4: Класс "Магазин" и "Продукт"
# Цель: Изучение принципов инкапсуляции и взаимодействия объектов.

# Задача: Создайте класс Продукт с атрибутами название, цена и категория. 
# Затем создайте класс Магазин, который будет содержать список продуктов.
# В Магазине реализуйте методы для добавления продукта, удаления продукта
# по названию, и метод, который выводит список продуктов определенной категории.
# class Product:
#     def __init__(self,name,cost,category) -> None:
#         self.name = name
#         self.cost = cost
#         self.category = category

# class Shop:
#     def __init__(self,list_shop=None) -> None:
#         self.list_shop = list_shop or []
    
#     def append_list(self,product):
#         self.list_shop.append(product)
#     def remove_list(self,product):
#         self.list_shop.remove(product)
#     def get_info(self,category):
#         print(f'Values shop: {[x.name for x in self.list_shop if x.category == category] }')
# prod1 = Product('Apple',100,'fruct')
# prod2 = Product('Orange',150,'fruct')
# prod3 = Product('Cabbage',100,'ovosh')
# shop1 = Shop()
# # print(shop1.list_shop)
# shop1.append_list(prod1)
# shop1.append_list(prod2)
# shop1.append_list(prod3)
# shop1.remove_list(prod2)
# shop1.get_info('slavfa')
# print(shop1.list_shop)



# Sanzhar, [19/2/24 13:56]
# Задание 5: Класс "Пользователь" и "УчетнаяЗапись"
# Цель: Глубокое понимание взаимодействия классов и управления состоянием.

# Задача: Создайте класс Пользователь с атрибутами имя, фамилия и email.
#  Создайте класс УчетнаяЗапись, который будет содержать пользователя, логин, 
# пароль и баланс. В классе УчетнаяЗапись реализуйте методы для изменения пароля,
#  пополнения баланса и совершения платежа, проверяя достаточность средств на балансе.

class User:
    def __init__(self,f_name,l_name,email) -> None:
        self.f_name = f_name
        self.l_name = l_name
        self.email = email

class Account(User):
    def __init__(self,f_name,l_name,email,login,password,balance) -> None:
        super().__init__(f_name,l_name,email)
        self.log = login
        self.pasw = password
        self.bal = balance

    def change_password(self,newpassword):
        print(f'Ваш новый пароль {newpassword}')
    
    def replenish_balance(self,sums_repl):
        return print(f'Balance replanish to {sums_repl} your balance now {self.bal + sums_repl}')
    
    def payment(self,cost_pay):
        print(f"Summa to payment {cost_pay} balance now {self.bal - cost_pay if self.bal>=cost_pay else 'Недостаточно средств'}")

    
acc1 = Account('Tima','bays','ggds@mail.ru','Edward','515150',5000)
acc1.change_password('fdgfdg')
acc1.replenish_balance(100)
acc1.payment(5000)