# # # [In reply to Anarbek]
# # # Задача: Разработка иерархии классов для университета

# # # Вы проектируете систему для университета. Ваша задача — создать классы для различных типов людей в университете.

# # # 1) Базовый класс Person: Этот класс должен содержать общие атрибуты, такие как name (имя), age (возраст), и 
# # # id (идентификационный номер). Также включите метод show_details(), который выводит информацию о человеке.

# # # 2) Класс Student: Наследует от Person. Добавляет специфические атрибуты, такие как student_id и courses 
# # # (список курсов, на которые записан студент)
# # # . Переопределите метод show_details() для вывода дополнительной информации специфичной для студента.

# # # 3) Класс Professor: Также наследует от Person. Вводит дополнительные атрибуты, например,
# # #  employee_id, department (кафедра) и research_area (область исследований).
# # # Переопределите метод show_details(), чтобы он отображал информацию, специфичную для профессора.

# # # 4) Класс Administrator: Наследует от Person. Включает дополнительные атрибуты, такие как role (роль в университете) и department. Метод show_details() должен быть переопределен, чтобы отображать информацию, относящуюся к администраторам

# # class Person:
# #     def __init__(self,name,age,id) -> None:
# #         self.name = name
# #         self.age = age
# #         self.id = id
    
# #     def show_details(self):
# #         print(f'Name: {self.name} \nAge: {self.age} \nID: {self.id}')

# # class Student(Person):
# #     def __init__(self, name, age, id,student_id,courses) -> None:
# #         super().__init__(name, age, id)
# #         self.student_id = student_id
# #         self.courses = courses

# #     def show_details(self):
# #         super().show_details()
# #         print(f'Student ID: {self.student_id}')
# #         print(f'Courses')
# #         for course in self.courses:
# #             print(course)

# # class Professor(Person):
# #     def __init__(self, name, age, id,employee_id,department,research_area) -> None:
# #         super().__init__(name, age, id)
# #         self.employee_id = employee_id
# #         self.department = department
# #         self.research_area = research_area
    
# #     def show_details(self):
# #         super().show_details()
# #         print(f'Employee ID: {self.employee_id}\nDepartment: {self.department}\n Research_area: {self.research_area}')

# # class Administator(Person):
# #     def __init__(self, name, age, id,role,department) -> None:
# #         super().__init__(name, age, id)
# #         self.role = role
# #         self.department = department
# #     def show_details(self):
# #         super().show_details()

# #         print(f'role: {self.role}\nDepartment: {self.department}')

# # student1 = Student('Raychel',19,7,8,['MATH','CHEMISTRY'])
# # professor= Professor('Esen',58,5,1,'IT','bOKKS')
# # admin= Administator('Esen',58,5,'Genius','Market')

# # student1.show_details()
# # professor.show_details()
# # admin.show_details()

# # ```1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.
# # 2. Добавить сеттеры и геттеры к существующим атрибутам.
# # 3. Добавить в класс Computer метод make_computations, в котором бы выполнялись
# # арифметические вычисления с атрибутами объекта cpu и memory.
# # 4. Создать класс Phone (телефон) с приватным полем sim_cards_list (список симкард)
# # 5. Добавить сеттеры и геттеры к существующему атрибуту.
# # 6. Добавить в класс Phone метод call с входящим параметром sim_card_number и
# # call_to_number, в котором бы распечатывалась симуляция звонка в зависимости от
# # переданного номера сим-карты (например: если при вызове метода передать число 1 и
# # номер телефона, распечатывается текст “Идет звонок на номер +996 777 99 88 11” с
# # сим-карты-1 - Beeline).
# # 7. Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone.
# # 8. Добавить метод в класс SmartPhone use_gps с входящим параметром location, который
# # бы распечатывал симуляцию проложения маршрута до локации.
# # 9. В каждом классе переопределить магический метод str которые бы возвращали
# # полную информацию об объекте.
# # 10. Перезаписать все магические методы сравнения в классе Computer (6 шт.), для того
# # чтоб можно было сравнивать между собой объекты, по атрибуту memory.
# # 11. Создать 1 объект компьютера, 1 объект телефона и 2 объекта смартфона12. Распечатать информацию о созданных объектах
# # 13. Опробовать все возможные методы каждого объекта (например: use_gps,
# # make_computations, call, а также магические методы)```

# class Computer:
#     def __init__(self,cpu,memory) -> None:
#         self.__cpu = cpu
#         self.__memory = memory
    
#     @property
#     def cpu(self):
#         return self.__cpu
    
#     @cpu.setter
#     def cpu(self,value):
#         self.__cpu = value
    
#     @property
#     def memory(self):
#         return self.__memory
    
#     @memory.setter
#     def memory(self,value):
#         self.__memory = value
    
#     def make_computations(self):
#         result = self.__cpu * self.__memory
#         return result

# obj1= Computer(500,'4GB')
# print(obj1)

# class Phone:
#     def __init__(self,sim_card_list) -> None:
#         self.__sims = sim_card_list
    
#     @property
#     def sim_card_list(self):
#         return self.__sims
    
#     @sim_card_list.setter
#     def sim_card_list(self,cards):
#         if isinstance(cards, list):
#             self.__sims = cards
#         else:
#             print("Invalid input")

# Write a lambda function handler that takes a sentence as a parameter and returns the count of words.
# Example:
# Input: programming is fun
# Output: 3
handler = lambda x  : len(x.split())
print(handler('programming is fun'))

