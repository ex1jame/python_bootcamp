
"""
1) Создайте функцию, которая будет принимать 2 числа, 
складывать их и возвращать результат сложения.
"""
# def sum_of_args(a: int,b: int,) -> int:
#         """Returns sum of given arguments"""
#         return a + b
# print(sum_of_args(15,2))
"""
2) Создайте функцию, которая будет принимать строку.
 Функция должна выводить длину этой строки(не использовать функцию len).
"""
# def line_str(text:str) -> str:
#         """Returns len of arguments"""
#         count = 0
#         for _ in text:
#                 count += 1
                
#         return count
# print(line_str('rfdnskjfdnjkfnrefnjewdnfklsd'))
"""
3) Создайте функцию, которая принимает два обязательных параметра. 
Задача этой функции выводить тип принятых аргументов.
"""
# def two_parametrs(a:int,b:str) -> type:
#     return print(type(a),type(b))
# two_parametrs(45,'fsdfdsfds')
"""
4) Создайте функцию, которая должна принимать 2 числа и возвращать результат их деления.
"""
# def divide_of_args(a: int,b: int,) -> int:
#         """Returns divide of given arguments"""
#         return a / b
# print(divide_of_args(15,2))
"""
5) Создайте функцию, которая принимает словарь. 
Пройдитесь по словарю циклом и распечатайте все его ключи
"""
# def dict_of_args(dict_test:dict) -> dict:
#         """Returns divide of given arguments"""
#         for _ in dict_test:
                
#             return dict_test.keys()
# dict_ = {
#     '123' : '321312',
#     '1232' : '321312',
#     '1242' : '321312',
# }
# print(dict_of_args(dict_))
"""
6) Создайте функцию, которая принимает и выводит "It's odd number" если это число не кратно двум и "It's even number" в противном случае.
"""
# def divide_of_args(a: int) -> str:
#         """Returns odd or even given arguments"""
#         if a % 2 == 0:
#                 print('It\'s even number')
#         else:
#                 print("It's odd number")
#         return a
# print(divide_of_args(13))
"""
7) Напишите функцию, которая будет принимать строку и проверять является ли она палиндромом. Пробелы и регистр учитывать не нужно.
(Палиндро́м, пе́ревертень — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях. Например, число 101; слова "кок", "топот", "комок" и т.д.)
"""
# def isPalindrome(string) -> str:
    
#     if string == string[::-1]:
#         print('Это палиндром')
#     else:
#         print('Не палиндром')
    
#     return string
# print(isPalindrome('kok'))

"""
😍 Создайте функцию которая принимает от пользователя два числа. Она должна сравнить эти числа между собой и вывести максимальное значение.
"""
# def isPalindrome(a:int,b:int) -> int:
    
#     if a == b:
#         print('равны')
#     elif a > b:
#         print('Первое число больше')
#     else:
#         print('Второе больше')

    
#     return a , b
# print(isPalindrome(5,6))
"""
9) Напишите функцию, которая принимает список чисел и возвращает их произведение.
"""
# def isPalindrome(a):
#     num = 1
#     for i in a:
#         num *= i
        
#     return num
# list_ = [1,2,3,4,5]
# print(isPalindrome(list_))
"""
10) Напишите функцию, которая принимает целое число и возвращает сумму всех его цифр.
 Например, число 123 --> 6
"""

# def isPalindrome(a):
#     string = str(a)
#     num = 0
#     for i in string:
#         num += int(i)
        
#     return num
# list_ = 1234
# print(isPalindrome(list_))


# Заядлый турист ведет тщательный учет своих походов. Во время последнего похода, который занял ровно шаги, за каждым шагом отмечалось, был ли это подъем в гору ,, или спуск ,шаг. Походы всегда начинаются и заканчиваются на уровне моря, и каждый шаг вверх или вниз представляет собойизменение единицы высоты. Мы определяем следующие термины:
# Гора – это последовательность последовательных ступенек над уровнем моря,
#  начиная со ступеньки вверх от уровня моря и заканчивая ступенькой вниз до уровня моря.
# Долина — это последовательность последовательных ступеней ниже уровня моря, начиная
#  со ступеньки вниз от уровня моря и заканчивая ступенькой вверх до уровня моря.
# Зная последовательность подъемов и спусков во время похода, найдите и выведите
#  количество пройденных долин .
# пример 1:
#  path = 8
#  steps = 'UDDDUDUU'
#  result = 1 dolina
# пример 2:
#  path = 10
#  steps = 'DUDDDUUDUU'
#  result = 2 dolina

def calculate_fuel_consumption(kilometers = 300, fuel_used = 30):print(f'На 100км было расходовано {((fuel_used / kilometers) * 100 ):.2f}л горючего')
calculate_fuel_consumption()