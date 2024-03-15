#Инкапсуляция :
# 1 Языковая конструкция которая помогает связать данные с методами для их обработки и управление
# (связь между данными и методами которые управляют ими) (класс - капсула)
# 2 Механизм сокрытия при помощи которого иожно ограничить доступ одного компонента программы к другому

# Encapsulation  = """
# class Phone:
#     number =  "99388912938"

#     def print_number(self):
#         print(f'moi nom {self.number}')
#         print(f'moi nom {Phone.number}')

# obj = Phone()
# obj.print_number()

# Инкапсуляция как механизм сокрытия
# 3 уровня сокрытия данных в питоне
        # 1 Публичный(public) - number,print_number
# 2 защищенный (protected) - нет доступа извне _number

# 3 приватный (__private) - __number 

# class Car:
#     _country = 'Germany'
#     __motor = 'GT Line'

#     def __init__(self) -> None:
#         self.marka = 'bmw'
#         self._model = 'i8'
#         self.__color = 'black'
    
    # @property
    # def color(self):
    #     return self.__color

    # @color.setter
    # def color(self, value):

# obj1 = Car()
# print(obj1._country, obj1.model)


# --------------------------------

# class Person:
#     def __init__(self,name,age) -> None:
#         self.__name = name
#         self.__age = age
    
#     def display_inf(self):
#         print(f'My name is {self.name} and I\'m {self.age} years old')

# obj = Person('John' ,18)
# obj.display_inf()
# obj.name = [1,2,3,4,5]
# obj.age = -25
# obj.display_inf()
# -------------------------------------------
# getter and setter
# они нужны чтобы избежать прямого обращения к сокрытым атрибутам
# при этом можно добавить логику валидации данных которые будут установлены в атрибут



class Person:
    def __init__(self,name,age) -> None:
        self.__name = name
        self.__age = age
    
    def display_inf(self):
        print(f'My name is {self.__name} and I\'m {self.__age} years old')

    def name(self): return self.__name

    def age(self): return self.__age

    def set_name(self,name):
        if not isinstance(name,str):
            print('Name must be str object!')
        else:
            self.__name = name
    
    def set_age(self,age):
        if not isinstance(age,int) or not 0 <= age <150:
            print('Invalid value for age')
        else:
            self.__age = age










































































































































































































































































































































































































