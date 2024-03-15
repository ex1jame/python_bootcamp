# """
# 1) Объявите 3 переменных, запишите в них строку, список и словарь
# . Затем запишите их в список, и пройдитесь по нему циклом чтобы 
# распечатать длину сразу каждого из объектов.
# """
# # string = 'gfdgfd'
# # list1 = [1,2,3,4,5]
# # dict1 = {1:1,2:2,3:3}
# # for i in string,list1,dict1:
# #     print(len(i))
# """
# 2) Создайте классы Dog и Cat с одинаковым методом voice. Для собак он должен печатать
#  "Гав", для кошек "Мяу".
# Объявите для каждого из классов по экземпляру. Затем объявить функцию to_pet(),
#  которая будет принимать животное и вызывать у него метод voice()
# """

# # class Dog:
# #     def voice(self):
# #         print(f'GAV')
# # class Cat:
# #     def voice(self):
# #         print(f'MEOW')

# # def to_pet(animal):
# #     animal=Dog()
# #     animal.voice()
# #     animal=Cat()
# #     animal.voice()
# # to_pet('sds')

# """
# 3. Создайте 2 класса: MyInt и MyString, наследуйте MyInt от int, MyString от str. У обоих
# классов переопределите метод, который отвечает за работу с оператором “+”.
# Напишите функцию add_objects(), которая принимает объект одного из 2 типов.
# При сложении объектов класса MyInt должно выдаваться сообщение “Это сложение”, а
# потом идти логика сложения 2 чисел, и выдача результата.
# При конкатенации объектов класса MyString() Должно выдаваться сообщение: “Это
# конкатенация”, а затем логика конкатенации из базового класса и выдача результата.
# """
# class MyInt(int):
#     def __add__(self, __value: int) -> int:
#         return super().__add__(__value)
# class MyString(str):
#     def __add__(self, __value: object, /) -> str:
#         return super().__add__(__value)
# def add_objects(obj):
#         if isinstance(obj, MyInt):
#             print("Это сложение")
#             result = obj + 5
#             print(result)
#         elif isinstance(obj, MyString):
#             print("Это конкатенация")
#             result = obj + 'dsd'
#             print(result)
# strs = MyString('dsds')
# itn = MyInt(10)

# add_objects(strs)
# add_objects(itn)

# """
# 4) Создайте 3 класса: Person, Employee и Student, при этом Employee и Student
#  должны наследоваться от Person. Определите во всех трёх классах метод get_info():
# -для класса Person он должен принимать и возвращать следующее: “Привет, меня зовут Иван Петров”.
# -для класса Employee он должен принимать и возвращать: “Привет, меня зовут Иван Петров, я работаю в компании “Рога и копыта” на должности “директор”.
# -для класса Student должно приниматься и возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.
# Определите функцию get_human_info(), которая будет принимать объект одного из трёх классов, вызывать метод get_info и печатать результат.
# """
# # class Person:
# #     def get_info(self):
# #         return 'Привет, меня зовут Иван Петров'
# # class Employee(Person):
# #     def get_info(self):
# #         return super().get_info() + f' я работаю в компании “Рога и копыта” на должности “директор”.'
# # class Student(Person):
# #     def get_info(self):
# #         return super().get_info() + f' я учусь в КГТУ на 3 курсе.'

# # person1 = Person()
# # emploey1 = Employee()
# # student1 = Student()
# # def get_human_info(obj):
# #     print(obj.get_info())

# # get_human_info(person1)
# # get_human_info(emploey1)
# # get_human_info(student1)
        
# """
# 5) Объявите абстрактный класс геометрических фигур Shape и 
# определите в нём абстрактный метод get_area() для расчёта 
# площади фигуры, которые необходимо переопределить в дочерних классах.

# Затем наследуйте от Shape три класса: Triangle, Square и Circle.
# -треугольник создаётся с заданными основанием и высотой
# -квадрат создаётся с заданной длиной стороны
# -круг создаётся с заданным радиусом
# Переопределите в каждом из классов метод get_area() таким образом, чтобы он рассчитывал площадь для конкретной фигуры.

# Затем создайте от каждого из трёх классов по экземпляру, и вызовите у каждого метод get_area()

# Подсказка: для создания абстрактных классов воспользуйтесь модулем abc
# """
# from abc import ABC,abstractmethod,abstractclassmethod

# class Shape:
#     def __init__(self,name) -> None:
#         self.name = name
#     @abstractmethod
#     def get_area(self):
#         pass
    
# class Triangle(Shape):
#     def __init__(self, osnovanie, visota) -> None:
#         super().__init__('Triangle')
#         self.osnovanie = osnovanie
#         self.visota = visota
    
#     def get_area(self):
#         return 0.5 * self.osnovanie * self.visota
# class Square(Shape):
#     def __init__(self, lenght) -> None:
#         super().__init__('square')
#         self.lenght = lenght
    
#     def get_area(self):
#         return self.lenght ** 2

# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__('KRUG')
#         self.radius = radius

#     def get_area(self):
#         from math import pi
#         return pi * self.radius **2

# obj = Circle(10)
# obj2 = Triangle(10,5)
# obj3 = Square(10)
# print(obj.get_area())
# print(obj2.get_area())
# print(obj3.get_area())
