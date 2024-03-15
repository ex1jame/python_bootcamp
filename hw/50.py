# # Напишите класс Subscriber, у которого есть переменные экземпляра:
# # firstname
# # lastname
# # Сделайте так, чтобы метод __repr__ возвращал firstname + lastname
# # Напишите класс Provider, у которого есть:
# # переменный экземпляра name -- название провайдера
# # переменный экземпляра subscribers -- список, в котором будут храниться экземпляры класса Subscriber
# # переменный экземпляра payments -- словарь, ключём которого является экземпляр класса Subscriber, 
# # значением является сумма (вещественное число)
# # метод register_payment, который принимает экземпляр класса Subscriber,
# #  и сумму, затем проверяет, есть ли такой экземпляр Subscriber в списке subscribers. 
# # Если есть, записывает экземпляр в словарь payments в качестве ключа, а сумму в качестве значения
# # Если нет, выкидывает (raise) ошибку ValueError
# # Напишите класс Terminal, у которого есть
# # переменная экземпляра amount = 0
# # переменная экземпляра providers = [ ]
# # Регистрировать провайдера через метод register, который принимает экземпляр класса Provider и добавляет в providers
# # Принимать деньги в счет провайдера (pay), который принимает экземпляр класса Provider,
# #  экземпляр класса Subscriber и сумму (вещественное число). Внутри метода должен вызываться метод 
# # register_payment экземпляра класса Provider. register_payment успешно сработал, то в переменую
# #  amount нужно добавить сумму.

# # class Subscriber:
# #     def __init__(self, firstname, lastname):
# #         self.firstname = firstname
# #         self.lastname = lastname

# #     def __repr__(self):
# #         return f'{self.firstname} {self.lastname}'


# # class Provider:
# #     def __init__(self, name):
# #         self.name = name
# #         self.subscribers = []
# #         self.payments = {}

# #     def register_payment(self, subscriber, amount):
# #         if subscriber in self.subscribers:
# #             self.payments[subscriber] = amount
# #         else:
# #             raise ValueError("Subscriber not registered")

# #     def register_subscriber(self, subscriber):
# #         self.subscribers.append(subscriber)


# # class Terminal:
# #     def __init__(self):
# #         self.amount = 0
# #         self.providers = []

# #     def register(self, provider):
# #         self.providers.append(provider)

# #     def pay(self, provider, subscriber, amount):
# #         provider.register_payment(subscriber, amount)
# #         self.amount += amount





# # subscriber1 = Subscriber("John", "Doe")
# # subscriber2 = Subscriber("Alice", "Smith")

# # provider1 = Provider("Provider1")
# # provider2 = Provider("Provider2")

# # terminal = Terminal()
# # terminal.register(provider1)
# # terminal.register(provider2)


# # provider1.register_subscriber(subscriber1)
# # provider2.register_subscriber(subscriber2)

# # terminal.pay(provider1, subscriber1, 25.0)
# # terminal.pay(provider2, subscriber2, 10)

# # print(f'Terminal amount: {terminal.amount}')
# # print(f'Provider1 payments: {provider1.payments}')
# # print(f'Provider2 payments: {provider2.payments}')



# Основные Концепции:
# 1) Абстракция: Создать абстрактный класс Транспортное Средство, 
# который будет базовым для всех типов транспорта.
# 2) Наследование: Разработать классы Грузовик, Легковой 
# Автомобиль и Мотоцикл, наследующие от Транспортное Средство.
# 3) Полиморфизм: Реализовать методы, такие как двигаться,
#  загружать и разгружать, которые будут работать по-разному 
# для разных типов транспортных средств.
# 4) Миксины: Включить миксин, например GPSМиксин, который 
# добавляет функциональность GPS в транспортные средства.

# Задачи:
# Абстрактный Класс Транспортное Средство:
from abc import ABC,abstractmethod
class Transport:
    def __init__(self,marka,model,year):
        self.__marka = marka
        self.__model = model
        self.__year = year
    
    @property
    def marka(self): return self.__marka

    @property
    def model(self): return self.__model

    @property
    def year(self): return self.__year

    @abstractmethod
    def move_on(self): pass

    @abstractmethod
    def load(self,weight):pass

    @abstractmethod
    def unload(self,weight):pass

class  Car(Transport):
    def __init__(self,marka,model,year,max_speed):
        super().__init__(marka,model,year)
        self.__max_speed= max_speed

    def move_on(self):
        print(f"{self.marka} {self.model}, Year:{self.year} started to drive on the road.")

    def load(self, weight):
        return super().load(weight)
    
    def unload(self, weight):
        return super().unload(weight)

    def show_info(self):
        print(f"\nMarka : {self.marka}\nModel : {self.model},\nYear  : {self.year}\nMax Speed : {self.__max_speed}")
# Определите атрибуты, общие для всех транспортных средств (например, марка, модель, год выпуска).
# Определите абстрактные методы двигаться, загружать и разгружать.
# Классы Грузовик, Легковой Автомобиль и Мотоцикл:

# Наследуйте эти классы от Транспортное Средство.
# Реализуйте методы двигаться, загружать и разгружать по-своему для каждого типа транспорта.
# Миксин GPSМиксин:

# Добавьте методы для отслеживания местоположения транспорта.
# Интегрируйте этот миксин с классами транспортных средств.
# Тестирование:

# Создайте несколько экземпляров каждого типа транспортного средства.
# Продемонстрируйте полиморфизм, вызывая общие методы на разных объектах.
# Покажите работу GPS-функциональности.
# Это задание позволит студентам практиковаться в применении концепций ООП в Python, а также познакомит их с реальной ситуацией, где эти практики могут быть полезны.