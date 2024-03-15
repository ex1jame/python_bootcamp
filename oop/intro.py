# ООП - обьектно-ориентрированное программирование

# class - this is  описание того как должен выглядить обьект, тоесть   в классе мы описываем
# какими свойствами(данными ) и поведением ( функции ) должен обладать обьект

# Обьект это некая сущность которую мы создаем от класса у обьекта есть собственное состояние свойств( данные)


# Атрибуты обычные переменные внутри класса

# методы функции внутри класса

#--------------------------------------------------

# class Human:
#     age = 0

#     def __init__(self,first_name,last_name,job,citizenship):
#         self.name = first_name+ ' ' +last_name
#         self.job = job
#         self.citizen = citizenship
#         # self.age = age
    
#     def show_info(self):
#         return f'Name: {self.name},Age: {self.age}, Job: {self.job} , Citizen: {self.citizen}'


# john = Human('JOhn','Snow','King of North','Northener')
# anvar = Human('Anvar','Lanister','programmer','KR')

# # print(john)
# # print(type(john))
# john.age =24
# john.job = 'King of WEsteros'
# print(john.show_info())
# print(anvar.show_info())

# class Dog:
#     # атрибуты класса 
#     age = 0
#     ushi = True

#     def __init__(self, name: str, color: str) -> None:
#         #Иницилизатор, именно здесь создаются атрибуты объекта
#         # self - ссылка на объект который создается
#         self.name = name
#         self.color = color

#     def bark(self):
#         print(f'{self.name} лает!')

#     def show_info(self):
#         print(f'Name: {self.name}, Age: {self.age}, color: {self.color}, ushi: {self.ushi}')

# rex = Dog('Rex', 'black')
# rex = Dog('Rex',age= 51, color='black')
# pluto = Dog('Pluto', 'white')
# aktosh = Dog(name='Aktosh', color='brown')


# rex.age = 2
# rex.age = 3
# rex.age = 4
# rex.age = 5
# rex.age = 6
# pluto.age = 7
# aktosh.age = 1
# aktosh.ushi = False


# print(rex.show_info())
# print(pluto.show_info())
# print(aktosh.show_info())

#---------------------------------------------------------------
class Human:
    def __init__(self,name) -> None:
        self.name  = name
        self.golod = 100

    def walk(self):
        print(f'{self.name} walking around!')
        self.golod += 30
    
    def work(self):
        print(f'{self.name} rabotu raboatet!')
        self += 50

    def eat(self,meal,finish = True):
        print(f'{self.name} покушала {meal}!')
        self.golod -= 60 if finish else 30
    
    def info(self):
        print(f'{self.name} -> {self.golod}')
    

obj = Human('Raychel')
obj.walk()
obj.eat('Kruasan')
obj.eat('Sandwich' , finish= False)
obj.eat('Burger' , finish= True) 
obj.info()

