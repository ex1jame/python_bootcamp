# 1) Создайте функцию, которая генерирует рандомное (случайно сгенерированное) 
# число и выводит на окно терминала через команду print(). Далее создайте декоратор, 
# который журналирует это событие. То есть функция декоратор должна писать в dict() 
# предложение: «Функция …………… была запущена успешно», а ключом будет уникальный 
# идентификатор (id).   (15 баллов)w
# import random as rn
# def jurnal(func):
#     journal_dict = {}
#     def wrapper(*args,**kwargs):
#         res = func(*args,**kwargs)
#         unique_id = id(res)
#         journal_dict[unique_id] = res
#         print(f"Функция {func.__name__} было успешно запущена,а ключом будет уникальным id:{unique_id}")
#         print(journal_dict)
#         return res
#     return wrapper
# @jurnal
# def random_int():
#     return rn.randint(1,100)
# random_number = random_int() 

# 2) Напишите функцию, которая принимает фразу, и возвращает его сокращенную форму.
# Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. For your interest -- FYI и т.п. (10 баллов)
# def string_cuts(string):
#     first_ele = ''
#     string = string.split(' ')
#     for word in string:
#         for element in word[0]:
#             first_ele += element
    
#     return print(first_ele.upper())
# string_cuts('Ruby on Rails')
# # 3) '''Напишите декоратор, который проверяет, 
# # что функция вызывается с определенными типами аргументов.''' (15 баллов)
# def type_check(excepted_type):
#     def decorator(func):
#         # print(excepted_type)
#         def wrapper(*args,**kwargs):
#             for arg in args:
#                 if not isinstance(arg,excepted_type):
#                     raise TypeError(f'Argument {arg} is not {func}')
#             res = func(*args,**kwargs)
#             print(f"Функция {func.__name__} было успешно запущена")
#             return res
#         return wrapper
#     return decorator

# @type_check(int)
# def int_num(*args):
#     list_ = []
#     for arg in args:
#         argus = arg * 2
#         list_.append(argus)
#     return list_
# print(int_num(5,5,5))
# 4) '''Создайте декоратор, который автоматически преобразует результат функции в другой тип данных,''' (15 баллов)
# def smena_types(transforms_type):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             res = []
#             for arg in args:
#                 res.append(transforms_type(arg))
#             # res = transforms_type(func(*args,**kwargs))
            
#             return res
#         return wrapper
#     return decorator

# @smena_types(int)
# def int_transform(*args):
#     list_ = []
#     for arg in args:
#         list_.append(arg)
#     return list_
# print(int_transform(10,25,'8'))



# wrapper_calls = 0
# # # 5) '''Реализуйте декоратор, который ограничивает максимальное количество вызовов функции.''' (20 баллов)
# def limit_calls(max_calls):
#     def decorator(func):
#         def wrapper(*arg,**kwargs):
#             nonlocal count
#             if count < max_calls:
#                 count += 1
#                 return func(*arg,**kwargs)
#             else:
#                 raise ValueError(f"Превышено кол во вызовоз функций")
        
#         count = 0
#         return wrapper
#     return decorator

# @limit_calls(3)
# def text_call():
#     return print('Serega')

# text_call()
# text_call()
# text_call()
# text_call()
# text_call()


        
# 6) '''Напишите декоратор, который автоматически логирует исключения, возникающие внутри функции.''' (15 баллов)

# def decorator(func):
#     def wrapper(*args,**kwargs):
#         try:
#             res = func(*args,**kwargs)
#             if int(res):
#                 return print(f'function {func.__name__} correct')
#             else:
#                 raise v
#         except ValueError as v:
#             print(v)
#         # return res
#     return wrapper
# @decorator
# def text_input():
#     return input('VVOd')
# text_input()
            
# 7) '''Напишите декоратор, который ограничивает доступ к функции только определенным пользователям или ролям.''' (15 баллов)\
def user_access(users):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for user in users:
                print(user)
                if 'name' in user and user['name'] == args[0] and 'roles' in user:
                    if 'admin' in user['roles']:
                        print('Разрешен доступ')
                        return func(*args, **kwargs)
                    else:
                        print('Вход запрещен для данной роли')
                        return None  # или можно вызвать исключение, в зависимости от требований
            print('Вход запрещен для данного пользователя')
            return None  # или можно вызв
        return wrapper
    return decorator
    
users=[
    {
        'name':'alena',
        'roles':'admin'
    },
    {
        'name':'igor',
        'roles':'admin'
    },
    {
        'name':'anar',
        'roles':'admin'
    },
    {
        'name':'genius',
        'roles':'user'
    },
]


@user_access(users)
def text_example(a):
    return a
text_example('anar')

# def user_access(users):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for user in users:
#                 if 'name' in user and user['name'] == args[0] and 'roles' in user:
#                     if 'admin' in user['roles']:
#                         print('Разрешен доступ')
#                         return func(*args, **kwargs)
#                     else:
#                         print('Вход запрещен для данной роли')
#                         return None  # или можно вызвать исключение, в зависимости от требований
#             print('Вход запрещен для данного пользователя')
#             return None  # или можно вызвать исключение, в зависимости от требований
#         return wrapper
#     return decorator
    
# users = [
#     {'name': 'alena', 'roles': 'admin'},
#     {'name': 'igor', 'roles': 'admin'},
#     {'name': 'anar', 'roles': 'admin'},
#     {'name': 'genius', 'roles': 'user'},
# ]

# @user_access(users)
# def text_example(a):
#     return a

# text_example('alena')
