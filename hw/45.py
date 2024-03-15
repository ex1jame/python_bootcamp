"""

1) Создайте класс Class1 с 2 любыми методами.
 Создайте второй класс Class2, 
 который наследуется от Class1, и
   определите в новом классе ещё 2 метода.
     Создайте экземпляр класса Class2. И вызовите у него все
       4 метода.

"""
# class Class1:
    # def __init__(self,color) -> None:
    #     self.color = color
    # def color_change(self,another):
    #     self.color = another
    #     return self.color
    # def start(self):
        # return f'GO ON'

# class Class2(Class1):
#     def __init__(self, color,model) -> None:
#         super().__init__(color)
#         self.model = model

#     def __str__(self):
#         return f'{self.color,self.model}'
    
#     def stop(self):
#         return f'srop'

# obj = Class2('black','horse')
# obj.color_change('white')
# obj.start()
# obj.stop()
# print(obj)

# писать код здесь

"""

2) Создайте класс A и определите в нём метод method1, 
который будет печатать строку "Основной функционал". 
Затем создайте второй класс B, который наследуется от 
класса A, и дополните method1 таким образом, чтобы он
 печатал также строку "Дополнительный функционал". 
 Объявите экземпляр класса B и вызовите метод method1.

"""
# class A:
#     def method1(self):
#         print(f'Основной функционал')

# class B(A):
#     def method1(self):
#         super().method1()
#         print(f'Дополнительный функионал')

# obj=B()
# obj.method1()
# писать код здесь

"""

3) Создайте класс MyString, который будет наследоваться от str. Определите 2 своих метода:

append, который будет принимать строку и добавлять её в конец исходной

pop, который удаляет из строки последний элемент и возвращает его.

Пример:

# example = MyString('String')

# example.append('hello')

# print(example) -> 'Stringhello'

# print(example.pop()) -> 'o'

# print(example) -> 'Stringhell'

"""

# class MyString:
#     def __init__(self,str1) -> None:
#         self.str = str1
#     def append(self,stroka):
#         self.str += stroka
#         return  self.str
#     def pop(self):
#         return f'{self.str[-1]}'

# obj=MyString('String')
# print(obj.append('hello'))
# print(obj.pop())

    
# писать код здесь
# class MyString(str):
#     def append(self, other_str):

#         return MyString(super(MyString, self).__add__(other_str))

#     def pop(self):

#         if len(self) == 0:
#             return ''
#         popped_char = self[-1]
#         return MyString(super(MyString, self)[:-1])

# example = MyString('String')
# example = example.append('hello')
# print(example)
# popped_char = example.pop()
# print(popped_char) 
# print(example)  


"""

4) Создайте класс MyDict который будет наследоваться от
 встроенного класса dict. Переопределите метод .get() 
 таким образом, чтобы при попытке получении несуществующего 
 ключа по умолчанию он вовзращал строку 'Are you kidding?'
   вместо None.

"""
# class MyDict(dict):
#     def get(self, key, default=None):
#         return super().get(key, 'Are you kidding?')

# my_dict = MyDict({'a': 1, 'b': 2})


# value_a = my_dict.get('a')
# print(value_a)



"""

5) Создайте класс Person который будет описывать человека, а точнее его имя и возраст. 
Создайте метод display(), который будет выводит данные об этом человеке.

Создайте второй класс Student, который будет наследоваться от класса Person, 
он должен принимать все атрибуты, которые были определены в родительском классе и 
добавьте еще один атрибут, который будет описывать направление студента. Создайте
 метод display_student(), который будет выводить данные об этом студенте.

Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, 
затем как о студенте.

"""
# class Person:
#     def __init__(self,name,old) -> None:
#         self.name = name
#         self.old = old
    
#     def display(self):
#         print(f'{self.name,self.old}')
    
# class Student(Person):
#     def __init__(self, name, old,facultet) -> None:
#         super().__init__(name, old)
#         self.facu = facultet
    
#     def display(self):
#         super().display()
#         print(self.facu)
    

# student = Student('raychel',18,'IT')
# student.display()
"""

6) Создайте класс ContactList, который должен наследоваться от встроенного класса list.
 В нем должен быть реализован метод search_by_name, который должен принимать имя и возвращать
список всех совпадений. Создайте экземпляр класса all_contacts и передайте список ваших контактов.

# """

# class ContactList(list):
#     def search_by_name(self, name):
#         matching_contacts = [contact for contact in self if name.lower() in contact.name.lower()]
#         return matching_contacts

