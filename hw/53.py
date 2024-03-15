# 1) Создайте класс Person и объявите в нем 3 атрибута класса: name (public), 
# phone_number(protected) и сard_number(private), атрибуты класса будут равны следующим 
# значениям: "John", "+996 557 55 17 57" и "9999 9999 9999 9999". Создайте объект 'john' 
# класса Person и выведите на экран все атрибуты класса.

# class Person:
#     def __init__(self) -> None:
#         self.name = 'john'
#         self._phone_number = '+996557551757'
#         self.__card_number = '9999999999999'
    
#     @property
#     def __str__(self) -> str:
#         return f'\nName:\t{self.name}\nPhone number:\t{self._phone_number}\nCard number:\t{self.__card_number}'

# obj = Person()
# print(obj.__str__)




# 2) Создайте класс Person у которого будут следующие атрибуты 
# экземпляра класса: name (public), phone_number(protected) и сard_number(private). 
# Создайте экземпляр "john" класса Person со значениями ("John", "+996 557 55 17 57"
#  и "9999 9999 9999 9999") и выведите на экран все его атрибуты.

# class Person:
#     def __init__(self,name,phone_number,card_number) -> None:
#         self.name = name
#         self._phone_number = phone_number
#         self.__card_number = card_number

#     @property
#     def str_chi(self) -> str:
#         return f'\nName:\t{self.name}\nPhone number:\t{self._phone_number}\nCard number:\t{self.__card_number}'

# obj = Person("John", "+996 557 55 17 57","9999 9999 9999 9999")
# print(obj.str_chi)

# 3) Снова создайте класс Person и объявите в нем 3 атрибута: name (public), 
# phone_number(protected) и сard_number(private), атрибуты класса будут равны с
# ледующим значениям: "John", "+996 557 55 17 57" и "9999 9999 9999 9999"..
# Создайте объект "john" класса Person и измените все атрибуты класса на
#  значение None после выведите все атрибуты класса.

# class Person:
#     def __init__(self) -> None:
#         self.name = 'john'
#         self._phone_number = '+996557551757'
#         self.__card_number = '9999999999999'
    
   
#     def __str__(self) -> str:
#         return f'\nName:\t{self.name}\nPhone number:\t{self._phone_number}\nCard number:\t{self.__card_number}'
    

# obj = Person()
# obj.name = None
# obj._phone_number = None
# obj._Person__card_number = None
# print(obj.__str__())


# 4) Продолжая изменять логику предыдущего задания создайте класс 
# Person у которого будут следующие атрибуты экземпляра класса: name (public),
#  phone_number(protected) и сard_number(private). При инициализации обьекта
#  проверяйте введенные имя. Для этого напишите приватный метод validate_name для 
# валидации имени: данный метод будет проверять длину имени, если длина имени меньше
#  двух то возвращайте имя по дефолту John, если же введенное пользователем имя больше 
# двух, то необходимо возвращать имя с заглавной буквы (JOHN -> John, john -> John и тд).
#  Создайте экземпляр sam класса Person со значениями ("SAM", "+996 557 55 17 57" и "9999
#  9999 9999 9999") и выведите на экран все его атрибуты


# class Person:
#     def __init__(self) -> None:
#         self.name = 'john'
#         self._phone_number = '+996557551757'
#         self.__card_number = '9999999999999'
    
#     def __validate_name(self):
#         if len(self.name) <= 2: 
#             return self.name
#         else:
#             self.name = self.name.capitalize()
#     def __str__(self) -> str:
#         self.__validate_name()
#         return f'\nName:\t{self.name}\nPhone number:\t{self._phone_number}\nCard number:\t{self.__card_number}'
    

# obj = Person()
# # obj.name = None
# # obj._phone_number = None
# # obj._Person__card_number = None
# print(obj.__str__())




