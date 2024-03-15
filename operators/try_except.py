# ОБРАБОТКА исключений
# Операторы try...except

# Ошибки Errors - синтаксис ошибки связанные с кодом
# SyntaxError
# IndentationError
# TabError

# Исключение Exceptions -> связаны с неправильными данными которые передаются в код, операции
ZeroDivisionError
ArithmeticError
NameError
IndexError
KeyError
ValueError
# BaseException  прородитель всех исключений
# try:
#     num1 = int(input('Enter the number1: '))
#     num2 = int(input('Enter the number2: '))

#     print(f'{num1} / {num2} == {num1 / num2}')
# except:
#     print("Invalid Values")
# print('Важный код')\
# try:
#     num1 = int(input('Enter the number1: '))
#     num2 = int(input('Enter the number2: '))

#     print(f'{num1} / {num2} == {num1 / num2}')
# except ValueError:
#     print("Чувак ты ввел неправильные данные для функции int!")
# except (ZeroDivisionError,KeyError):    
#     print('На ноль делить нельзя')
# else:
#     print('no errors')
# finally:
#     print('The end!')
# print('Важный код')

# -------------------------------------------------------------
# try:
    # <body> # код с вероятным исключение
# except:
    # <body except> сработает только если ошибка try
# else:
    # <body> сработает только если нет ошибки в try
# <finally>:
    # <body> сработает в любом случае

# import sys

# ls = [1,2,3,4,5]
# try:
#     index = int(input('vvedite index'))
# except:
#     print(f'oops , we catched {sys.exc_info()[0]} error')

# 2. Exception as <name(e)>

# ls = [1,2,3,4,5]
# while True:
#     try:
#         index = int(input('Vvedite index: '))
#         print(ls[index])
#     except Exception as e:
#         print(f'Oops, we catched {e.__class__} error!')