# class Contact:
#     def __init__(self, name, phone_number):
#         self.name = name
#         self.phone_number = phone_number

# all_contacts = ContactList([
#     Contact("John Doe", "123-456-7890"),
#     Contact("Jane Smith", "987-654-3210"),
#     Contact("Bob Johnson", "555-123-4567"),
#     Contact("Alice Brown", "888-999-0000")
# ])

# search_result = all_contacts.search_by_name("John")
# print("Результаты поиска по имени 'John':", search_result)

# search_result = all_contacts.search_by_name("Alice")
# print("Результаты поиска по имени 'Alice':", search_result)

 

"""

7. Создайте класс Smartphone, экземпляры класса должны иметь такие свойства - name, color, memory, battery. battery по умолчанию

должно быть 0. Переопредилите метод str так чтобы при распечатке он выдавал строку с названием и памятью смартфона.

У данного класса также должен быть метод charge, который увеличивает значение батареи на указанную величину.

 

Создайте два дочерних класса от Smartphone - Iphone и Samsung.

У Iphone должен быть дополнительный аттрибут - ios и метод send_imessage - возвращает строку с сообщением и от какого телефона оно было выслано.

А у Samsung должен быть дополнительный аттрибут android и метод show_time, который показывает текущее время.

Создайте объекты от данных классов и примените все методы.

"""
# class Smartphone:
#     def __init__(self, name, color, memory, battery=0):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = battery

#     def charge(self, amount):
#         self.battery += amount

#     def __str__(self):
#         return f"{self.name} ({self.memory}GB)"

# class Iphone(Smartphone):
#     def __init__(self, name, color, memory, ios_version, battery=0):
#         super().__init__(name, color, memory, battery)
#         self.ios = ios_version

#     def send_imessage(self, message):
#         return f"iMessage from {self.name} ({self.memory}GB): {message}"

# class Samsung(Smartphone):
#     def __init__(self, name, color, memory, android_version, battery=0):
#         super().__init__(name, color, memory, battery)
#         self.android = android_version

#     def show_time(self):
#         import datetime
#         current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         return f"{self.name} ({self.memory}GB) current time: {current_time}"

# iphone = Iphone("iPhone 13", "Silver", 128, "iOS 15")
# samsung = Samsung("Galaxy S21", "Black", 256, "Android 12")

# print(iphone)  
# print(samsung)  

# iphone.charge(50)
# samsung.charge(30)

# print(f"iPhone battery level: {iphone.battery}%")
# print(f"Samsung battery level: {samsung.battery}%")

# message_result = iphone.send_imessage("Hello from iPhone")
# print(message_result)

# time_result = samsung.show_time()
# print(time_result)

 

"""

8. Создайте класс Spell для магических заклинаний, экземпляры класса имеют два аттрибута - name - название и
 formula - полное произношение заклинания.

У класса есть два метода: get_description() - дает полное описание заклинания и execute() - совершает заклинание.

Переопределите у класса метод str, чтобы он выдавал вам название, формулу и описание вместе, к примеру:
Открытие замков: Alohomora

позволяет магу попасть в любую комнату,

способно открыть любую закрытую замочную скважину.

 

Наследуя от класса Spell создайте три заклинания,переопределяя в них родительские методы. Создайте объекты этих трех заклинаний. Вызовите все методы

"""
# class Spell:
#     def __init__(self, name, formula):
#         self.name = name
#         self.formula = formula

#     def get_description(self):
#         return f"{self.name} - {self.formula}"

#     def execute(self):
#         return f"{self.name} spell is cast successfully."

#     def __str__(self):
#         return f"{self.name}: {self.formula}\n{self.get_description()}"


# class Alohomora(Spell):
#     def get_description(self):
#         return "Allows the wizard to access any room, capable of opening any locked door."

# class Expelliarmus(Spell):
#     def get_description(self):
#         return "Disarms the opponent by causing their wand or weapon to fly out of their hand."

# class Patronus(Spell):
#     def get_description(self):
#         return "Conjures a magical guardian, called a Patronus, to protect against dark creatures and entities."
# alohomora_spell = Alohomora("Unlocking Charm", "Alohomora")
# expelliarmus_spell = Expelliarmus("Disarming Charm", "Expelliarmus")
# patronus_spell = Patronus("Patronus Charm", "Expecto Patronum")



# print(alohomora_spell)
# print(alohomora_spell.execute())