# 5) На этот раз заказчик передумал и попросил вас переписать предыдущий класс, 
# теперь его интересует только валидация номера телефона и номера карты. Создайте
#  класс Person у которого будут следующие атрибуты экземпляра класса: name (public),
#  phone_number(protected) и сard_number(private). При инициализации обьекта проверяйте
#  введенный номер телефона и номер карты. Для этого напишите приватный метод
#  validate_phone_number и защищенный метод validate_cart_number.
# Метод validate_phone_number сначала проверяет на то чтобы номер телефона являлся 
# типом int иначе возвращаем None далее нужно также проверять, чтобы номер начинался 
# на 999 иначе возвращается None
# Метод validate_cart_number в первую очередь также проверяет то что бы номер
#  карты являлся типом int иначе возвращаем None далее нужно также проверять что
#  чтобы количество цифр в номере карт была ровно 16 иначе также возвращаем None.
#  Создайте экземпляр 'tolik' класса Person c правильными данными и выведите на экран
#  все его атрибуты
# class Person:
#     def __init__(self,name,phone_number,card_number) -> None:
#         self.name = name
#         self._phone_number = phone_number
#         self.__card_number = card_number
    
#     def __validate_name(self):
#         if len(self.name) <= 2: 
#             return self.name
#         else:
#             self.name = self.name.capitalize()

#     def __validate_phone_number(self):
#         if isinstance(self._phone_number, int) and str(self._phone_number).startswith('999'):
#             return self._phone_number
#         else:
#             self._phone_number = None

#     def __validate_card_number(self):
#         if isinstance(self.__card_number, int) and len(str(self.__card_number)) == 16 and str(self.__card_number).startswith('999'):
#             return self.__card_number
#         else:
#             self.__card_number = None

#     def __str__(self) -> str:
#         self.__validate_card_number()
#         self.__validate_phone_number()
#         self.__validate_name()
#         return f'\nName:\t{self.name}\nPhone number:\t{self._phone_number}\nCard number:\t{self.__card_number}'
    

# tolik = Person(name='tolik', phone_number=999557551757, card_number=9999888877776666)
# print(tolik.__str__())





# 6) Необходимо написать класс Game у которого есть приватный атрибут класса
#  "level" который равен нулю и атрибут экземпляра класса name (ваше имя).
# Класс Game должен иметь методы для увеличения уровня игры (play) и получения 
# текущего уровня (get_level).
# Метод play принимает в себя переменную hours и проверяет если значение этой 
# переменной больше двух то уровень игры увеличивается на единицу иначе ничего 
# не происходит. Так как атрибут класса "level" приватный и поэтому недоступен извне,
#  необходимо реализовать метод "get_level" который возвращает значение атрибута "level".
# Создайте экземпляр "game" класса Game. Выведите на экран значение атрибута
#  "level" затем два раза используйте метод play чтобы уровень игры поднялся на два, 
# после снова выведите на экран значение атрибута "level".

# class Game:
#     def __init__(self,name) -> None:
#         self.__level = 0
#         self.name = name
    
#     def play(self,hours):
#         if hours > 2:
#             self.__level += 1
#         else:
#             return hours
        

#     def get_level(self):
#         return self.__level
    
# obj = Game('John')
# print(obj.get_level())
# obj.play(4)
# obj.play(3)
# print(obj.get_level())

# 7) Необходимо написать класс Game у которого есть приватный атрибут класса
#  "level" который равен нулю и атрибут экземпляра класса name (ваше имя).
# Класс Game должен иметь два метода: "set_level" и приватный метод "validate_name". 
# При инициализации экземпляра класса вызывается приватный метод validate_name 
# который возвращает имя в котором первая буква в верхнем регистре, а остальные 
# в нижнем (JOHN -> John).
# Также в классе необходимо реализовать метод "set_level" который принимает
#  в себя переменную "level" и увеличивает  значение приватного атрибута класса 
# "level" на значение этой переменной которую передали только в том случае если 
# имя обьекта (который сейчас играет в эту игру) "Tolik", иначе выведите на экран
#  '"имя_обьекта" ты не Tolik!'.
# Создайте сначала экземпляр класса "game" и передайте ему имя Raychel в качестве 
# аргумента. Далее вызовите метод set_level и передайте ему значение 5. После выведите 
# в терминал значение атрибута "level" (так как у нас не реализован метод get_level, 
# выведите это "нелегальным" способом). Теперь создайте экземпляр класса game2 и
#  передайте ему имя "TOLIK" в качестве аргумента. Далее вызовите метод set_level 
# и передайте ему значение 5. После выведите в терминал значение атрибута "level"
#  (так как у нас не реализован метод get_level, выведите это "нелегальным" способом).
# Ожидаемый вывод: 
# Raychel ты не Tolik!

# class Game:
#     def __init__(self,name) -> None:
#         self.__level = 0
#         self.name = name
        
