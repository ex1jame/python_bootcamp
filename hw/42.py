# # ДЗ 1
# # 1. Создать класс Person с атрибутами fullname, age, is_married

# # 2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю
# # информацию о человеке

# # 3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом
# # marks, который был бы словарем, где ключ это название урока, а значение - оценка.

# # 4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по
# # всем предметам
# # 5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом
# # experience.
# # 6. Добавить в класс Teacher атрибут уровня класса salary
# # 7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей
# # формуле: к стандартной зарплате прибавляется бонус 5% за каждый год опыта свыше 3х
# # лет.
# # 8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
# # 9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики
# # добавляются в список и список возвращается функцией как результат.
# # 10. Вызвать функцию create_students и через цикл распечатать всю информацию о каждом
# # ученике с его оценками по каждому предмету. Также рассчитать его среднюю оценку по
# # всем предметам.

# class Person:
#     def __init__(self,fullname,age,is_married) -> None:
#         self.name = fullname
#         self.age = age
#         self.maried = is_married
#     def introduce_myself(self):
#         print(f'fullname {self.name} age {self.age} maried {self.maried}')
# obj = Person('raychel gen',18,'No maried')
# obj.introduce_myself()

# class Student(Person):
#     def __init__(self, fullname, age, is_married,marks) -> None:
#         super().__init__(fullname, age, is_married)
#         self.marks = marks

#     def avg_mark(self):
#         total_marks = sum(self.marks.values())
#         return total_marks / len(self.marks)
    
#     def introduce_myself(self):
#         super().introduce_myself()
#         print('Marks: ', self.marks)
#         print('Average Mark: ',self.avg_mark())
    
# class Teacher(Person):
#     def __init__(self, fullname, age, is_married,experience,salary) -> None:
#         super().__init__(fullname, age, is_married)
#         self.experience = experience
#         self.salary = salary
    

#     def salary_calc(self):
#         base_salary = 3000
#         bonus_percentage = 0.05

#         if self.experience > 3:
#             bonus_years = self.experience - 3
#             bonus = base_salary * bonus_percentage *bonus_years
#             return base_salary + bonus
#         else:
#             return base_salary
    
#     def introduce_myself(self):
#         super().introduce_myself()
#         print(f'Experience: {self.experience}')
#         print(f'Salary: ${self.salary_calc():.2f}')


# def create_students():
#     student1 = Student("John Doe", 18, False, {"Math": 85, "History": 92, "English": 88})
#     student2 = Student("Jane Doe", 17, False, {"Math": 78, "History": 90, "English": 95})
#     student3 = Student("Bob Smith", 19, True, {"Math": 90, "History": 85, "English": 89})

#     return [student1, student2, student3]


# students_list = create_students()

# for student in students_list:
#     student.introduce_myself()
#     print("\n")
#=----------------------------------------------------------------------------------------


# Задача: Создание системы управления библиотекой

# Цель: Разработать классы для управления библиотекой, которые позволят управлять книгами
#  и пользователями библиотеки.

# Описание:

# Класс Book:

# Атрибуты: title (название), author (автор), isbn (международный стандартный книжный номер), availability (доступность книги для выдачи).
# Методы:
# Конструктор для инициализации атрибутов.

# return_book() - возвращает книгу в библиотеку, меняя статус доступности.
# str() - возвращает информацию о книге в читаемом формате.
# Класс User:

# Атрибуты: name (имя пользователя), user_id (ID пользователя), borrowed_books (список взятых книг).
# Методы:
# Конструктор для инициализации атрибутов.
# borrow_book(book) - добавляет книгу в список взятых, если она доступна.
# return_book(book) - удаляет книгу из списка взятых и возвращает её в библиотеку.
# get_borrowed_books() - возвращает список взятых пользователем книг.
# str() - возвращает информацию о пользователе и его взятых книгах.
# Класс Library:

# Атрибуты: books (список всех книг в библиотеке), users (список зарегистрированных пользователей).
# Методы:
# Конструктор для инициализации атрибутов.
# add_book(book) - добавляет новую книгу в библиотеку.
# add_user(user) - регистрирует нового пользователя в библиотеке.
# find_book(title) - ищет книгу по названию.
# find_user(user_id) - ищет пользователя по ID.
# borrow_book(user_id, book_title) - оформляет выдачу книги пользователю.
# return_book(user_id, book_title) - принимает возвращение книги от пользователя.
# Задание:
# Реализуйте вышеописанные классы с соответствующими атрибутами и методами. 
# Обеспечьте взаимодействие между классами таким образом, чтобы можно было регистрировать 
# пользователей, добавлять книги в библиотеку, а также осуществлять процесс заимствования 
# и возврата книг.

class Book:
    def __init__(self,title,author,isbn,availability) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.avable = availability


    def return_book(self):
        print(f'Вы вернули {self.title}, {True if self.avable == True else False}')

    
    def book_str(self):
        print(f'Name of book {self.title}\nAte')