# print(expelliarmus_spell)
# print(expelliarmus_spell.execute())

# print(patronus_spell)
# print(patronus_spell.execute())

 

"""

9. Напишите класс CustomError который наследуется от встроенного класса исключений Exception. 
Переопределите init таким образом

чтобы через экземпляр класса можно было передавать сообщение и создавать новые виды исключений.

Создайте исключение от этого класса с сообщением:

"ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ"

 

Напишите функцию проверяющую строки на регистр и если строка не написана в верхнем регистре выбросите исключение созданное классом CustomError:

 

Traceback (most recent call last):

  File "inheritance.py", line 121, in <module>

    check_letters(a)

  File "inheritance.py", line 117, in check_letters

    raise capitals_error

main.CustomError: ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ

 

"""
# class CustomError(Exception):
#     def __init__(self, message: object) -> None:
#         super().__init__(message)
        
# capital_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')
    
# def upper_error(input_str):
#     if not input_str.isupper():
        
#         raise capital_error


# a = 'HEdsds'

# try:
#     upper_error(a)
# except CustomError as e:
#     print(f'Исключение {e}')
        

 

"""

10. Создайте класс Character с помощью которого можно создавать героев для игры. Экземпляры класса должны иметь аттрибут name. У класса должна быть переменная power_list, в которой хранится словарь:

power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }

 

Класс должен иметь методы:

give_weapon - выбирает случайное оружие из списка

 

give_role - выбирает случайную роль из списка, к примеру:

["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]

 

give_powers, передавая силу и значение можно менять power_list для определенного героя, к примеру:

char1.give_powers('ловкость', 5)

увеличит ловкость вашего героя.

 

Создайте три разных дочерьних класса от класса Character - Elf, Orc, DragonBorn,

дайте каждому из классов уникальный метод и добавьте уникальные аттрибуты экземпляра класса,наследуя init от Character. Создайте несколько героев от этих классов и вызовите их методы и методы родительского класса Character.

"""
from random import choice

class Character:
    def __init__(self, name) -> None:
        self.name = name
        self.power_list = {'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0}

    def give_weapon(self):
        weapons = ["Меч", "Лук", "Топор", "Посох", "Кинжал"]
        return choice(weapons)

    def give_role(self):
        roles = ["Варвар", "Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
        return choice(roles)

    def give_powers(self, power, value):
        if power in self.power_list:
            self.power_list[power] += value

class Elf(Character):
    def __init__(self, name, bow_skill) -> None:
        super().__init__(name)
        self.bow_skill = bow_skill

    def elf_special_ability(self):
        return "Скрытность и ловкость эльфов помогают избегать врагов."

class Orc(Character):
    def __init__(self, name, brute_strength) -> None:
        super().__init__(name)
        self.brute_strength = brute_strength

    def orc_special_ability(self):
        return "Силовые характеристики орков делают их мощными в ближнем бою."

class DragonBorn(Character):
    def __init__(self, name, breath_weapon) -> None:
        super().__init__(name)
        self.breath_weapon = breath_weapon

    def dragonborn_special_ability(self):
        return "Дыхание дракона придает драконорожденным уникальное оружие."

# Пример использования
elf_character = Elf("Леголас", 8)
print(f"{elf_character.name} получил оружие: {elf_character.give_weapon()}")
print(f"{elf_character.name} выбрал роль: {elf_character.give_role()}")
elf_character.give_powers('ловкость', 5)
print(f"{elf_character.name} улучшил свою ловкость: {elf_character.power_list['ловкость']}")
print(elf_character.elf_special_ability())

orc_character = Orc("Громмаш", 10)
print(f"{orc_character.name} получил оружие: {orc_character.give_weapon()}")
print(f"{orc_character.name} выбрал роль: {orc_character.give_role()}")
orc_character.give_powers('сила', 8)
print(f"{orc_character.name} улучшил свою силу: {orc_character.power_list['сила']}")
print(orc_character.orc_special_ability())

dragonborn_character = DragonBorn("Сапфир", "Огненное дыхание")
print(f"{dragonborn_character.name} получил оружие: {dragonborn_character.give_weapon()}")
print(f"{dragonborn_character.name} выбрал роль: {dragonborn_character.give_role()}")
dragonborn_character.give_powers('интеллект', 7)
print(f"{dragonborn_character.name} улучшил свой интеллект: {dragonborn_character.power_list['интеллект']}")
print(dragonborn_character.dragonborn_special_ability())

 