"""
1) Проверить введенное пользователем число и если оно больше 5 то вывести “True”, иначе “False”.
# """
# guess = int(input("Число: "))
# while guess > 5:
#     print("True")
#     break
# else:
#     print('False')
    
"""
2) Проверить введенные пользователем данные и если длина 
строки больше или равна 5 символам вывести “True” иначе “False”.
"""
# guess = input("Stroku: ")
# len_guess = len(guess)
# while len_guess >= 5:
#     print("True")
#     break
# else:
#     print('False')
    
"""
3) Проверить введенное пользователем значение если оно больше 
или равно 90, вывести “Отлично ваша оценка 5”, если значение больше или равно
 80, вывести “Здорово ваша оценка 4”, если значение больше или равно 70, вывести 
 “Хорошо ваша оценка 3”, если значение больше или равно 60, вывести “Вам стоит подучить материал", 
 в других случаях “вы не сдали экзамен”.
"""
# guess = int(input("Число: "))
# while True:
#     if guess >= 90:
#         print("Отлично ваша оценка 5")
#         break
#     if guess >= 80:
#         print("Отлично ваша оценка 4")
#         break
        

#     if guess >= 70:
#         print("Отлично ваша оценка 3")
#         break
        

#     if guess >= 60:
#         print("Вам стоит подучить материал")
#         break
        

#     else:
#         print("вы не сдали экзамен")
#         break
        



"""
4) Проверить введенное пользователем число если оно отрицательное то вывести 
“negative”, если положительное то “positive”, если оно равно 0 то вывести “Zero”
"""
# guess = int(input("Число: "))
# while True:
#     if guess > 0:
#         print("positive")
#         break
#     elif guess < 0:
#         print("negative")
#         break
#     else:
#         print("zero")
#         break
"""
5) Даны два целых числа. Выведите значение наименьшего из них.
"""
# numbers = [45 , 32]
# min_num = min(numbers)
# print(min_num)

"""
6) Даны три целых числа. Выведите значение наименьшего из них.
"""
# numbers = [45 , 32,12]
# min_num = min(numbers)
# print(min_num)
"""
7) Даны три целых числа. Определите, сколько среди них совпадающих. 
Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).
"""
# ls_num = [2,1,10]

# while True:
#     if ls_num[0] == ls_num[1] == ls_num[2]:
#         print("3")
#         break
#     if ls_num[0] == ls_num[1] or ls_num[1] == ls_num[2] or ls_num[0] == ls_num[2]:
#         print("2")
#         break
#     else:
#         print("0")
#         break


"""
8) Вводятся два целых числа. Проверить делится ли первое на второе. Вывести на экран сообщение об этом, 
частное (в любом случае), а также остаток от деления (если он есть). input: 678 23 
output: 678 не делится на 23 
Частное: 29 
Остаток: 11
"""
# a = 678
# b = 23
# c = b // a

# while True:
#     if b // a == 0:
#         print(f"не делится {a} на {b}")
#         print(f"Остаток: {b % a},частное: {c}")
        
#         break
#     else:
#         print("делится")
#         break
    
"""
9) Дано номер года. Требуется определить, является ли год 
с данным номером високосным. Если год является високосным,
 то выведите YES, иначе выведите NO. Напомним, что в соответствии с 
 григорианским календарем, год является високосным, если его номер кратен 4,
   но не кратен 100, а также если он кратен 400.
"""
year = 2024

while True:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(" Високосным ")
        break
    else:
        print("Не високосный")
        break
"""
10)  Перевести число, введенное пользователем, в байты или килобайты в зависимости от его выбора.
"""
# num = int(input("chislo: "))
# guess = int(input('1 bite 2 kilobite'))
# while True:
#     if guess == 1:
#         print(f"{num / 1000}bite")
#         break
#     if guess == 2:
#         print(f"{num * 1000} kilobite")
#         break

""" 
11) Создайте список при помощи встроенной функции.
"""
# ls_list = [1,2,3,4]
# print(ls_list)

"""
12) Дан список list_ = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333, ]. 
Посчитайте сколько раз встречается (333), (3.1432) и ('n').
"""
# list_ip = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333]
# count_ip = list_ip.count(333)
# count_ip2 = list_ip.count(3.1432)
# count_ip3 = list_ip.count('n')
# print(count_ip)
# print(count_ip2)
# print(count_ip3)

"""
13) Дан список list_ = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333, ].
 Узнайте под каким индексом лежит (86) и удалите (1546.89).
"""

# list_ip = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333, ]
# print(list_ip.index(86))
# print(list_ip.pop(5))
# print(list_ip)

"""
14) Дан список list_ = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333, ]. Сперва отсортируйте его по возрастанию, а затем переверните его.
"""

# list_ip = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333]
# list_ip.sort()
# list_ip.sort(reverse=True)

# print(list_ip)
# print(list_ip[::-1])
"""
15) Создайте два списка, и расширьте список тремя разными путями.
"""

# list1 = [1,2,3]
# list2 = [4,5,6]
# list1.append(list2)
# list1.extend(list2)
# list3 = list1 + list2
# print(list3)
"""
16) Создайте кортеж только с одним элементом и выведите его тип данных.
"""
# a = (1)
# print(type(a))
"""
17) Создайте кортеж при помощи встроенной функции.
"""
# a = 1,2,3,4
# a = tuple(a)
# print(a)
""" 
18)Дан кортеж tuple_ = ('a', 1, 'Hello', True, ['1', 'b']). Возвратите новый кортеж удалив слово 'Hello'.
"""
# tuple_list = ('a', 1, 'Hello', True, ['1', 'b'])
# tuple_list = list(tuple_list)
# print(tuple_list.pop(2))
# print(tuple_list)
# Пишите код здесь

"""
19) Дан кортеж tuple_ = ('b', 1, 'Hello', True, ['False', 'b'], None, ('tuple')).
 Выведите элементы только с чётными индексами.
"""
# tuple_time = ('b', 1, 'Hello', True, ['False', 'b'], None, ('tuple'))
# counter = 0
# for x in tuple_time:
#     if counter % 2 == 0:
#         print(x)
#     counter += 1