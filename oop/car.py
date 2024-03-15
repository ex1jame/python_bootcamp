# import json  


# class Car:

#     def __init__(self,model,color,max_speed):
#         self.model = model
#         self.color = color
#         self.max_speed = max_speed
    
#     def stop_engine(self):
#         print(f'{self.model} is stopped')
    
#     def display_info(self):
#         try:
#             print(f"Vehicle Information: Model - {self.model}, Color - {self.color}")
#         except AttributeError:
#             print(f"Attribute {self.max_speed} is missing  ")

#     def change_color(self, new_color):
#         print(f'Change color {self.color} is changed {new_color}')
#         self.color = new_color
#     def start_engine(self):
#         print(f'{self.model} isss running engine')


# class ElectricCar(Car):
#     def __init__(self, model,color,brand,year,max_speed):
#         super().__init__(model,color,max_speed)
#         self.brand = brand
#         self.year = year
#     def w_to_dict(self):
#         return{
#             'model' : self.model,
#             'color' : self.color,
#             'brand' : self.brand,
#             'year' : self.year,
#             'speed' : self.max_speed,
#         }
    
#     def from_dict(self,data):
#         self.model = data['model']
#         self.color = data['color']
#         self.brand = data['brand']
#         self.year = data['year']
#         self.max_speed = data['speed']
    
#     def save_to_file(self,filename):
#         data_list =[car.w_to_dict() for car in self] 
#         with open(filename, 'w') as file:
#             json.dump(data_list,file,indent=4)
    
#     def load_from_file(self,filename):
#         try:
#             with open(filename,'r') as file:
#                 data_list = json.load(file)
#                 cars = [ElectricCar('','',0) for _ in data_list]
#                 for car,data in zip(cars,data_list):
#                     car.from_dict(data)
#                 return cars

#         except FileNotFoundError:
#                 print(f'File {filename} not found')
#         except json.JSONDecodeError:
#             print(f'Error decoding JSON data from file {filename} .')
    
    
#     def start_engine(self):
#         print(f'{self.brand} engine is running')

#     def display_info(self):
#         # Переопределение метода родительского класса
#         print(f"Car Information: Brand - {self.brand}, Year - {self.year}, Model - {self.model}, Color - {self.color}, Speed - {self.max_speed}")

# cars = [   
#     ElectricCar(model='BMW',color='White',max_speed=200,brand= "Toyota", year=2003),
#     ElectricCar(model='Toyota',color='Red',max_speed=150,brand= "Sivsa", year=2021),
#     ElectricCar(model='Mers',color='black',max_speed=180,brand= "TLO", year=2010)
# ]
# ElectricCar.save_to_file(cars,'cars_data.json')
# fsjdnfjdsf = ElectricCar(model='BMW',color='White',max_speed=200,brand= "Toyota", year=2003),

# fdslfmsd321321 = ElectricCar(model='Toyota',color='Red',max_speed=150,brand= "Sivsa", year=2021),


# my_car = Car(model='BMW',color='White',max_speed=200)
# my_car2 = Car(model='Toyota',color='Red',max_speed=150)
# my_car3 = Car(model='Mers',color='black',max_speed=180)
# my_car = ElectricCar(model="Camry", color="Blue",brand= "Toyota", year=2022,max_speed=155)
# my_car.display_info()
# for car in cars:
#     car.start_engine()
#     # car.change_color(new_color='Green')
#     car.display_info()

# def obj_call_to_methods(obj): #вызов объекта в подклассе electric_car в функции
#     obj.start_engine()
#     obj.display_info()
#     obj.stop_engine()

# obj_call_to_methods(my_car)

class Human:
    def __init__(self,value) -> None:
        self.value = value
    
    def __eq__(self,other):
        if isinstance(other,Human):
            return self.value == other.value
        return 
    
    def __lt__(self,other):
        if isinstance(other,Human):
            return self.value < other.value
        return
    def __ut__(self,other):
        if isinstance(other,Human):
            return self.value > other.value
        return
    
        
    
    def __le__(self,other):
        if isinstance(other,Human):
            return self.value <= other.value
        return
    

obj1 = Human(value=15)
obj2 = Human(value=32)

print(obj1 == obj2)
print(obj1 > obj2)
print(obj1 < obj2)
print(obj1 <= obj2)
        