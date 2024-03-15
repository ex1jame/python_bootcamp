# # Типы данных в питоне: 

# # 1. NoneType - ничего, пустота -> None
# # 2. Boolean - истинна или ложь -> True/False(1/0)
# # 3. String - строки - str -> 'Hello wORLD', "hELLOW WORLD
# "My names is John Snow!"
# 'I\'m king'
# # 4. Числовые типа данных
#  a) integer - int -> -1,2,555
#    b)float - число с плавающей точкой -> 1.5 , 1.25, 1.3213
    #  C) complex - 1.3k
       
# 5. Списковые типы данных (коллекция)
# a) list(массив/список) -> [5, 3, 2, false, 'dead']
# b) tuple(кортеж) -> (1 , 3, 5, None)
# c) range(последовательность) -> range(1,10)
# 6. set() - множество ->  {1, 2, 3, 4, 5, 1, 'he'}без порядок
# 7.dict(словари) -> содержат данные в себе в виде пары ключ значение {1: 'HI', 2: true, 3:32}

# -------------------------------------------------------------------------------------------------------
# # mutable(изменяемый тип данных)
# 1 list
# 2 set
# 3 dict

# # Immutable(неизменяемый тип данных)
# 1 None
# 2 bool
# 3 int,float , complex
# 4 str 
# 5 tuple,range
# 6 frozenset
# -------------------------------------------------------------------------------------------------------

# Переменная - проименовання область памяти, предназначена для хранения данных.С ее помощью мы можем проводить различные операции
# PEP8 !!! УЗНАЙ ЧТО ЭТО

# listofnames = not recommended
# list_of_names = Snake case
# list0fName = Camel case

'''
Стандартный вывод данных
'''
# в питоне для вывода данных в терминале используется встроенная функция print()

# stroka = 'hi i\'m genius'

# print(stroka)
# print(1,2,3,4,5 sep='!',end=)

"""
Стандартный ввод данных
используется функция input()
"""

# name = input("Enter your name: " )
# print("Hello", name,end='!')sd

# str1 = input()
# print(str1)
# print(type(str1))

# num=5
# print(num)45

# print(type(num))

num1 = input('Enter num1: ')
num2 = input('Enter num2: ')
num1 = int(num1)
num2 = int(num2)

print(num1 * num2)