# 1. Класс Driver
# # Атрибуты:
# class Driver:
#     def __init__(self,name,age,balance) -> None:
#         self.__name = name
#         self.__validate_age(age)
#         self.__age = age
        
#         self.__cars = []
#         self.__current_car = None
#         self.__rating = 0
#         self.__balance = balance

#     def __validate_age(self, age):
#         if not isinstance(age, int) or age <= 0:
#             raise ValueError("Age must be a positive integer.")
#         return age
    
#     @property
#     def name(self):
#         return self.__name

#     @property
#     def age(self):
#         return self.__age

#     @property
#     def cars(self):
#         return self.__cars

#     @property
#     def current_car(self):
#         return self.__current_car

#     @property
#     def rating(self):
#         return self.__rating
    
#     @rating.setter
#     def rating(self,value):
#         self.__rating = value

#     @property
#     def balance(self):
#         return self.__balance
    
#     @balance.setter
#     def balance(self,value):
#         self.__balance = value
    


# # __name: Имя (приватное).
# # __age: Возраст (приватный, должен быть не меньше 18 лет).
# # __cars: Список автомобилей (приватный, изначально пустой).
# # __current_car: Текущий автомобиль для гонок (приватный).
# # __rating: Рейтинг (приватный, изменяется в зависимости от результатов гонок).
# # __balance: Баланс (приватный, виртуальные деньги для покупки улучшений и новых автомобилей).
# # Методы:

# # Конструктор для инициализации атрибутов, с валидацией возраста.
# # Методы для добавления автомобиля в гараж и выбора текущего автомобиля.
# # Метод для участия в гонке и обновления рейтинга и баланса в зависимости от результатов.
# # Метод для покупки автомобиля или улучшений.
#     def add_car(self,car):
#         self.cars.append(car)
    
#     def choose_current_car(self, car):
#         if car in self.__cars:
#             self.__current_car = car
#         else:
#             print("Car not found in the garage.")
    
#     def participate_in_race(self,race_result):
#         race_winner,race_earnings = race_result
#         if self.current_car is not None:
#             if self.current_car == race_winner:
#                 self.rating += 1
#                 self.balance += race_earnings
#                 print('You are win')
#             else:
#                 print('You are not win')
#                 self.rating -= 1
        
#         else:
#             print('Please choose car before race')
    
#     def buy_car(self,car_cost,car):
#         if self.balance >= car_cost:
#             self.cars.append(car)
#         else:
#             print('Rabotay bomj')

#     def upgrade_car(self,upgrade_cost):
#         if self.current_car is not None:
#             if self.balance >= upgrade_cost:
#                 self.balance -= upgrade_cost
#                 print(f'{self.current_car} is upgraded')
#             else:
#                 print(f'U bomj ne obnovim')
#         else:
#             print(f'Vybery car')
    
# driver = Driver(name='John', age=25, balance=10000)

# car1 = 'Bmw'
# car2 = 'FAS'
# car3 = 'Car3'

# driver.add_car(car3)
# driver.add_car(car2)
# driver.add_car(car1)

# driver.choose_current_car(car2)

# driver.participate_in_race(('FAS', 500))  # Assuming Car2 won the race

# driver.buy_car(3000, 'Car4')

# driver.upgrade_car(1000)

    
# 2. Класс Car
# Атрибуты:

# __make: Марка (приватная).
# __model: Модель (приватная).
# __power: Мощность (приватная, только положительные числа).
# __upgrades: Уровень улучшений (приватный, список улучшений).
# __cost: Стоимость (приватная).
# Методы:

# Конструктор с валидацией мощности и стоимости.
# Метод для добавления улучшения к автомобилю.
# class Car:
#     def __init__(self,make,model,power,cost) -> None:
#         self.__make = make
#         self.__model = model
#         self.__power = power
#         self.__upgrades = []
#         self.__cost = cost
    
    
#     @property
#     def make(self):
#         return self.__make

#     @property
#     def model(self):
#         return self.__model

#     @property
#     def power(self):
#         return self.__power

#     @property
#     def upgrades(self):
#         return self.__upgrades

#     @property
#     def cost(self):
#         return self.__cost

#     def add_upgrade(self, upgrade):
#         self.upgrades.append(upgrade)

# car = Car(make='Toyota', model='Camry', power=150, cost=25000)

# # Accessing properties
# print(car.make)
# print(car.model)
# print(car.power)
# print(car.upgrades)
# print(car.cost)

# # Adding an upgrade
# car.add_upgrade('Turbo')
# print(car.upgrades)
# 3. Класс Upgrade
# Атрибуты:

# __name: Название улучшения (приватное).
# __type: Тип улучшения (приватный).
# __cost: Стоимость улучшения (приватная).
# __improvement: Величина улучшения (приватная).
# Методы:

# Конструктор для всех атрибутов.
class Upgrade:
    def __init__(self,name,type,cost,improvement) -> None:
        self.__name = name
        self.__type = type
        self.__cost = cost
        self.__improvement = improvement
    
    @property
    def info(self):
        return self.__name,self.__type,self.__cost,self.__improvement
    
    @info.setter

    def info(self,info_tuple):
        if len(info_tuple) == 4: 
            self.__improvement, self.__name, self.__type, self.__cost = info_tuple
            return info_tuple
        else:
            print("Invalid number of elements in info_tuple. Expected 4.")
    
obj = Upgrade('toyota','type',1524,'impr')
print(obj.info)

# 4. Класс Race
# Атрибуты:

# __name: Название гонки (приватное).
# __track_length: Длина трассы (приватная).
# __participants: Список участников (приватный).
# __prize_fund: Призовой фонд (приватный).
# __difficulty: Сложность трассы (приватная).
# __weather: Погодные условия (приватные).
# Методы:

# Конструктор для всех атрибутов с валидацией длины трассы.
# Метод для регистрации участника.
# Метод для проведения гонки с учетом мощности автомобилей, улучшений, сложности трассы и погоды.
# 5. Класс Weather
# Атрибуты:

# __type: Тип погоды (приватный).
# __effect: Влияние на гонку (приватное).
# Методы:

# Конструктор для всех атрибутов.
# 6. Класс RacingLeague
# Атрибуты:

# __name: Название лиги (приватное).
# __races: Список гонок (приватный).
# __participants: Список участников (приватный).
# Методы:

# Конструктор для всех атрибутов.
# Методы для добавления гонок и регистрации участников.
# Метод для проведения чемпионата с распределением призов.
class RacingLeague:
    def __init__(self,name) -> None:
        self.__name = name
        self.__races = []
        self.__participants = []
    
    def add_race(self,race):
        self.__races.append(race)
    
    def add_participants(self,parti):
        self.__participants.append(parti)
    
    def championate(self,prize):
        if len(self.__participants) > 0:
            prize_per_participant = sum(prize.values()) / len(self.__participants)
            for participant in self.__participants:
                prize_amount = prize.get(participant, 0)
                print(f"{participant} wins {prize_amount} prize.")
        else:
            print("No participants registered for the championship.")


leag = RacingLeague('leGUE')

leag.add_race('race 1')
leag.add_race('race 2')


leag.add_participants('1')
leag.add_participants('2')
leag.add_participants('3')

prize_distribution = {"Driver 1": 1000, "Driver 2": 800, "Driver 3": 500}
leag.championate(prize_distribution)