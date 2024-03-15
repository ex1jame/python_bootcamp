# # PRINCIPE OOP:
# # 1. Наследование
# # 2. Инкапсуляция
# # 3. Полиморфизм

# # 4. Абстракция
# # 4. Композиция
# # 4. Агрегация

# # №----------------------------------------------------

# # Наследование
# # Позволяет принимать родительские методы и атрибуты дочернему классу

# # Родительский класс
# # Дочерний класс

# # ------------------------------------------------------------


# # class Animal:
# #     def print_info(self):
# #         print('I\M AN ANIMAL')


# # class Lion(Animal):
# #     pass

# # class Dog(Animal):
# #     pass

# # lion = Lion()
# # lion.print_info()

# #------------------------------------------------------------------
# class Animal:
#     def say(self):
#         print(f'This animals name is {self.name}: {self.golos}')
    
#     def eat(self):
#         print(f'{self.name} eats:{self.meal}')

# class Lion(Animal):
#     name = 'lion'
#     golos = 'roar'
#     meat = 'meal'
#     griva = True

#     def info(self):
#         print(f'{self.name} griva:{self.griva}')


# class Koala(Animal):
#     name = 'koala'
#     golos = 'roar'
#     meat = 'efkalit'
#     griva = True

#     def info(self):
#         print(f'{self.name} griva:{self.griva}')


# class Dog(Animal):
#     name = 'dog'
#     golos = 'bark'
#     meat = 'meat'
#     griva = True

#     def info(self):
#         print(f'{self.name} griva:{self.griva}')


# simba = Lion()
# julian = Koala()
# rex = Dog()

# rex.say()
# julian.say()

# simba.say()

# print()

#--------------------------------------------------------------------
# class Person:
#     def info(self):
#         print(f'I\m study at bishkek')

# class Student(Person):
#     def info(self):
#         # super().info()
#         print(f'I\m study at Manas UNiversity')
#         super().info()


# obj = Student()
# obj.info()

#-----------------------------------

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def get_info(self):
        return {'brand': self.brand, 'model': self.model, 'price': self.price}

class Acer(Laptop):
    def __init__(self, model, price,year,videocard):
        super().__init__('Acer', model, price)
        self.year = year
        self.video = videocard
    def get_info(self):
        repr = super().get_info()
        repr['year'] = self.year
        repr['videocard'] = self.video
        return repr

class Apple(Laptop):
    def __init__(self, model, price,display,year):
        super().__init__('Macbook', model, price)
        self.display = display
        self.year = year

    
    def get_info(self):
        repr =super().get_info()
        repr['year'] = self.year
        repr['display'] = self.display
        return repr
    
mac = Apple('Proo' , 1500 , 14 , 2020)
print(mac.get_info())
acer = Acer('swift' , 600 , 2019,'Nvidia')
print(acer.get_info())