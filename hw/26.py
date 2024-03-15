# # адание 1.
# # Есть список list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, 
# # "nursultan", 42, "ulukbek", "edil", 91, "nurlan", 1.5, 27.9]


 

# #      Написать функцию которая будет принимать этот список в качестве аргумента.
# #  Далее функция должна ВЕРНУТЬ список состоящий из имен(строковых значений) и чтобы
# # эти имена были с заглавной буквы и в алфавитном порядке
# #     Написать функцию которая будет принимать этот список в качестве аргумента. 
# # Далее функция должна ВЫВЕСТИ НА КОНСОЛЬ список из целочисленных значений в отсортированном
# # ?виде но в обратном порядке, т.е от большого к маленькому
# #     Написать функцию которая будет принимать этот список в качестве аргумента.
# #  Далее функция должна ВЕРНУТЬ сложение всех чисел с плавающей точкой
# # list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, "nursultan", 42, "ulukbek", "edil", 91, "nurlan", 1.5, 27.9]

# # def func_take_string(list):
# #     strings = []
# #     for word in list:
# #         if isinstance(word,str):
# #             word.capitalize()
# #             strings.append(word)
# #         strings.sort()
# #     return print(strings)
# # def func_take_chislo(list):
# #     chisla = []
# #     for number in list:
# #         if isinstance(number,int):
# #             chisla.append(number)
# #         chisla.sort(reverse=True)
# #     return print(chisla)
# # def func_take_float(list):
# #     sum_float = 0
# #     for number in list:
# #         if isinstance(number,float):
# #             sum_float += number
        
# #     return print(sum_float)
# # func_take_string(list_1)
# # func_take_chislo(list_1)
# # func_take_float(list_1)
# # Задание 2.
# # Сэндвичи: напишите функцию, которая получает первым аргументом размер сэндвича в 
# # виде строкового значения и список компонентов сэндвича.

# # При вызове функции, функция должна выводить описание заказанного сэндвича 
# # например «Большой сэндвич со следующими ингредиентами: огурец, колбаса … » .
# # Вызовите функцию три раза с разными количествами аргументов и разными размерами
# #  (Большой, средний, маленький)
# # def sandwich_type(size_sandwich:str,*components):
# #     components_str = ', '.join(components)
# #     return print(f'{size_sandwich} сэндвич со следующими ингрелиентами: ',components_str)
# # sandwich_type('Большой','Капуста','Сыр','Колбаса','Булки')
# # sandwich_type('Средний','Капуста','Сыр','Колбаса','Булки')
# # sandwich_type('Маленький','Капуста','Сыр','Колбаса','Булки')
 

# # Задание 3.
# # Напишите функцию для сохранения информации об автомобиле в словаре . 
# # Функция всегда должна возвращать производителя и название модели, но при 
# # этом она может получать произвольное количество именованных аргументов .
# #  Вызовите функцию с передачей обязательной информации и еще двух пар «имя—значение»
# #  (например, цвет и комплектация) . Ваша функция должна работать для вызовов следующего 
# # вида: car = make_car(‘subaru’, ‘outback’, colour=’blue’, engine='V8') и возвращать 
# # строку" Subaru Outback colour is blue, engine is V8

# def make_car(make,model,**components):
#     car = {'make': make, 'model' : model}
#     car.update(components)
#     return f"{car['make']} {car['model']} colour is {car.get('colour','unknown')}, engine is {car.get('engine','unknown')}"
# print(make_car('subaru', 'outback', colour='blue', engine='V8'))
    

# # Задача 4

# # Напишите функцию count_letters, которая принимает на вход текст и подсчитывает,
# #  какое в нём количество цифр и букв. Функция должна вывести на экран информацию 
# # о найденных буквах и цифрах в определённом формате.

# # Реализовать в цикле while, для выхода пользователь должен ввести "выход"

# # Пример:

# # Введите текст: 100 лет в обед

# # Какую цифру ищем? 0

# # Какую букву ищем? л

 

# # Количество цифр 0: 2

# # Количество букв л: 1
# while True:
#     text_user = input("Введите текст: ")
#     if text_user in 'выход':
#         break
#     guess = input('Какую букву ищем? ')
#     guess1 = input('Какую цифру ищем? ')
#     def count_letters(text):
#         count_letter = 0
#         count_digits = 0
#         for letter in text:
#             if guess == letter:
#                 count_letter += 1
#             if guess1 == letter:
#                 count_digits += 1

#         return print(f'Количество буквы {guess} = {count_letter} \nКоличество цифр {guess1} = {count_digits}')
#     count_letters(text_user)
# # Задача 5.

# # Напишите функцию, которая в виде аргумента принимает словарь 
# # (данные с именами и должностями , где ключ это имя работника,  а значение его должность.
# #  Функция должна вернуть предложения, типа:  
# # Работник Асан, занимает должность Директор
dict_={
    'Asan':'Director',
    'Geroy':'Vlastitel',
    'Daria':'Vlastitelnica',
}
def rabota(dictionary):
    for name,job in dictionary.items():
        print(f"Работник {name}, занимает должность {job}")
    return