#     def set_level(self,level):
#         self.__validate_name()
#         if self.name == 'Tolik':
#             self.__level = level
#         else:
#             print(f'{self.name} u are not Tolik')

#     def __validate_name(self):
#         self.name = self.name.capitalize()
    
#     def play(self,hours):
#         if hours > 2:
#             self.__level += 1
#         else:
#             return hours
        

#     def get_level(self):
#         return self.__level
    
# obj = Game('Raychel')
# obj.set_level(5)
# print(obj.get_level())
# game2 = Game('Tolik')
# game2.set_level(5)
# print(game2.get_level())


 





# 😍 Необходимо написать класс Game у которого есть приватный атрибут
#  класса level который равен нулю и атрибут экземпляра класса name (ваше имя).
# Так как атрибут класса level приватный и поэтому недоступен извне, 
# необходимо реализовать два метода для работы с ним: get_level и set_level. 
# Где get_level возвращает значение атрибута level и set_level принимает значение
#  и присваивает его атрибуту level. Создайте экземпляр game класса Game. Выведите 
# на экран значение атрибута level затем присвойте ему значение 10 и выведите его на экран.

# class Game:
#     def __init__(self,name) -> None:
#         self.__level = 0
#         self.name = name
        
#     def set_level(self,level):
#         self.__validate_name()
#         if self.name == 'Tolik':
#             self.__level = level
#         else:
#             print(f'{self.name} u are not Tolik')

#     def __validate_name(self):
#         self.name = self.name.capitalize()
    
#     def play(self,hours):
#         if hours > 2:
#             self.__level += 1
#         else:
#             return hours
        

#     def get_level(self):
#         return self.__level
    
# game2 = Game('Tolik')
# game2.set_level(10)
# print(game2.get_level())






# 9) Необходимо написать класс Game у которого есть приватный атрибут класса l
# evel который равен нулю. Напишите метод level с использование декоратора @property 
# для предоставления доступа к атрибуту level. Создайте экземпляр game класса Game. 
# Выведите на экран значение атрибута level.


# class Game:
#     def __init__(self,name) -> None:
#         self.__level = 0
#         self.name = name
        
#     @property
#     def level(self):
#         return self.__level
    
    
# game2 = Game('Tolik')
# print(game2.level)




# 10) Необходимо написать класс Game у которого есть приватный атрибут класса 
# level который равен нулю. Напишите метод level с использованием декоратора
#  @setter для того чтобы вы имели право на изменение приватного атрибута класса
#  level вне класса Game. Но обратите внимание что вы не сможете написать этот 
# метод без метода level у которого используется декоратор @property, поэтому также
#  создайте этот метод.
# Создайте экземпляр game класса Game. Выведите на экран значение атрибута level, 
# после 'легально' измените значение level на 10 и снова выведите это значение на экран.


# class Game:
#     def __init__(self,name) -> None:
#         self.__level = 0
#         self.name = name
        
#     @property
#     def level(self):
#         return self.__level
    
#     @level.setter
#     def level(self,value):
#         self.__level = value
    
#     def set_level(self,level):
#         self.__validate_name()
#         if self.name == 'Tolik':
#             self.__level = level
#         else:
#             print(f'{self.name} u are not Tolik')

#     def __validate_name(self):
#         self.name = self.name.capitalize()
    
#     def play(self,hours):
#         if hours > 2:
#             self.__level += 1
#         else:
#             return hours

    
# game2 = Game('Tolik')
# game2.level = 2
# print(game2.level)






# 11) Напишите класса Person, который будет хранить информацию о пользователе.
#  У обьекта будут следующие атрибуты экземпляра класса: имя(name), фамилия(last_name),
#  возраст(age), почта (email). При инициализации обьекта, передовать аргументы классу 
# не нужно, все его атрибуты по умолчанию будут равны None и также все они будут 
# приватными. Поэтому реализуйте для каждого атрибута методы доступа get и set 
# не используя декораторы property и setter. У вас будут такие методы: get_name,
#  set_name, get_last_name, set_last_name, get_age, set_age, get_email, set_email.
# Создайте экземпляр john класса Person выедите все его атрибуты, затем измените
#  их как показано ниже и после снова выведите на экран. Пример:
# john = Person()
# print(john.get_name()) # None
# print(john.get_last_name()) # None
# print(john.get_age()) # None
# print(john.get_email()) # None
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name()) # John
# print(john.get_last_name()) # Snow
# print(john.get_age()) # 30
# print(john.get_email()) # johnsnow@gmail.com


