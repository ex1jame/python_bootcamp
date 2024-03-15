# General class (parent class)
# class Computer:
#     def __init__(self) -> None:
#         pass
# class Vehicle(Computer):
#     def __init__(self, name, max_speed):
#         self.name = name
#         self.max_speed = max_speed

#     def start_engine(self):
#         print(f"{self.name} engine started.")

#     def stop_engine(self):
#         print(f"{self.name} engine stopped.")


# # Child class (derived class)
# class Car(Vehicle, Computer):
#     def __init__(self, name, max_speed, num_doors):
#         super().__init__(name, max_speed)
#         self.num_doors = num_doors

#     def open_door(self):
#         print(f"{self.name} door opened.")

#     def close_door(self):
#         print(f"{self.name} door closed.")

# class Engine(Car,Vehicle):
    

# from datetime import datetime
# class Car:
#     today = datetime.now()
    
#     wheels = 4
#     def __init__(self, model, brand, year):
#         self.model = model
#         self.brand = brand
#         self.__year = year
#         self.enginge = False


#     def start(self):
#         if self.enginge == False:
#             self.enginge = True
#             print('car is ready')

#     def drive(self):
#         if self.enginge == True:
#             print('car is go')
#         else:
#             print ('engine is not started')

#     def stop(self):
#         if self.enginge == True:
#             self.enginge = False
#             print('car is stop')
#     def __str__(self) -> str:
#         return f'brand: {self.brand}, model: {self.model}, year: {self.__year}'
#     @property
#     def year(self):
#         return self.__year
    
#     def set_year(self, new_year):
#         self.__year = new_year
    

# class Truck(Car):
#     wheels = 12
#     def __init__(self, model, brand, year, cargo):
#         super().__init__(model, brand, year)
#         self.cargo = cargo
#         self.load = 0
#     def cargo_load(self, poduct, kg):
#         if self.cargo < kg:
#             return 'truck not can load this product'
#         else:
#             self.load += kg

#     def get_year(self):
#         # year_now = Car.today.year()

        
#         age = int(str(Car.today)[0:4]) - self.year
#         return age

# class OilCar(Car):
#     pass

# class ElectricCar(Car):
#     pass

# class HybridCar(OilCar, ElectricCar):
#     pass

    



# some_car = Car('X6', 'BMW', 2017)
# some_truck = Truck('KG', 'Super', 2020, 40)
# some_truck.drive()
# some_truck.start()
# some_truck.drive()

# some_car.model = 'x5'
# print(some_car)
# print(some_car.year)


# print(some_car)
# some_truck.set_year= 2000

    
# print(some_truck.today)
# print(some_truck.get_year())