rabota(dict_)

 

# # Задача 6 (дополнительно)

# # Напишите программу, которая будет суммировать все числа, введенные пользователем,
# #  игнорируя при этом нечисловой ввод. Выводите на экран текущую сумму чисел после каждого
# # очередного ввода. Ввод пользователем значения, не являющегося числовым, должен приводить 
# # к появлению соответствующего предупреждения, после чего пользователю должно быть предложено
# # ввести следующее число. Выход из программы будет осуществляться путем пропуска ввода.
# # Удостоверьтесь, что ваша программа корректно обрабатывает целочисленные значения и числа
# # с плавающей запятой.

# def summa():
#     sum_all = 0
#     while True:
#         chislo = input('Введите число: ')
        
#         if not chislo:
#             print("Ошибка, введите только числа")
#             break
#         try:
#             chislo = float(chislo)
#             sum_all += chislo
#             print(sum_all)
#         except ValueError:
#             print("Ошибка, введите только числа")
#     return print(f'Sum: {sum_all}')
# summa()
        
    
        
# # Пример:

# # Введите число: 1

# # Сумма: 1

# # Введите число: 2

# # Сумма: 3

# # Введите число: 5

# # Сумма: 8

# # Введите число: кукарача

# # Ошибка, введите только числа

# # Введите число: 12

# # Сумма: 20 (т.е. сумма не обнуляется, а продолжает "считать" (8 + 12 = 20)


# [Forwarded from Осмон]
# 1) '''Напишите функцию, принимающую на вход длины двух катетов прямо-
# угольного треугольника и возвращающую длину гипотенузы, рассчитан-
# ную по теореме Пифагора. В главной программе должен осуществляться
# запрос длин сторон у пользователя, вызов функции и вывод на экран
# полученного результата.'''
# import math
# def triangle():
#     katet1 = int(input('Длина 1 катета: '))
#     katet2 = int(input('Длина 2 катета: '))
#     gipotenuz = math.sqrt(katet1 ** 2 + katet2 ** 2 )
#     return print(f'Dlina gipotenuzy: {gipotenuz}')
# triangle()

# 2) '''Представьте, что сумма за пользование услугами такси складывается из
# базового тарифа в размере $4,00 плюс $0,25 за каждые 140 м поездки.
# Напишите функцию, принимающую в качестве единственного параметра
# расстояние поездки в километрах и возвращающую итоговую сумму опла-
# ты такси. В основной программе должен демонстрироваться результат
# вызова функции.'''

# def tax(distance:float):
#     base_tarif= 4.00
#     bonus_tarif = 0.25
#     distance_tarif = 0.140
#     surcharge = distance / distance_tarif
#     sum_tax = base_tarif + surcharge * bonus_tarif
#     return print(f'Сумма оплаты такси: {sum_tax:.2f}')
# tax(100)


# 3) '''Интернет-магазин предоставляет услугу экспресс-доставки для части
# своих товаров по цене $10,95 за первый товар в заказе и $2,95 – за все
# последующие. Напишите функцию, принимающую в качестве единствен-
# ного параметра количество товаров в заказе и возвращающую общую
# сумму доставки. В основной программе должны производиться запрос
# количест­ва позиций в заказе у пользователя и отображаться на экране
# сумма доставки.'''
# def sum_tovarov():
#     count_tovar = int(input('Count tovar: '))
#     base_tovar= 10.95
#     next_tovar = 2.95
#     surcharge = count_tovar * next_tovar
#     sum_tovar =  base_tovar + surcharge
#     return print(f'Сумма tovarov: {sum_tovar:.2f}')
# sum_tovarov()

# 4) '''Напишите функцию, которая будет принимать на вход три числа в качест­
# ве параметров и возвращать их медиану. В основной программе должен
# производиться запрос к пользователю на предмет ввода трех чисел, а так-
# же вызов функции и отображение результата.'''

# def mediana(a,b,c):
#     meditos = [a,b,c]
#     meditos.sort()
#     medianas = meditos[1]
#     return medianas

# print(mediana(7,2,5))
# 5) '''Используя решения из упражнений 100 и 102, напишите программу, ге-
# нерирующую случайный надежный пароль и выводящую его на экран.
# Посчитайте, с какого раза удастся создать пароль, отвечающий нашим
# требованиям надежности, и выведите на экран количество попыток. Им-
# портируйте функции из предыдущих упражнений и вызывайте их при
# необходимости для решения этой задачи.'''
# import secrets
# import string

# def is_strong(password):
#     return any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password)

# def generate_password(length=12):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(secrets.choice(characters) for _ in range(length))
#     return password

# def generate_strong_password():
#     attempts = 0
#     max_attempts = 1000 
#     while attempts < max_attempts:
#         password = generate_password()
#         if is_strong(password):
#             print(f'Сгенерированный надежный пароль: {password}')
#             print(f'Количество попыток: {attempts + 1}')
#             return
#         attempts += 1

#     print(f'Не удалось создать надежный пароль за {max_attempts} попыток.')


# generate_strong_password()
