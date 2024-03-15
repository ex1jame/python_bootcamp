# # # Типы данных числа -> int, float

# # # = ->оператор присваивания
# # num = 5
# # # print(num) 5
# # # num = 79  переопределение
# # # print(num) #79
# # num += 1 # num = num + 1
# # print(num) #80

# # abc -> нижний регистр
# # ABC -> ВЕРХНИЙ РЕГИСТР

# # PEP8 
# # tomorrow_day = '11.01.2024' Snake case
# # tomorrowDay = '11.01.2024' Camel case

# #  +


# # -
# # num1 = int(input('num1 '))
# # num2 = int(input('num2 '))
# # print(num2, '-', num1, '=', num2 - num1)

# # *
# # num1 = int(input('num1 '))
# # num2 = int(input('num2 '))
# # print(num2, '*', num1, '=', num2 * num1)

# # /(деление обычное) and //(без остатка) and %(модульное деление получение остатка)
# # num1 = 17
# # num2 = 9
# # print('/', num1 / num2)
# # print('//', num1 // num2)
# # # print('%', num1 % num2)

# # ** -> возведение в степень


# # print( 5 ** 2) возведение в степень

# # print(144 ** 0.5) квадратный корень
# # print(36 ** (1 / 2)) 

# # pow - возведение в степень
# # pow(num1, num2, <mod>)
# # print(pow(5, 2)) 5 ** 2
# # print(pow(5, 2, 2)) # 5 ** 2 % 2x

# # abs( ) - абсолютное значение числа -> abs(-5) -> 5

# # a = abs(-16)
# # b = abs(15)
# # c = abs(-4)

# # print(a,b,c)

# # round() - округление числа с плавающей
# # a = 5.49
# # print(round(a))

# # b = 7.3654845
# # print(round(b, 2))

# # divmod(a, b) - Она выводит два числа, первое число это результат целого деления(//), 
# # а второе число это модульное деление чисел a и b
 
# # print(22 / 5)
# # print(divmod(22, 5))
# # import math

# # a = 5
# # print(round(math.sqrt(5),2))

# # множественное присваивание
# # a = 'moloko'
# # b = 'water'
# # a , b = b , a

# # print(a, b )

# # num1, num2, num3 = input('num1'),input('num2'), input('num3')
# # print(num1)
# # print(num2)
# # print(num3)


# from random import randint  
# num = randint(1, 10)
# print(num)


# i = 0

# while i < 3:
#     guess = int(input('Guess the numhber: '))
#     if guess == num:
#         print('Ty horosh')
#         i = 32
#     i += 1

