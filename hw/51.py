"""
1)Создайте класс и объявите в нём 3 метода: публичный, 
защищённый и приватный. Затем создайте экземпляр данного 
класса и вызовите по очереди каждый из методов.
"""
# class Class1:
#     def public(self):
#         print(f'Public 1 \n Protect : {self._protect()} n\Private :{self.__private()}')
    
#     def _protect(self):
#         print(f'PRotect')
    
#     def __private(self):
#         print(f'Private value')

# obj= Class1()
# obj.public()
"""
2)Определите класс A, в нём объявите метод method1, 
который печатает строку "Hello World". Затем создайте класс B,'
 который будет наследоваться от класса A. Создайте экземпляр от класса B,
   и через него вызовите метод method1.
"""
# class A:
#     def method1(self):
#         print(f'Hello world!')
    
# class B(A):
#     pass

# obj = B()
# obj.method1()
"""
3)Объявите класс Car, в котором будет приватный атрибут экземпляра speed.
 Затем определите метод set_speed, который будет устанавливать значение скорости 
 и метод show_speed, с помощью которого Вы будете получать значение скорости.
"""
# class Car:
#     def __init__(self) -> None:
#         self.__speed = 0
    
#     def set_speed(self,value):
#         if isinstance(value,(int,float)):
#             self.__speed = value
#         else:
#             raise ValueError("Value must be number")
            
#     def show_speed(self):
#         print(f'Speed {self.__speed}')

# obj = Car()
# obj.set_speed(50)
# obj.show_speed()
"""
4)Перепишите класс Car из предыдущего задания.
Перепишите метод set_speed() с использование декоратора @speed.setter, 
а метод show_speed() с использованием декоратора @property, для того
 чтобы можно было работать с данным классом следующим образом:

car = Car()
car.speed = 120
print(car.speed)
"""
# писать код здесь
# class Car:
#     def __init__(self) -> None:
#         self.__speed = None
    
#     @property
#     def speed(self):
#         return self.__speed
    
#     @speed.setter
#     def speed(self,value):
#         if isinstance(value,(int,float)):
#             self.__speed = value
#         else:
#             raise ValueError("Value must be number")
            

#     @property
#     def show_speed(self):
#         print(f'Speed {self.__speed}')
# car = Car()
# car.speed = 120
# print(car.speed)
"""
5. Создайте класс Car. Пропишите в init параметры make, model, year, odometer, fuel.
Пусть у показателя odometer будет первоначальное значение 0, а у fuel 70.
Добавьте метод drive, который будет принимать расстояние в км. В самом начале проверьте,
хватит ли вам бензина из расчета того, что машина расходует 10 л / 100 км (1л - 10 км) . Если
его хватит на введенное расстояние, то пусть этот метод добавляет эти километры к значению
одометра, но не напрямую, а с помощью приватного метода __add_distance. Помимо этого
пусть метод drive также отнимет потраченное количество бензина с помощью приватного
метода __subtract_fuel, затем пусть распечатает на экран “Let’s drive!”. Если же бензина не Let’s drive!”. Если же бензина не
хватит, то распечатайте “Let’s drive!”. Если же бензина не Need more fuel, please, fill more!”
"""
# писать код здесь
# class Car:
#     def __init__(self,make:str,model:str,year:int)->None:
#         self.make = make
#         self.model = model
#         self.year = year
#         self._odometers = 0
#         self._fuel = 70
    
#     def drive(self,distance):
#         need = distance // 10
#         if self._fuel < need:
#             print('Need more fuel, please, fill more!')
#         else:
#             self.__add_distance(distance)
#             self.__substract_fuel(need)
#             print('Let`s drive!')
    
#     def __add_distance(self,distance):
#         self._odometers += distance
    
#     def __substract_fuel(self,amount):
#         self._fuel -= amount
    
#     @property
#     def odometers(self):
#         return self._odometers
        
# my_car = Car("Toyota","Camry",2018)
# print(my_car.odometers)
# my_car.drive(150)
# print(my_car.odometers)  