# class Person:
#     def __init__(self) -> None:
#         self.__name=None
#         self.__last_name=None
#         self.__age = None
#         self.__email = None
    
#     @property
#     def get_info(self):
#         return self.__name,self.__last_name,self.__age,self.__email

#     @get_info.setter
#     def get_info(self,info_tuple):
#         if len(info_tuple) == 4: 
#             self.__name, self.__last_name, self.__age, self.__email = info_tuple
#         else:
#             print("Invalid number of elements in info_tuple. Expected 4.")
    
    

# john = Person()
# john.get_info = ('John','Snow',30,'johnsnow@gmail.com')
# print(john.get_info)
# 12) Перепишите предыдущий класс используя декораторы property и setter. Условие:
#  Реализуйте класс Person, который будет хранить информацию о пользователе. 
# У обьекта будут следующие атрибуты экземпляра класса: имя(name),
#  фамилия(last_name), возраст(age), почта (email). 
# При инициализации обьекта, передовать аргументы классу не нужно, все его атрибуты 
# по умолчанию будут равны None и также все они будут приватными. Поэтому реализуйте
#  для каждого атрибута методы доступа get и set с помощью декораторов которые вы прошли.
# Создайте экземпляр john класса Person выедите все его атрибуты, затем измените 
# их как показано ниже и после снова выведите на экран. Пример:
# john = Person()
# print(john.name) # None
# print(john.last_name) # None
# print(john.age) # None
# print(john.email) # None
# john.name = 'John'
# john.last_name = 'Snow'
# john.age = 30
# john.email = 'johnsnow@gmail.com'
# print(john.name) # John
# print(john.last_name) # Snow
# print(john.age) # 30
# print(john.email) # johnsnow@gmail.com

# Согласитесь что этот способ использования декораторы 
# позваоляет писать более понятный и элегантный код


# class Person:
#     def __init__(self) -> None:
#         self.__name=None
#         self.__last_name=None
#         self.__age = None
#         self.__email = None
    
#     @property
#     def get_info(self):
#         return self.__name,self.__last_name,self.__age,self.__email

#     @get_info.setter
#     def get_info(self,info_tuple):
#         if len(info_tuple) == 4: 
#             self.__name, self.__last_name, self.__age, self.__email = info_tuple
#         else:
#             print("Invalid number of elements in info_tuple. Expected 4.")
    
    

# john = Person()
# john.get_info = ('John','Snow',30,'johnsnow@gmail.com')
# for an in john.get_info:
#     print(an)



# 13) Реализуйте класс Dad у которого будут следующие атрибуты класса:
#  name который равен 'John', защищенный атрибут last_name который равен 
# 'Snow' и приватный атрибут age равный 40. Затем реализуйте класс Me:
#  который будет наследоваться от класса Dad и будет содержать атрибуты
#  name равный 'Sam', защищенный атрибут last_name равный фамилии отца и
#  приватный атрибут age равный 10. Также реализуйте 2 метода: about_me 
# который выводит информацию об этом обьекте в виде: 'My name is Sam Snow
#  and I am 10 years old' и about_dad который выводит информацию об этом обьекте 
# в виде: 'My father is John Snow'. (Обратите внимание что в методе about_father
#  мы не выводим атрибут age обьекта отца, как этот атрибут приватный а это значит
#  что он не будет доступен в дочерних классах).
# Создайте экземпляр me класса Me и вызовите методы обьекта (их два).
# Ожидаемый результат: 
# My name is Sam Snow and I am 10 years old
# My father is John Snow

class Dad:
    name = 'John'
    _last_name = 'Snow'
    __age = 40

    

    
class Me(Dad):
    def __init__(self) -> None:
        super(Me,self).__init__()
        self.name = 'Sam'
        self._last_name = 'Snow'
        self.__age = 10
    
    def about_me(self):
        print(f'My name is {self.name} {self._last_name} and I am {self.__age} years old')
    
    def about_dad(self):
        return f'My father is {Dad().name} {Dad()._last_name}'
    

me = Me()
print(me.about_dad())
me.about_me()

